# main.py


from app.app_utilities import AppUtilitiesClass

from PySide6.QtCore import Signal, Slot
import os
import cantools



from layers.threadObj_base import ThreadObj_base

class ThreadObj_App_dbcDecode(ThreadObj_base):
    def __init__(self):
        super().__init__()
        self.isCancelDecode = True  # 是否取消解析

    @Slot()
    def cancel_decoding_slot(self):
        self.isCancelDecode = True

    @Slot(str, str)
    def parse_dbc_file(self, file_name, sqlDatabaseName):
        
        self.singal_tipsPrint.emit("Start DBC parsing")
        self.singal_tipsPrint.emit("DBC parsing....")
        # 连接数据库
        db = AppUtilitiesClass.sqlDB_connect(sqlDatabaseName)

        # 表名
        tableName = os.path.basename(file_name)
        tableName = tableName[:-4]
        
        # Load DBC file
        dbc_db = cantools.database.load_file(file_name)

        # Get all messages in the DBC file
        messages = dbc_db.messages

        if len(messages) > 0:
            proStatus_info = {
                "name": "dbcDecode",
                "tips": "dbc decoding...",
                "threadObj_cancelFunc" : self.cancel_decoding_slot
            }
            proStatus_valueMax = len(messages)
            proStatus_value = 0
            # 通知主界面启动一个进度条对话框
            self.signal_processStatusStart.emit(proStatus_info)
            self.isCancelDecode = False
            # Store signals in the database
            for msg in messages:
                if self.isCancelDecode:
                    self.signal_dialog_info.emit("dbc decode has been canceled!")
                    self.signal_processStatusSetValue.emit(111)
                    break
                # 设置进度条的值
                proStatus_value = proStatus_value + 1
                value = int(float(proStatus_value) / proStatus_valueMax * 100)
                self.signal_processStatusSetValue.emit(value)
                for sig in msg.signals:
                    data_dict = {
                        "signal_name": sig.name,
                        "frame_id": hex(msg.frame_id),
                        "start_bit": str(sig.start),
                        "len_bit" : str(sig.length),
                        "byte_order" : sig.byte_order,
                    }
                    
                    # 把结果写进数据库
                    AppUtilitiesClass.sqlDB_insert_dbcDecodeData(db, tableName, data_dict)

        AppUtilitiesClass.sqlDB_disconnect(db)

        # 解析完成
        if self.isCancelDecode:
            self.singal_tipsPrint.emit("DBC parsing cancel")
            self.signal_dbcDecode_complete.emit(tableName)
        else:
            self.singal_tipsPrint.emit("DBC parsing complete")
            self.signal_dbcDecode_complete.emit(tableName)

    # dbc 解析完成信号, 发送保存解析结果的表名
    signal_dbcDecode_complete = Signal(str)

    
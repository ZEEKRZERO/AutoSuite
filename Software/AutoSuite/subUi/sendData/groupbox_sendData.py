
from PySide6.QtWidgets import QMessageBox, QFileDialog, QVBoxLayout, QMenu, QDialog
from PySide6.QtGui import QAction, QStandardItemModel, QStandardItem, QIcon
from PySide6 import QtWidgets
from PySide6.QtCore import Signal, Slot, Qt, QSize,QTimer, QThread


from app.app_utilities import AppUtilitiesClass

from subUi.sendData.ui_groupbox_sendData import Ui_GroupBox_sendData
from subUi.sendData.dialog_addSendFrame import Dialog_addSendFrame

from layers.appDataLay.appBusSendData import ThreadObj_App_busSendData

class GroupBox_sendData(QtWidgets.QDialog):
    def __init__(self, threadObj_ioPort, parent=None):
        super().__init__(parent)
        self.ui = Ui_GroupBox_sendData()
        self.setWindowModality(Qt.NonModal) # 设置为非模态，允许与其他窗口交互
        self.ui.setupUi(self)

        self.threadObj_ioPort = threadObj_ioPort

        self.ui.comboBox_busType.blockSignals(True)

        self.timerisCreated_send = False

        self.ui.comboBox_busType.addItem("Can")
        self.ui.comboBox_busType.addItem("FlexRay")
        self.ui.comboBox_busType.addItem("Lin")
        self.ui.comboBox_busType.addItem("Ethernet")
        self.ui.comboBox_busType.addItem("CanFD")
        self.ui.comboBox_busType.setCurrentText("Can")

        self.model_tableView_headers = []
        self.model_tableView_data = QStandardItemModel()
        self.model_tableView_data_currentRow = 0

        self.setTableTitle_tableView_data()

        self.ui.comboBox_busType.blockSignals(False)

        # 发送线程管理
        self.threadObj_sendBusData = None
        self.thread_sendBusData = None

        # 配置 发送线程
        self.thread_cfg_threadObj_sendBusData()

    
    # 发送线程配置
    def thread_cfg_threadObj_sendBusData(self):
        if self.thread_sendBusData is not None:
            return
        
        # 创建线程
        self.thread_sendBusData = QThread(self)
        self.threadObj_sendBusData = ThreadObj_App_busSendData()
        self.threadObj_sendBusData.moveToThread(self.thread_sendBusData)
        self.thread_sendBusData.finished.connect(self.thread_sendBusData.deleteLater)
        self.thread_sendBusData.finished.connect(self.threadObj_sendBusData.deleteLater)

        # 信号连接
        self.threadObj_sendBusData.signal_busSendData.connect(self.threadObj_ioPort.devices_sendByteArrays_slot)
        self.threadObj_ioPort.signal_devices_info_disconnect.connect(self.cancel_timer_send)  # 设备断开连接，停止定时发送
        self.signal_sendBusData.connect(self.threadObj_sendBusData.packAndSendBusData_slot)
        # self.destroyed.connect(lambda:(
        #     self.thread_sendBusData.quit,
        #     print("thread_sendBusData stop")
        # ))
        self.rejected.connect(lambda:(
            self.thread_sendBusData.quit,
            print("thread_sendBusData stop")
        ))

        # 启动线程
        self.thread_sendBusData.start() 

    @Slot()
    def cancel_timer_send(self):
        self.ui.checkBox_repeat.setChecked(False)
    

    # 设置 tableView_data 表头
    def setTableTitle_tableView_data(self):
        self.model_tableView_headers= []
        if self.ui.comboBox_busType.currentText() == "Can":
            self.model_tableView_headers = ["Channel","FrameID","Length","Data"]
        elif self.ui.comboBox_busType.currentText() == "FlexRay":
            self.model_tableView_headers = ["Channel","FrameID","Length","Data"]
        elif self.ui.comboBox_busType.currentText() == "Lin":
            self.model_tableView_headers = ["Channel","FrameID","Length","Data"]
        elif self.ui.comboBox_busType.currentText() == "Ethernet":
            self.model_tableView_headers = []
        elif self.ui.comboBox_busType.currentText() == "CanFD":
            self.model_tableView_headers = ["Channel","FrameID","Length","Data"]
        
        self.model_tableView_data.setHorizontalHeaderLabels(self.model_tableView_headers)
        self.ui.tableView_data.setModel(self.model_tableView_data)
    
    # 往 tableView_data 里添加数据
    def addTableData_tableView_data(self, data_dict):
        if self.model_tableView_data_currentRow > 2000 :
            self.model_tableView_data_currentRow = 0
            self.model_tableView_data.clear()
            self.setTableTitle_tableView_data()

        col = 0
        for header in self.model_tableView_headers:
            item = QStandardItem(data_dict[header])
            self.model_tableView_data.setItem(self.model_tableView_data_currentRow, col, item)
            col = col + 1

        self.ui.tableView_data.setModel(self.model_tableView_data)
        self.model_tableView_data_currentRow = self.model_tableView_data_currentRow + 1

    # 清空发送表格的数据   
    @Slot()
    def on_pushButton_clearData_clicked(self):
        # 创建消息对话框
        msg_box = QMessageBox()
        msg_box.setText(f"确认清空发送总线数据表格?")
        msg_box.setWindowTitle("提示")
        msg_box.setIcon(QMessageBox.Information)
        msg_box.addButton("确认", QMessageBox.AcceptRole)
        msg_box.addButton("取消", QMessageBox.RejectRole)
        icon = QIcon()
        icon.addFile(u":/icons/zeekr", QSize(), QIcon.Normal, QIcon.Off)
        msg_box.setWindowIcon(icon)

        # 弹出对话框并等待用户操作
        response = msg_box.exec()
        if response == 0:
            self.model_tableView_data_currentRow = 0
            self.model_tableView_data.clear()
            self.setTableTitle_tableView_data()
            self.singal_tipsPrint.emit(f"成功清空发送总线数据表格！")


    # 添加要发送的数据
    @Slot()
    def on_pushButton_addData_clicked(self):
        dialog = Dialog_addSendFrame(busType=self.ui.comboBox_busType.currentText(), parent=self)
        if dialog.exec_() == QDialog.Accepted:
            # 向表格添加数据
            if len(dialog.data_dict) > 0 and self.ui.comboBox_busType.currentText() != "Ethernet" :
                self.addTableData_tableView_data(dialog.data_dict)


    # 发送总线数据
    @Slot()
    def on_pushButton_sendData_clicked(self):
        
        # 从表格获取要发送的数据
        list_busFrames = []

        row_count = self.ui.tableView_data.model().rowCount()

        for row in range(row_count):
            row_data = {}
            header_view = self.ui.tableView_data.horizontalHeader()
            for column in range(self.ui.tableView_data.model().columnCount()):
                item = self.ui.tableView_data.model().item(row, column)
                key = self.ui.tableView_data.model().headerData(column, header_view.orientation())
                if item is not None:
                    row_data[key] = item.text()
                else:
                    row_data[key] = item.text()
                row_data["busType"] = self.ui.comboBox_busType.currentText()
            
            list_busFrames.append(row_data)

        # 发送信号，通知发送线程对数据进行发送
        self.signal_sendBusData.emit(list_busFrames)

    # 定时发送
    @Slot()
    def on_checkBox_repeat_stateChanged(self):
        if self.ui.checkBox_repeat.isChecked() :
            if self.timerisCreated_send == False:
                self.timerisCreated_send = True
                self.timer_send=QTimer() 
                self.timer_send.timeout.connect(self.on_pushButton_sendData_clicked)
                # self.destroyed.connect(lambda self :(
                #     print("timer_send del"),
                #     self.timer_send.stop(),
                #     self.timer_send.deleteLater
                #     ))
                self.rejected.connect(lambda:(
                    print("send Data timer_send del"),
                    self.timer_send.stop(),
                    self.timer_send.deleteLater
                ))
            interValue = self.ui.spinBox_repeatInterValue.value()
            self.timer_send.setInterval(interValue)  
            self.timer_send.start()
        else:
            self.timer_send.stop()

    # 总线类型改变
    @Slot(int)
    def on_comboBox_busType_currentIndexChanged(self, index):
        # 清空数据并重新设置表头
        self.model_tableView_data_currentRow = 0
        self.model_tableView_data.clear()
        self.setTableTitle_tableView_data()

    # 输出提示信息信号
    singal_tipsPrint = Signal(str)

    # 信号，通知发送总线数据
    signal_sendBusData = Signal(list)


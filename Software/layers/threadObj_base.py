# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass



from PySide6.QtCore import QObject
from PySide6.QtCore import Signal, Slot, QTimer


# 线程对象的基类
class ThreadObj_base(QObject):
    def __init__(self):
        super().__init__()


    # 基本信号连接
    def base_connect(self, obj_ui):
        self.signal_processStatusStart.connect(obj_ui.info_processStatus_start_slot)
        self.signal_processStatusSetValue.connect(obj_ui.info_processStatus_updateValue_slot)
        self.singal_tipsPrint.connect(obj_ui.app_print)
        self.signal_dialog_info.connect(obj_ui.info_dialog_slot)


    # 进度条开始信号
    signal_processStatusStart= Signal(dict)
    # 进度条值设置信号
    signal_processStatusSetValue = Signal(int)

    # 提示信息输出信号
    singal_tipsPrint = Signal(str)

    # 弹出提示对话框信号
    signal_dialog_info = Signal(str)



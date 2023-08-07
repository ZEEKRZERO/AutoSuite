# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass


from PySide6 import QtWidgets
from PySide6.QtCore import Signal, Slot, Qt, QThread

from subUi.rawDataDis.ui_groupbox_rawdatadis import Ui_GroupBox_rawDataDis

from layers.middleDataLay.middleDataLay import ThreadObj_MiddleData



class GroupBox_rawDataDis(QtWidgets.QDialog):
    def __init__(self, threadObj_ioPort, parent=None):
        super().__init__(parent)
        self.ui = Ui_GroupBox_rawDataDis()
        self.ui.setupUi(self)

        self.threadObj_ioPort = threadObj_ioPort

        # 信号连接
        self.ui.checkBox_hexDisplay.stateChanged.connect(lambda :(self.signal_ui_gbRawData_hexDisplay.emit(self.ui.checkBox_hexDisplay.isChecked())))
        self.ui.checkBox_suspendDis.stateChanged.connect(lambda :(self.signal_ui_gbRawData_SuspendDis.emit(self.ui.checkBox_suspendDis.isChecked())))

        self.ui.pushButton_clearDisplay.clicked.connect(lambda :(self.reflash_rawDataDisplay_slot("",True)))
        self.ui.pushButton_clearTx.clicked.connect(lambda :(self.ui.plainTextEdit_txData.clear()))
        self.ui.pushButton_tx.clicked.connect(self.send_raw_data)


        # 发送线程管理
        self.threadObj_handData = None
        self.thread_handData = None

        # 配置 发送线程
        self.thread_cfg_threadObj_handData()

    # 中间数据层设备配置
    def thread_cfg_threadObj_handData(self):

        if self.threadObj_handData is not None:
            return

        # 创建线程
        self.thread_handData = QThread(self)
        self.threadObj_handData = ThreadObj_MiddleData()
        self.threadObj_handData.moveToThread(self.thread_handData)
        self.thread_handData.finished.connect(self.thread_handData.deleteLater)
        self.thread_handData.finished.connect(self.threadObj_handData.deleteLater)

        # 信号连接
        self.threadObj_ioPort.signal_devices_readData.connect(self.threadObj_handData.receive_raw_data_slot)
        self.threadObj_handData.signal_ui_flash_raw_data.connect(self.reflash_rawDataDisplay_slot)
        self.signal_ui_gbRawData_hexDisplay.connect(self.threadObj_handData.set_isDisplay_hex_slot)
        self.signal_ui_gbRawData_SuspendDis.connect(self.threadObj_handData.set_isDisplay_Suspend_slot)
        self.signal_ui_gbRawData_SendData.connect(self.threadObj_ioPort.devices_sendByteArrays_slot)
        self.destroyed.connect(self.thread_handData.quit)

        # 启动线程
        self.thread_handData.start()



    # 刷新显示的数据，str为要显示的字符串，isClear，表示是否清空显示
    @Slot(str, bool)
    def reflash_rawDataDisplay_slot(self, str, isClear):
        if self.ui.textBrowser_rxData.textCursor().position() - self.ui.textBrowser_rxData.document().firstBlock().position()  > 1000000 :
            isClear = True
        if  isClear :
            self.ui.textBrowser_rxData.clear()
        self.ui.textBrowser_rxData.append(str)
        self.ui.textBrowser_rxData.verticalScrollBar().setValue(self.ui.textBrowser_rxData.verticalScrollBar().maximum())


    # 发送原始数据
    @Slot()
    def send_raw_data(self) :
        string = self.ui.plainTextEdit_txData.toPlainText()
        byte_stream = None

        if self.ui.checkBox_hexSend.isChecked() :
            # 16 进制发送
            byte_stream = bytes.fromhex(string)
        else :
            # ASCII 发送
            byte_stream = string.encode('ascii')
            pass

        if self.ui.checkBox_sendNewLine.isChecked() :
            byte_stream += "\r\n".encode('ascii')

        print(byte_stream)
        # 发送发送信号
        self.signal_ui_gbRawData_SendData.emit(byte_stream)


    # 界面通知，进行十六进制显示，参数为 True，表示进行ASCII显示
    signal_ui_gbRawData_hexDisplay = Signal(bool)

    # 界面通知，进行原始数据发送，参数为 True，表示暂停显示
    signal_ui_gbRawData_SuspendDis = Signal(bool)

    # 界面通知，进行原始数据发送，参数为要发送的字节数组
    signal_ui_gbRawData_SendData = Signal(bytes)

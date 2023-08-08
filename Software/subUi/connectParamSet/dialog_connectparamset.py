# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass

from PySide6 import QtWidgets
from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QFileDialog

import serial
import serial.tools.list_ports

from subUi.connectParamSet.ui_dialog_connectparamset import Ui_Dialog_connectParamSet

from app.app_utilities import AppUtilitiesClass


class Dialog_connectParamSet(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Dialog_connectParamSet();
        self.ui.setupUi(self)

        # 默认连接参数字典
        self.connectParamDict = {
            "connectMode": "WIFI",
            "USB": {
                "VID": "0808",
                "PID": "8081"
            },
            "WIFI": {
                "IP": "www.baidu.com",
                "PORT": "80"
            },
            "UART": {
                "com": "COM3",
                "baudRate": "115200",
                "dataBits": "8",
                "parity": "0",
                "stopBits": "1"
            },
            "CANCfg": {
                "SPD": "500K",
                "RES120": "ENABLE"
            },
            "FRCfg": {
                "NODE": "NodeSend"
            }
        }

        # 连接方式种类定义
        self.ui.comboBox_connectMode.insertItem(0, "UART")
        self.ui.comboBox_connectMode.insertItem(1, "WIFI")
        self.ui.comboBox_connectMode.insertItem(2, "USB")

        # fr配置选择
        self.ui.comboBox_cfgFile.insertItem(0, "NodeSend.xml")
        self.ui.comboBox_cfgFile.insertItem(1, "NodeRecv.xml")

        # can配置选择
        self.ui.comboBox_canCfg_spd.insertItem(0, "500K")
        self.ui.comboBox_canCfg_spd.insertItem(1, "250K")

        # 串口选择参数设置
        self.ui.comboBox_uartBuadRate.addItem("115200")
        self.ui.comboBox_uartBuadRate.setDisabled(True)
        self.ui.comboBox_uartCheakBits.addItem("0")
        self.ui.comboBox_uartDataBits.addItem("8")
        self.ui.comboBox_uartStopBits.addItem("1")

        # 信号连接

        # 加载参数
        self.load_connectParam(True)


    def load_connectParam(self, isFirstLoad=False):

        self.connectParamDict = AppUtilitiesClass.cfgParam_connect_load()

        # print(self.connectParamDict)

        if isFirstLoad :
            self.ui.comboBox_connectMode.blockSignals(True)
            self.ui.comboBox_connectMode.setCurrentText(self.connectParamDict["connectMode"])
            self.ui.comboBox_connectMode.blockSignals(False)
            self.ui.stackedWidget.setCurrentIndex(self.ui.comboBox_connectMode.currentIndex())
            # FR
            self.ui.comboBox_cfgFile.setCurrentText(self.connectParamDict["FRCfg"]["NODE"]+".xml")
            # CAN
            self.ui.comboBox_canCfg_spd.setCurrentText(self.connectParamDict["CANCfg"]["SPD"])
            if self.connectParamDict["CANCfg"]["RES120"] == "ENABLE":
                self.ui.checkBox_canCfg_r120.setChecked(True)
            else:
                self.ui.checkBox_canCfg_r120.setChecked(False)
            

        if self.ui.comboBox_connectMode.currentText() == "WIFI" :
            self.ui.lineEdit_IPAddr.setText(self.connectParamDict["WIFI"]["IP"])
            self.ui.lineEdit_IPPort.setText(self.connectParamDict["WIFI"]["PORT"])
            self.ui.pushButton_reflsh_com.hide()
        elif self.ui.comboBox_connectMode.currentText() == "UART" :
            self.ui.comboBox_uartPort.clear()
            self.ui.comboBox_uartPort.addItem(self.connectParamDict["UART"]["com"])
            self.ui.comboBox_uartBuadRate.setCurrentText(self.connectParamDict["UART"]["baudRate"])
            self.ui.comboBox_uartDataBits.setCurrentText(self.connectParamDict["UART"]["dataBits"])
            self.ui.comboBox_uartCheakBits.setCurrentText(self.connectParamDict["UART"]["parity"])
            self.ui.comboBox_uartStopBits.setCurrentText(self.connectParamDict["UART"]["stopBits"])
            self.ui.pushButton_reflsh_com.show()
        elif self.ui.comboBox_connectMode.currentText() == "USB" :
            self.ui.lineEdit_VID.setText(self.connectParamDict["USB"]["VID"])
            self.ui.lineEdit_PID.setText(self.connectParamDict["USB"]["PID"])
            self.ui.pushButton_reflsh_com.hide()

    @Slot(int)
    def on_comboBox_connectMode_currentIndexChanged(self, index):
        self.ui.stackedWidget.setCurrentIndex(self.ui.comboBox_connectMode.currentIndex())
        self.load_connectParam()

    @Slot()
    def on_pushButton_reflsh_com_clicked(self):

        # 遍历可用的串口名
        list_ports = list(serial.tools.list_ports.comports())
        self.ui.comboBox_uartPort.clear()
        if len(list_ports) > 0:
            for port in list_ports:
                self.ui.comboBox_uartPort.addItem(port.device)


    @Slot()
    def on_pushButton_ok_clicked(self) :
    
        # FR
        self.connectParamDict["FRCfg"]["NODE"] = self.ui.comboBox_cfgFile.currentText().split(".")[0]
        # CAN
        self.connectParamDict["CANCfg"]["SPD"] == self.ui.comboBox_canCfg_spd.currentText()
        if self.ui.checkBox_canCfg_r120.isChecked():
            self.connectParamDict["CANCfg"]["RES120"] = "ENABLE"
        else:
            self.connectParamDict["CANCfg"]["RES120"] = "DISABLE"

        self.connectParamDict["connectMode"] = self.ui.comboBox_connectMode.currentText()
        if self.connectParamDict["connectMode"] == "WIFI" :
            self.connectParamDict["WIFI"]["IP"] = self.ui.lineEdit_IPAddr.text()
            self.connectParamDict["WIFI"]["PORT"] = self.ui.lineEdit_IPPort.text()
        elif self.connectParamDict["connectMode"] == "UART" :
            self.connectParamDict["UART"]["com"] = self.ui.comboBox_uartPort.currentText()
            self.connectParamDict["UART"]["baudRate"] = self.ui.comboBox_uartBuadRate.currentText()
            self.connectParamDict["UART"]["dataBits"] = self.ui.comboBox_uartDataBits.currentText()
            self.connectParamDict["UART"]["parity"] = self.ui.comboBox_uartCheakBits.currentText()
            self.connectParamDict["UART"]["stopBits"] = self.ui.comboBox_uartStopBits.currentText()
        elif self.connectParamDict["connectMode"] == "USB" :
            self.connectParamDict["USB"]["VID"] = self.ui.lineEdit_VID.text()
            self.connectParamDict["USB"]["PID"] = self.ui.lineEdit_PID.text()

        # 保存配置参数
        AppUtilitiesClass.cfgParam_connect_save(self.connectParamDict)

        # 发送连接参数更新信号
        self.signal_CfgParam_connect_update.emit()
        # 退出对话框
        self.accept()

    @Slot()
    def on_pushButton_cancel_clicked(self):
        # 退出对话框
        self.reject()

    @Slot()
    def on_pushButton_newNode_clicked(self):
        # 创建文件选择对话框实例
        file_dialog = QFileDialog(self)
        # 设置对话框选项
        file_dialog.setDirectory("./data/frNodeCfg")
        file_dialog.setFileMode(QFileDialog.ExistingFile) 
        # 显示对话框并获取选择的文件
        selected_file, _ = file_dialog.getOpenFileName(caption="Open xml File",filter="XML files (*.xml)")
        if selected_file:
            pass

    # 连接参数更新信号
    signal_CfgParam_connect_update = Signal()


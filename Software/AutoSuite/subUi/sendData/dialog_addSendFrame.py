# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass


from PySide6.QtWidgets import QMessageBox, QFileDialog
from PySide6 import QtWidgets
from PySide6.QtCore import Signal, Slot, Qt

from subUi.sendData.ui_dialog_addSendFrame import Ui_Dialog_addSendFrame

class Dialog_addSendFrame(QtWidgets.QDialog):
    def __init__(self, busType="Can", parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog_addSendFrame()
        self.ui.setupUi(self)

        self.ui.comboBox_busType.addItem("Can")
        self.ui.comboBox_busType.addItem("FlexRay")
        self.ui.comboBox_busType.addItem("Lin")
        self.ui.comboBox_busType.addItem("Ethernet")
        self.ui.comboBox_busType.addItem("CanFD")
        self.ui.comboBox_busType.setCurrentText(busType)
        self.ui.comboBox_busType.setEnabled(False)

        self.data_dict = {}


    @Slot(int)
    def on_comboBox_busType_currentIndexChanged(self, index):
        self.ui.stackedWidget_main.setCurrentIndex(self.ui.comboBox_busType.currentIndex())

    
    @Slot()
    def on_pushButton_ok_clicked(self) :
        
        self.data_dict = {
            "busType" : self.ui.comboBox_busType.currentText()
        }

        if self.ui.comboBox_busType.currentText() == "Can":
            self.data_dict["Channel"] = self.ui.lineEdit_can_channel.text()
            self.data_dict["FrameID"] = self.ui.lineEdit_can_frameID.text()
            self.data_dict["Length"] = self.ui.lineEdit_can_length.text()
            self.data_dict["Data"] = self.ui.lineEdit_can_data.text()
        elif self.ui.comboBox_busType.currentText() == "FlexRay":
            self.data_dict["Channel"] = self.ui.lineEdit_flexRay_channel.text()
            self.data_dict["FrameID"] = self.ui.lineEdit_flexRay_frameID.text()
            self.data_dict["Length"] = self.ui.lineEdit_flexRay_length.text()
            self.data_dict["Data"] = self.ui.lineEdit_flexRay_data.text()
        elif self.ui.comboBox_busType.currentText() == "Lin":
            self.data_dict["Channel"] = self.ui.lineEdit_lin_channel.text()
            self.data_dict["FrameID"] = self.ui.lineEdit_lin_frameID.text()
            self.data_dict["Length"] = self.ui.lineEdit_lin_length.text()
            self.data_dict["Data"] = self.ui.lineEdit_lin_data.text()
        elif self.ui.comboBox_busType.currentText()  == "Ethernet":
            pass
        elif self.ui.comboBox_busType.currentText()  == "CanFD":
            self.data_dict["Channel"] = self.ui.lineEdit_canFD_channel.text()
            self.data_dict["FrameID"] = self.ui.lineEdit_canFD_frameID.text()
            self.data_dict["Length"] = self.ui.lineEdit_canFD_length.text()
            self.data_dict["Data"] = self.ui.lineEdit_canFD_data.text()
        # 退出对话框
        self.accept()

    @Slot()
    def on_pushButton_cancel_clicked(self):
        # 退出对话框
        self.reject()
# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass


from PySide6.QtWidgets import QMessageBox, QFileDialog
from PySide6 import QtWidgets
from PySide6.QtCore import Signal, Slot, Qt


from app.app_utilities import AppUtilitiesClass

from subUi.signalFuzz.ui_dialog_selectSignal import Ui_dialog_selectSignal

class Dialog_selectSignal(QtWidgets.QDialog):
    def __init__(self, isNeedUB, parent=None):
        super().__init__(parent)
        self.ui = Ui_dialog_selectSignal()
        self.ui.setupUi(self)

        if isNeedUB:
            self.ui.checkBox_isUseUB.setEnabled(True)
        else:
            self.ui.checkBox_isUseUB.setEnabled(False)

        # 存储传递的数据
        self.cfgParam_dict = {
            "selfDefineSignalName" : "",
            "isUseUB" : False
        }

    @Slot()
    def on_pushButton_cancel_clicked(self):
        self.reject()

    @Slot()
    def on_pushButton_ok_clicked(self):

        self.cfgParam_dict = {
            "selfDefineSignalName" : self.ui.lineEdit_selfDefineSignalName.text(),
            "isUseUB" : self.ui.checkBox_isUseUB.isChecked()
        }
        self.accept()  # 关闭对话框并返回数据

   
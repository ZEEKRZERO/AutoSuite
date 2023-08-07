# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass



from PySide6.QtWidgets import QMessageBox, QFileDialog
from PySide6 import QtWidgets
from PySide6.QtCore import Signal, Slot, Qt

from subUi.signalFuzz.ui_dialog_fuzzSetting import Ui_Dialog_fuzzSetting

class Dialog_fuzzSetting(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog_fuzzSetting()
        self.ui.setupUi(self)

    @Slot()
    def on_pushButton_ok_clicked(self) :

        # 退出对话框
        self.accept()

    
    @Slot()
    def on_pushButton_cancel_clicked(self):
        # 退出对话框
        self.reject()
# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass


from PySide6.QtWidgets import QMessageBox, QFileDialog
from PySide6 import QtWidgets
from PySide6.QtCore import Signal, Slot, Qt


from subUi.about.ui_dialog_about import Ui_Dialog_about

class Dialog_about(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog_about()
        self.ui.setupUi(self)





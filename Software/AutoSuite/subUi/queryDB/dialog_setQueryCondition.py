# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass



from PySide6.QtWidgets import QMessageBox, QFileDialog
from PySide6 import QtWidgets
from PySide6.QtCore import Signal, Slot, Qt


from subUi.queryDB.ui_dialog_setQueryCondition import Ui_dialog_setCondition

class Dialog_setCondition(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_dialog_setCondition()
        
        self.ui.setupUi(self)

    def setup_editFormConnect(self):
        itemNum = int(self.ui.formLayout_setCondition.count() / 2)
        print(itemNum)
        for i in range(itemNum):
            item_label = self.ui.formLayout_setCondition.itemAt(i).widget()
            item_lineEdit = self.ui.formLayout_setCondition.itemAt(i+1).widget()
            # print(item_label.text())
            label = item_label.text().split('\n')
            print("lable", label)
            lineEdit_text = item_label.text().split('\n')[0]
            # print(label)
            # print(lineEdit_text)
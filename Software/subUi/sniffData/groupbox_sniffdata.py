# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass



from PySide6 import QtWidgets
from PySide6.QtCore import Signal, Slot, Qt, QThread
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView, QHeaderView,QTableWidgetItem
from PySide6.QtGui import QStandardItemModel, QStandardItem

from subUi.sniffData.ui_groupbox_sniffdata import Ui_GroupBox_sniffData
from subUi.sniffData.dialog_sniffdatasetting import Dialog_sniffDataSetting

from layers.appDataLay.appBusReslove import ThreadObj_App_busReslove

from app.app_utilities import AppUtilitiesClass


class GroupBox_sniffData(QtWidgets.QDialog):
    def __init__(self, threadObj_ioPort, parent=None):
        super().__init__(parent)
        self.ui = Ui_GroupBox_sniffData()
        self.ui.setupUi(self)

        self.ui.checkBox_suspend.blockSignals(True)
        self.ui.checkBox_rtSave.blockSignals(True)

        self.ui.checkBox_rtSave.setChecked(True)

        # 显示计数
        self.busDataItemsCnt = 0
        self.ui.lineEdit_itemsCnt.setText(str(self.busDataItemsCnt))

        self.threadObj_ioPort = threadObj_ioPort

        self.model_tableView_mianTable = QStandardItemModel()
        self.model_tableView_mianTable_currentRow = 0

        # self.sniffDataParam = AppUtilitiesClass.cfgParam_sniffData_load()
        self.updateSniffDataParam_slot()

        # 信号连接
        self.ui.pushButton_setting_2.clicked.connect(self.dialogCfg_dialog_sniffdatasetting)


        self.ui.checkBox_suspend.blockSignals(False)
        self.ui.checkBox_rtSave.blockSignals(False)


        # 总线解析线程管理
        self.threadObj_appBusReslove = None
        self.thread_appBusReslove = None
        # 配置总线解析线程
        self.thread_cfg_threadObj_appBusReslove()

        


    # 总线数据解析线程配置
    def thread_cfg_threadObj_appBusReslove(self):

        if self.threadObj_appBusReslove is not None:
            return

        # 创建线程
        self.thread_appBusReslove = QThread(self)
        self.threadObj_appBusReslove = ThreadObj_App_busReslove()
        self.threadObj_appBusReslove.moveToThread(self.thread_appBusReslove)
        self.thread_appBusReslove.finished.connect(self.thread_appBusReslove.deleteLater)
        self.thread_appBusReslove.finished.connect(self.threadObj_appBusReslove.deleteLater)

        # 信号连接
        self.threadObj_appBusReslove.signal_sendBytes.connect(self.threadObj_ioPort.devices_sendByteArrays_slot)
        self.threadObj_appBusReslove.signal_busDataDecodedReslut.connect(self.refrashBusData_slot)
        self.threadObj_ioPort.signal_devices_readData.connect(self.threadObj_appBusReslove.receive_packet_slot)
        self.destroyed.connect(self.thread_appBusReslove.quit)
        
        # 启动线程
        self.thread_appBusReslove.start()


    @Slot()
    def updateSniffDataParam_slot(self):
        self.sniffDataParam = AppUtilitiesClass.cfgParam_sniffData_load()
        headers = ["Channel","ReceiveTime","BusType","FrameID","FrameType","DataLength","Data","Timestamp"]
        self.model_tableView_mianTable.setHorizontalHeaderLabels(headers)
        self.ui.tableView_mianTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView_mianTable.verticalHeader().setVisible(False)

        self.ui.tableView_mianTable.setModel(self.model_tableView_mianTable)




    # 配置抓取参数设置对话框 
    @Slot()
    def dialogCfg_dialog_sniffdatasetting(self) :
        # 创建对话框
        dialog = Dialog_sniffDataSetting()
        # 对话框信号连接

        # 显示对话框
        dialog.exec()

    @Slot()
    def on_pushButton_clear_2_clicked(self):
        self.model_tableView_mianTable_currentRow = 0
        self.model_tableView_mianTable.clear()
        self.busDataItemsCnt = 0
        self.ui.lineEdit_itemsCnt.setText(str(self.busDataItemsCnt))
        self.updateSniffDataParam_slot()

    @Slot()
    def on_checkBox_suspend_stateChanged(self):
        # 暂停or继续抓取
        if self.threadObj_appBusReslove is not None:
            status = self.ui.checkBox_suspend.isChecked()
            self.threadObj_appBusReslove.suspendDecodeBusData = status
    @Slot()
    def on_checkBox_rtSave_stateChanged(self):
        # 是否实时保存到数据库当中
        if self.threadObj_appBusReslove is not None:
            status = self.ui.checkBox_rtSave.isChecked()
            self.threadObj_appBusReslove.suspendSaveData2DB = not status


    @Slot(dict)
    def refrashBusData_slot(self,decoded_dict):

        if self.model_tableView_mianTable_currentRow > 2000 :
            self.model_tableView_mianTable_currentRow = 0
            self.model_tableView_mianTable.clear()
            self.updateSniffDataParam_slot()

        item = QStandardItem(decoded_dict["channel"])
        self.model_tableView_mianTable.setItem(self.model_tableView_mianTable_currentRow, 0, item)
        item = QStandardItem(decoded_dict["receiveTime"])
        self.model_tableView_mianTable.setItem(self.model_tableView_mianTable_currentRow, 1, item)
        item = QStandardItem(decoded_dict["busType"])
        self.model_tableView_mianTable.setItem(self.model_tableView_mianTable_currentRow, 2, item)
        item = QStandardItem(decoded_dict["frameID"])
        self.model_tableView_mianTable.setItem(self.model_tableView_mianTable_currentRow, 3, item)
        item = QStandardItem(decoded_dict["frameType"])
        self.model_tableView_mianTable.setItem(self.model_tableView_mianTable_currentRow, 4, item)
        item = QStandardItem(decoded_dict["dataLength"])
        self.model_tableView_mianTable.setItem(self.model_tableView_mianTable_currentRow, 5, item)
        item = QStandardItem(decoded_dict["data"])
        self.model_tableView_mianTable.setItem(self.model_tableView_mianTable_currentRow, 6, item)
        item = QStandardItem(decoded_dict["timestamp"])
        self.model_tableView_mianTable.setItem(self.model_tableView_mianTable_currentRow, 7, item)

        self.ui.tableView_mianTable.setModel(self.model_tableView_mianTable)
        self.ui.tableView_mianTable.scrollToBottom()


        self.model_tableView_mianTable_currentRow = self.model_tableView_mianTable_currentRow + 1

        self.busDataItemsCnt = self.busDataItemsCnt + 1
        # 显示计数
        self.ui.lineEdit_itemsCnt.setText(str(self.busDataItemsCnt))
        








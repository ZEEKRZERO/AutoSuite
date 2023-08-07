# This Python file uses the following encoding: utf-8
import sys

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

from PySide6.QtWidgets import QApplication, QMessageBox, QProgressDialog

from PySide6 import QtWidgets
from PySide6.QtCore import Signal, Slot, QThread, Qt, QUrl, QTranslator, QLibraryInfo, QLocale
from PySide6.QtGui import QDesktopServices

import datetime

from ui_mainwindow import Ui_MainWindow

from app.app_utilities import AppUtilitiesClass
from layers.deviceLay.connectDeviceLay import ThreadObj_IOManage

from subUi.connectParamSet.dialog_connectparamset import Dialog_connectParamSet
from subUi.rawDataDis.groupbox_rawdatadis import GroupBox_rawDataDis
from subUi.sniffData.groupbox_sniffdata import GroupBox_sniffData

from subUi.queryDB.dialog_querysniffdb import Dialog_querySniffDB
from subUi.signalFuzz.groupbox_signalFuzz import GroupBox_signalFuzz
from subUi.about.dialog_about import Dialog_about
from subUi.sendData.groupbox_sendData import GroupBox_sendData  


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.progress_dialog = None

        # 子视图
        self.subUi_rawData = None
        self.subUi_subWinHand_rawData =None

        self.subUi_sniffData = None
        self.subUi_subWinHand_sniffData =None

        self.subUi_signalFuzz = None
        self.subUi_subWinHand_signalFuzz =None

        self.dialogList_send_data = []
        
        # 加载连接参数
        self.connectParam = AppUtilitiesClass.cfgParam_connect_load()

        # Io线程配置
        self.thread_cfg_threadObj_ioPort()
        
        # action 连接
        self.initActionsConnections()

        # 启动设备管理线程
        self.thread_ioPort.start()


    def initActionsConnections(self):

        # 失能设备连接与断开按钮
        self.ui.action_Connect.setEnabled(False)
        self.ui.action_Disconnect.setEnabled(False)

        # 动作连接
        self.ui.action_Connect.triggered.connect(lambda:(
            self.signal_device_connect.emit()
        ))
        self.ui.action_Disconnect.triggered.connect(lambda:(
            self.signal_device_disconnect.emit()
        ))

        # 视图打开与关闭管理      
        self.ui.action_connectParamSet.triggered.connect(self.dialogCfg_dialog_connectParamSet)
        self.ui.action_historyQuery.triggered.connect(self.dialogCfg_dialog_querySniffDB)
        self.ui.action_about.triggered.connect(self.dialogCfg_dialog_about)
        self.ui.action_send_data.triggered.connect(self.dialogCfg_dialog_send_data)
        self.ui.action_dbcDecode.triggered.connect(self.dialogCfg_dialog_dbcDecode)
        self.ui.action_helpDoc.triggered.connect(lambda:(
            QDesktopServices.openUrl(QUrl("www.autosuite.org"))
        ))
        self.ui.action_swLanguage.triggered.connect(self.switch_language_slot)
        

        self.ui.action_rawDis.triggered.connect(lambda isCheacked : (
            self.createOrDeleteMDIAreaSubUi_rawDataDis(self.ui.action_rawDis, isCheacked, self.ui.mdiArea_main)))
        self.ui.action_sniff.triggered.connect(lambda isCheacked : (
            self.createOrDeleteMDIAreaSubUi_sniffData(self.ui.action_sniff, isCheacked, self.ui.mdiArea_main)))
        self.ui.action_signalFuzz.triggered.connect(lambda isCheacked : (
            self.createOrDeleteMDIAreaSubUi_signalFuzz(self.ui.action_signalFuzz, isCheacked, self.ui.mdiArea_main)))
        

        self.ui.action_Connect.setEnabled(True)
        self.ui.action_Disconnect.setEnabled(False)

    # 多语言切换
    @Slot(bool)
    def switch_language_slot(self, isChecked):

        translator = QTranslator()
        if isChecked:
            # 英文显示
            # translator.load("translations/your_app_en.qm")
            print("English")
        else:
            # 中文显示
            # translator.load("translations/your_app_zh.qm")
            print("Chinese")

        # QApplication.instance().installTranslator(translator)
        # self.retranslateUi()

    # 设备层线程配置
    def thread_cfg_threadObj_ioPort(self):

        # 创建线程
        self.thread_ioPort = QThread(self)
        self.threadObj_ioPort = ThreadObj_IOManage(self.connectParam)
        self.threadObj_ioPort.moveToThread(self.thread_ioPort)
        self.thread_ioPort.finished.connect(self.thread_ioPort.deleteLater)
        self.thread_ioPort.finished.connect(self.threadObj_ioPort.deleteLater)

        # 信号连接 
        self.threadObj_ioPort.base_connect(self) # 基本信号连接
        self.signal_device_connect.connect(self.threadObj_ioPort.devices_open_slot)
        self.signal_device_disconnect.connect(self.threadObj_ioPort.devices_close_slot)

        self.threadObj_ioPort.signal_devices_info_connectState.connect(self.ui_info_connectState_slot)
        self.threadObj_ioPort.signal_devices_info_disconnect.connect(self.ui_info_disconnect_slot)


        # # 启动线程
        # self.thread_ioPort.start()

    # mdiArea 子UI配置   原始数据显示 子UI
    def createOrDeleteMDIAreaSubUi_rawDataDis(self, action, isCreate, mdiArea):

        if isCreate:
            # 创建子UI
            self.subUi_rawData = GroupBox_rawDataDis(threadObj_ioPort=self.threadObj_ioPort, parent=self)
            # 连接信号

            # 添加并显示 子 UI
            self.subUi_subWinHand_rawData = mdiArea.addSubWindow(self.subUi_rawData)
            self.subUi_rawData.show()
            self.subUi_subWinHand_rawData.destroyed.connect(lambda : (
                action.blockSignals(True),
                action.setChecked(False),
                action.blockSignals(False)
            ))
        else:
            self.subUi_rawData.close()
            mdiArea.setActiveSubWindow(self.subUi_subWinHand_rawData)
            mdiArea.closeActiveSubWindow()

    # mdiArea 子UI配置   数据抓取 子UI
    def createOrDeleteMDIAreaSubUi_sniffData(self, action, isCreate, mdiArea):

        if isCreate:
            # 创建子UI
            self.subUi_sniffData = GroupBox_sniffData(threadObj_ioPort=self.threadObj_ioPort, parent=self)

            # 添加并显示 子 UI
            self.subUi_subWinHand_sniffData = mdiArea.addSubWindow(self.subUi_sniffData)
            self.subUi_sniffData.show()
            self.subUi_subWinHand_sniffData.destroyed.connect(lambda : (
                action.blockSignals(True),
                action.setChecked(False),
                action.blockSignals(False)
            ))
        else:
            self.subUi_sniffData.close()
            mdiArea.setActiveSubWindow(self.subUi_subWinHand_sniffData)
            mdiArea.closeActiveSubWindow()

    # mdiArea 子UI配置   信号 fuzz
    def createOrDeleteMDIAreaSubUi_signalFuzz(self, action, isCreate, mdiArea):

        if isCreate:
            # 创建子UI
            self.subUi_signalFuzz = GroupBox_signalFuzz(mainWin=self, threadObj_ioPort=self.threadObj_ioPort, parent=self)
            # 连接信号
            self.subUi_signalFuzz.singal_tipsPrint.connect(self.app_print)            
            # 添加并显示 子 UI
            self.subUi_subWinHand_signalFuzz = mdiArea.addSubWindow(self.subUi_signalFuzz)
            self.subUi_signalFuzz.show()
            self.subUi_subWinHand_signalFuzz.destroyed.connect(lambda : (
                action.blockSignals(True),
                action.setChecked(False),
                action.blockSignals(False)
            ))
        else:
            self.subUi_signalFuzz.close()
            mdiArea.setActiveSubWindow(self.subUi_subWinHand_signalFuzz)
            mdiArea.closeActiveSubWindow()
            
    # 设备连接状态消息提示
    @Slot(bool)
    def ui_info_connectState_slot(self, isSuccess):
        if isSuccess:
            QMessageBox.information(None, "device connect status", "device connect successfully!")
            self.ui.action_Connect.setEnabled(False)
            self.ui.action_Disconnect.setEnabled(True)
        else:
            QMessageBox.critical(None, "device connect status", "device connect failed!")
            self.ui.action_Connect.setEnabled(True)
            self.ui.action_Disconnect.setEnabled(False)        

    # 设备断开消息提示
    @Slot()
    def ui_info_disconnect_slot(self):
        QMessageBox.information(None, "device connect status", "device disconnect!")
        self.ui.action_Connect.setEnabled(True)
        self.ui.action_Disconnect.setEnabled(False)

    # 配置 参数配置对话框 
    @Slot()
    def dialogCfg_dialog_connectParamSet(self) :
        # 创建对话框
        dialog = Dialog_connectParamSet()
        # 对话框信号连接
        dialog.signal_CfgParam_connect_update.connect(self.threadObj_ioPort.devices_updateConnectParam_slot)

        self.dialogList_send_data.append(dialog)
        # 显示对话框
        dialog.exec()

    # 配置 数据库查询对话框 
    @Slot()
    def dialogCfg_dialog_querySniffDB(self) :
        # 创建对话框
        dialog = Dialog_querySniffDB(mainWin=self, parent=self)
        dialog.ui.pushButton_dbcDecode.setVisible(False)
        # 对话框信号属性设置
        # winflags = Qt.Dialog
        # winflags |= Qt.WindowMaximizeButtonHint
        # dialog.setWindowFlag(winflags)
        # 对话框信号连接
        dialog.singal_tipsPrint.connect(self.app_print)
        
        # 显示对话框
        dialog.exec()
    # 配置 发送总线数据对话框
    @Slot()
    def dialogCfg_dialog_send_data(self) :

        # 创建对话框
        dialog = GroupBox_sendData(threadObj_ioPort=self.threadObj_ioPort, parent=self)
        # 连接信号
        dialog.singal_tipsPrint.connect(self.app_print)

        # 显示对话框
        dialog.show()
    
    # 配置 关于对话框 
    @Slot()
    def dialogCfg_dialog_about(self) :
        # 创建对话框
        dialog = Dialog_about()
        # 对话框信号连接
        
        # 显示对话框
        dialog.exec()

    # 配置 dbc 解析对话框 
    @Slot()
    def dialogCfg_dialog_dbcDecode(self) :
        # 创建对话框
        list_dbName = ["dbcDataDB"]  
        dialog = Dialog_querySniffDB(list_dbName=list_dbName, mainWin=self, parent=self)
        dialog.ui.pushButton_dbcDecode.setVisible(True)
        # 对话框信号属性设置

        # 对话框信号连接
        dialog.singal_tipsPrint.connect(self.app_print)
        dialog.on_pushButton_dbcDecode_clicked() # 弹出 dbc 解析
        # 显示对话框
        dialog.exec()

    # 清空输出窗口打印的消息
    @Slot()
    def on_pushButton_clearAppPrint_clicked(self):
        self.ui.textBrowser_appPrint.clear()

    # 弹出提示信息对话框
    @Slot(str)
    def info_dialog_slot(self, info_str):
        QMessageBox.information(None, "information", info_str)

    # 往界面的输出窗口打印提示信息槽函数
    @Slot(str)
    def app_print(self, tipsString):
        outString = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "  " + tipsString
        self.ui.textBrowser_appPrint.append(outString)

    # 创建并显示进度条对话框
    @Slot(dict)
    def info_processStatus_start_slot(self, dict_info):
        # 进度条对话框标识
        self.progress_dialog_name = dict_info["name"]
        # 创建进度条对话框
        self.progress_dialog = QProgressDialog()
        self.progress_dialog.setWindowTitle("Progress")
        self.progress_dialog.setLabelText(dict_info["tips"])
        self.progress_dialog.setCancelButtonText("Cancel")
        self.progress_dialog.setRange(0, 100)
        self.progress_dialog.setModal(True)  # 设置为模态对话框

        # 信号连接
        self.progress_dialog.canceled.connect(lambda : (
            dict_info["threadObj_cancelFunc"]()  # 限于pyside6 不支持中断的信号连接方式使用了这种写法，这种调用要注意线程间数据访问的互斥
        ))

        # 显示对话框
        self.progress_dialog.exec()

    # 更新进度条对话框的进度
    @Slot(int)
    def info_processStatus_updateValue_slot(self, value):
        if self.progress_dialog is not None:
            if value > 100:
                self.progress_dialog.setValue(100)
            else:
                self.progress_dialog.setValue(value)
                if value == 100:
                    # 弹出消息对话框
                    QMessageBox.information(None, "information", f"{self.progress_dialog_name} has been completed!")
    
    # 连接设备信号
    signal_device_connect = Signal()

    # 断开设备连接信号
    signal_device_disconnect = Signal()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwinow = MainWindow()
    mainwinow.show()
    sys.exit(app.exec())

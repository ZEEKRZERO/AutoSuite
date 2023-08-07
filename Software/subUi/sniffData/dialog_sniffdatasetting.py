# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass


from PySide6 import QtWidgets
from PySide6.QtCore import Signal, Slot, Qt

from subUi.sniffData.ui_dialog_sniffdatasetting import Ui_Dialog_sniffDataSetting

from app.app_utilities import AppUtilitiesClass


class Dialog_sniffDataSetting(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Dialog_sniffDataSetting()
        self.ui.setupUi(self)

        # 默认 抓取数据配置参数
        self.cfgParam_sniffData_dict = {
            # 字段选择
            "key_selection" : {
                "key_ch" : True,
                "key_receiveTime" : True,
                "key_busType" : True,
                "key_frameID" : True,
                "key_frameType" : True,
                "key_dataLen" : True,
                "key_data" : True,
                "key_timestamp" : True,
            },
            # 滤波配置
            "filter_cfg" : {
                "isEnableFilter" : False,
                "filter_IDMask" : "",
                "filter_tarID" : "",
                "filter_dataMask" : "",
                "filter_tarData" : "",
                "filter_relation_idWithData" : "and",
            }
        }
        # 信号连接
        self.ui.checkBox_key_all.stateChanged.connect(self.on_checkBox_key_all_stateChanged)
        self.ui.tabWidget.currentChanged.connect(lambda arg:(
            self.param_load_slot()
        ))
        self.ui.pushButton_ok.clicked.connect(self.param_save_slot)
        self.ui.pushButton_cancel.clicked.connect(lambda : (
            self.reject() # 退出对话框
        ))

        self.param_load_slot()
        

    # 加载并显示参数
    @Slot()
    def param_load_slot(self) :
        
        # 从配置文件加载配置参数
        self.cfgParam_sniffData_dict = AppUtilitiesClass.cfgParam_sniffData_load()

        # 刷新显示配置参数
        if self.ui.tabWidget.currentIndex() == 0 :
            self.ui.checkBox_key_channel.setChecked(self.cfgParam_sniffData_dict["key_selection"]["key_ch"])
            self.ui.checkBox_key_resTime.setChecked(self.cfgParam_sniffData_dict["key_selection"]["key_receiveTime"])
            self.ui.checkBox_key_busType.setChecked(self.cfgParam_sniffData_dict["key_selection"]["key_busType"])
            self.ui.checkBox_key_frameID.setChecked(self.cfgParam_sniffData_dict["key_selection"]["key_frameID"])
            self.ui.checkBox_key_frameType.setChecked(self.cfgParam_sniffData_dict["key_selection"]["key_frameType"])
            self.ui.checkBox_key_dataLen.setChecked(self.cfgParam_sniffData_dict["key_selection"]["key_dataLen"])
            self.ui.checkBox_key_data.setChecked(self.cfgParam_sniffData_dict["key_selection"]["key_data"])
            self.ui.checkBox_key_timestamp.setChecked(self.cfgParam_sniffData_dict["key_selection"]["key_timestamp"])
            if (self.cfgParam_sniffData_dict["key_selection"]["key_ch"] and self.cfgParam_sniffData_dict["key_selection"]["key_receiveTime"]
                and self.cfgParam_sniffData_dict["key_selection"]["key_busType"] and self.cfgParam_sniffData_dict["key_selection"]["key_frameID"]
                and self.cfgParam_sniffData_dict["key_selection"]["key_frameType"] and self.cfgParam_sniffData_dict["key_selection"]["key_dataLen"]
                and self.cfgParam_sniffData_dict["key_selection"]["key_data"] and self.cfgParam_sniffData_dict["key_selection"]["key_timestamp"]):
                self.ui.checkBox_key_all.setChecked(True)
            else:
                self.ui.checkBox_key_all.setChecked(False)
        elif self.ui.tabWidget.currentIndex() == 1 :
            self.ui.checkBox_isEnableFilter.setChecked(self.cfgParam_sniffData_dict["filter_cfg"]["isEnableFilter"])
            self.ui.lineEdit_idmask.setText(self.cfgParam_sniffData_dict["filter_cfg"]["filter_IDMask"])
            self.ui.lineEdit_tarId.setText(self.cfgParam_sniffData_dict["filter_cfg"]["filter_tarID"])
            self.ui.lineEdit_datamask.setText(self.cfgParam_sniffData_dict["filter_cfg"]["filter_dataMask"])
            self.ui.lineEdit_tardata.setText(self.cfgParam_sniffData_dict["filter_cfg"]["filter_tarData"])
            if self.cfgParam_sniffData_dict["filter_cfg"]["filter_relation_idWithData"] == "and" :
                self.ui.radioButton_and.setChecked(True)
            else:
                self.ui.radioButton_or.setChecked(True)

    # 保存修改的参数
    @Slot()
    def param_save_slot(self) :
        # 从配置文件加载配置参数
        param = AppUtilitiesClass.cfgParam_sniffData_load()

        # 读取界面修改后的参数
        if self.ui.tabWidget.currentIndex() == 0 :
            param["key_selection"]["key_ch"] = self.ui.checkBox_key_channel.isChecked()
            param["key_selection"]["key_receiveTime"] = self.ui.checkBox_key_resTime.isChecked()
            param["key_selection"]["key_busType"] = self.ui.checkBox_key_busType.isChecked()
            param["key_selection"]["key_frameID"] = self.ui.checkBox_key_frameID.isChecked()
            param["key_selection"]["key_frameType"] = self.ui.checkBox_key_frameType.isChecked()
            param["key_selection"]["key_dataLen"] = self.ui.checkBox_key_dataLen.isChecked()
            param["key_selection"]["key_data"] = self.ui.checkBox_key_data.isChecked()
            param["key_selection"]["key_timestamp"] = self.ui.checkBox_key_timestamp.isChecked()

        elif self.ui.tabWidget.currentIndex() == 1 :
            param["filter_cfg"]["isEnableFilter"] = self.ui.checkBox_isEnableFilter.isChecked()
            param["filter_cfg"]["filter_IDMask"] = self.ui.lineEdit_idmask.text()
            param["filter_cfg"]["filter_tarID"] = self.ui.lineEdit_tarId.text()
            param["filter_cfg"]["filter_dataMask"] = self.ui.lineEdit_datamask.text()
            param["filter_cfg"]["filter_tarData"] = self.ui.lineEdit_tardata.text()

            if self.ui.radioButton_and.isChecked() :
                param["filter_cfg"]["filter_relation_idWithData"] = "and"
            else :
                param["filter_cfg"]["filter_relation_idWithData"] = "or"

        # 保存参数到文件
        AppUtilitiesClass.cfgParam_sniffData_save(param)

        # 退出对话框
        self.accept()

    @Slot(int)
    def on_checkBox_key_all_stateChanged(self, arg):
        if self.ui.checkBox_key_all.isChecked() :
            self.ui.checkBox_key_channel.setChecked(True)
            self.ui.checkBox_key_resTime.setChecked(True)
            self.ui.checkBox_key_busType.setChecked(True)
            self.ui.checkBox_key_frameID.setChecked(True)
            self.ui.checkBox_key_frameType.setChecked(True)
            self.ui.checkBox_key_dataLen.setChecked(True)
            self.ui.checkBox_key_data.setChecked(True)
            self.ui.checkBox_key_timestamp.setChecked(True)
        else:
            self.ui.checkBox_key_channel.setChecked(False)
            self.ui.checkBox_key_resTime.setChecked(False)
            self.ui.checkBox_key_busType.setChecked(False)
            self.ui.checkBox_key_frameID.setChecked(False)
            self.ui.checkBox_key_frameType.setChecked(False)
            self.ui.checkBox_key_dataLen.setChecked(False)
            self.ui.checkBox_key_data.setChecked(False)
            self.ui.checkBox_key_timestamp.setChecked(False)
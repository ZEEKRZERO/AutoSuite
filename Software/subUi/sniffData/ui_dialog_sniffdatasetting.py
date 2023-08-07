# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_sniffdatasetting.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QTabWidget, QVBoxLayout, QWidget)
import rc_resource

class Ui_Dialog_sniffDataSetting(object):
    def setupUi(self, Dialog_sniffDataSetting):
        if not Dialog_sniffDataSetting.objectName():
            Dialog_sniffDataSetting.setObjectName(u"Dialog_sniffDataSetting")
        Dialog_sniffDataSetting.resize(371, 328)
        icon = QIcon()
        icon.addFile(u":/icons/setting.svg", QSize(), QIcon.Normal, QIcon.Off)
        Dialog_sniffDataSetting.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Dialog_sniffDataSetting)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_ok = QPushButton(Dialog_sniffDataSetting)
        self.pushButton_ok.setObjectName(u"pushButton_ok")

        self.horizontalLayout.addWidget(self.pushButton_ok)

        self.pushButton_cancel = QPushButton(Dialog_sniffDataSetting)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")

        self.horizontalLayout.addWidget(self.pushButton_cancel)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.tabWidget = QTabWidget(Dialog_sniffDataSetting)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_3 = QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.checkBox_key_all = QCheckBox(self.groupBox)
        self.checkBox_key_all.setObjectName(u"checkBox_key_all")
        font = QFont()
        font.setPointSize(12)
        self.checkBox_key_all.setFont(font)

        self.horizontalLayout_4.addWidget(self.checkBox_key_all)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkBox_key_channel = QCheckBox(self.groupBox)
        self.checkBox_key_channel.setObjectName(u"checkBox_key_channel")
        self.checkBox_key_channel.setFont(font)

        self.horizontalLayout_2.addWidget(self.checkBox_key_channel)

        self.checkBox_key_resTime = QCheckBox(self.groupBox)
        self.checkBox_key_resTime.setObjectName(u"checkBox_key_resTime")
        self.checkBox_key_resTime.setFont(font)

        self.horizontalLayout_2.addWidget(self.checkBox_key_resTime)

        self.checkBox_key_busType = QCheckBox(self.groupBox)
        self.checkBox_key_busType.setObjectName(u"checkBox_key_busType")
        self.checkBox_key_busType.setFont(font)

        self.horizontalLayout_2.addWidget(self.checkBox_key_busType)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.checkBox_key_frameID = QCheckBox(self.groupBox)
        self.checkBox_key_frameID.setObjectName(u"checkBox_key_frameID")
        self.checkBox_key_frameID.setFont(font)

        self.horizontalLayout_3.addWidget(self.checkBox_key_frameID)

        self.checkBox_key_frameType = QCheckBox(self.groupBox)
        self.checkBox_key_frameType.setObjectName(u"checkBox_key_frameType")
        self.checkBox_key_frameType.setFont(font)

        self.horizontalLayout_3.addWidget(self.checkBox_key_frameType)

        self.checkBox_key_dataLen = QCheckBox(self.groupBox)
        self.checkBox_key_dataLen.setObjectName(u"checkBox_key_dataLen")
        self.checkBox_key_dataLen.setFont(font)

        self.horizontalLayout_3.addWidget(self.checkBox_key_dataLen)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.checkBox_key_data = QCheckBox(self.groupBox)
        self.checkBox_key_data.setObjectName(u"checkBox_key_data")
        self.checkBox_key_data.setFont(font)

        self.horizontalLayout_5.addWidget(self.checkBox_key_data)

        self.checkBox_key_timestamp = QCheckBox(self.groupBox)
        self.checkBox_key_timestamp.setObjectName(u"checkBox_key_timestamp")
        self.checkBox_key_timestamp.setFont(font)

        self.horizontalLayout_5.addWidget(self.checkBox_key_timestamp)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_6 = QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.groupBox_2 = QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout_7.addWidget(self.label)

        self.lineEdit_idmask = QLineEdit(self.groupBox_2)
        self.lineEdit_idmask.setObjectName(u"lineEdit_idmask")

        self.horizontalLayout_7.addWidget(self.lineEdit_idmask)


        self.gridLayout_4.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout_10.addWidget(self.label_4)

        self.lineEdit_tarId = QLineEdit(self.groupBox_2)
        self.lineEdit_tarId.setObjectName(u"lineEdit_tarId")

        self.horizontalLayout_10.addWidget(self.lineEdit_tarId)


        self.gridLayout_4.addLayout(self.horizontalLayout_10, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.radioButton_and = QRadioButton(self.tab_2)
        self.radioButton_and.setObjectName(u"radioButton_and")

        self.horizontalLayout_12.addWidget(self.radioButton_and)

        self.radioButton_or = QRadioButton(self.tab_2)
        self.radioButton_or.setObjectName(u"radioButton_or")

        self.horizontalLayout_12.addWidget(self.radioButton_or)


        self.gridLayout_6.addLayout(self.horizontalLayout_12, 2, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_5 = QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_2)

        self.lineEdit_datamask = QLineEdit(self.groupBox_3)
        self.lineEdit_datamask.setObjectName(u"lineEdit_datamask")

        self.horizontalLayout_8.addWidget(self.lineEdit_datamask)


        self.gridLayout_5.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.horizontalLayout_11.addWidget(self.label_5)

        self.lineEdit_tardata = QLineEdit(self.groupBox_3)
        self.lineEdit_tardata.setObjectName(u"lineEdit_tardata")

        self.horizontalLayout_11.addWidget(self.lineEdit_tardata)


        self.gridLayout_5.addLayout(self.horizontalLayout_11, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_3, 3, 0, 1, 1)

        self.checkBox_isEnableFilter = QCheckBox(self.tab_2)
        self.checkBox_isEnableFilter.setObjectName(u"checkBox_isEnableFilter")
        font1 = QFont()
        font1.setPointSize(9)
        self.checkBox_isEnableFilter.setFont(font1)

        self.gridLayout_6.addWidget(self.checkBox_isEnableFilter, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(Dialog_sniffDataSetting)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog_sniffDataSetting)
    # setupUi

    def retranslateUi(self, Dialog_sniffDataSetting):
        Dialog_sniffDataSetting.setWindowTitle(QCoreApplication.translate("Dialog_sniffDataSetting", u"sniff Settings", None))
        self.pushButton_ok.setText(QCoreApplication.translate("Dialog_sniffDataSetting", u"OK", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("Dialog_sniffDataSetting", u"Cancel", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog_sniffDataSetting", u"Field", None))
        self.checkBox_key_all.setText(QCoreApplication.translate("Dialog_sniffDataSetting", u"ALL", None))
        self.checkBox_key_channel.setText(QCoreApplication.translate("Dialog_sniffDataSetting", u"Channel", None))
        self.checkBox_key_resTime.setText(QCoreApplication.translate("Dialog_sniffDataSetting", u"Receive time", None))
        self.checkBox_key_busType.setText(QCoreApplication.translate("Dialog_sniffDataSetting", u"Bus type", None))
        self.checkBox_key_frameID.setText(QCoreApplication.translate("Dialog_sniffDataSetting", u"Frame ID", None))
        self.checkBox_key_frameType.setText(QCoreApplication.translate("Dialog_sniffDataSetting", u"Frame type", None))
        self.checkBox_key_dataLen.setText(QCoreApplication.translate("Dialog_sniffDataSetting", u"Length", None))
        self.checkBox_key_data.setText(QCoreApplication.translate("Dialog_sniffDataSetting", u"Data", None))
        self.checkBox_key_timestamp.setText(QCoreApplication.translate("Dialog_sniffDataSetting", u"Timestamp", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog_sniffDataSetting", u"Sniff field", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog_sniffDataSetting", u"ID\u8fc7\u6ee4", None))
        self.label.setText(QCoreApplication.translate("Dialog_sniffDataSetting", u"ID\u63a9\u7801", None))
        self.label_4.setText(QCoreApplication.translate("Dialog_sniffDataSetting", u"\u76ee\u6807ID", None))
        self.radioButton_and.setText(QCoreApplication.translate("Dialog_sniffDataSetting", u"\u4e0e", None))
        self.radioButton_or.setText(QCoreApplication.translate("Dialog_sniffDataSetting", u"\u6216", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog_sniffDataSetting", u"\u6570\u636e\u8fc7\u6ee4", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_sniffDataSetting", u"\u6570\u636e\u63a9\u7801", None))
        self.label_5.setText(QCoreApplication.translate("Dialog_sniffDataSetting", u"\u76ee\u6807\u6570\u636e", None))
        self.checkBox_isEnableFilter.setText(QCoreApplication.translate("Dialog_sniffDataSetting", u"\u542f\u7528\u8fc7\u6ee4\u5668", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog_sniffDataSetting", u"Filter", None))
    # retranslateUi


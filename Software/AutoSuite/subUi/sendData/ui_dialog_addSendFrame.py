# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_addSendFrame.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTextBrowser, QVBoxLayout, QWidget)
import rc_resource

class Ui_Dialog_addSendFrame(object):
    def setupUi(self, Dialog_addSendFrame):
        if not Dialog_addSendFrame.objectName():
            Dialog_addSendFrame.setObjectName(u"Dialog_addSendFrame")
        Dialog_addSendFrame.resize(455, 243)
        icon = QIcon()
        icon.addFile(u":/icons/zeekr.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog_addSendFrame.setWindowIcon(icon)
        self.gridLayout_6 = QGridLayout(Dialog_addSendFrame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_2 = QGroupBox(Dialog_addSendFrame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.comboBox_busType = QComboBox(self.groupBox_2)
        self.comboBox_busType.setObjectName(u"comboBox_busType")

        self.gridLayout_2.addWidget(self.comboBox_busType, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.gridLayout_6.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.groupBox = QGroupBox(Dialog_addSendFrame)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget_main = QStackedWidget(self.groupBox)
        self.stackedWidget_main.setObjectName(u"stackedWidget_main")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_4 = QGridLayout(self.page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.page)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.lineEdit_can_channel = QLineEdit(self.page)
        self.lineEdit_can_channel.setObjectName(u"lineEdit_can_channel")

        self.horizontalLayout_6.addWidget(self.lineEdit_can_channel)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.page)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.lineEdit_can_frameID = QLineEdit(self.page)
        self.lineEdit_can_frameID.setObjectName(u"lineEdit_can_frameID")

        self.horizontalLayout_7.addWidget(self.lineEdit_can_frameID)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.page)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_8.addWidget(self.label_7)

        self.lineEdit_can_length = QLineEdit(self.page)
        self.lineEdit_can_length.setObjectName(u"lineEdit_can_length")

        self.horizontalLayout_8.addWidget(self.lineEdit_can_length)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.page)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_9.addWidget(self.label_8)

        self.lineEdit_can_data = QLineEdit(self.page)
        self.lineEdit_can_data.setObjectName(u"lineEdit_can_data")

        self.horizontalLayout_9.addWidget(self.lineEdit_can_data)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)


        self.gridLayout_4.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.stackedWidget_main.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_3 = QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_9 = QLabel(self.page_2)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_10.addWidget(self.label_9)

        self.lineEdit_flexRay_channel = QLineEdit(self.page_2)
        self.lineEdit_flexRay_channel.setObjectName(u"lineEdit_flexRay_channel")

        self.horizontalLayout_10.addWidget(self.lineEdit_flexRay_channel)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_10 = QLabel(self.page_2)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_11.addWidget(self.label_10)

        self.lineEdit_flexRay_frameID = QLineEdit(self.page_2)
        self.lineEdit_flexRay_frameID.setObjectName(u"lineEdit_flexRay_frameID")

        self.horizontalLayout_11.addWidget(self.lineEdit_flexRay_frameID)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_11 = QLabel(self.page_2)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_12.addWidget(self.label_11)

        self.lineEdit_flexRay_length = QLineEdit(self.page_2)
        self.lineEdit_flexRay_length.setObjectName(u"lineEdit_flexRay_length")

        self.horizontalLayout_12.addWidget(self.lineEdit_flexRay_length)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_12 = QLabel(self.page_2)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_13.addWidget(self.label_12)

        self.lineEdit_flexRay_data = QLineEdit(self.page_2)
        self.lineEdit_flexRay_data.setObjectName(u"lineEdit_flexRay_data")
        self.lineEdit_flexRay_data.setMaxLength(128)

        self.horizontalLayout_13.addWidget(self.lineEdit_flexRay_data)


        self.verticalLayout_4.addLayout(self.horizontalLayout_13)


        self.gridLayout_3.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.stackedWidget_main.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_5 = QGridLayout(self.page_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_14 = QLabel(self.page_3)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_15.addWidget(self.label_14)

        self.lineEdit_lin_channel = QLineEdit(self.page_3)
        self.lineEdit_lin_channel.setObjectName(u"lineEdit_lin_channel")

        self.horizontalLayout_15.addWidget(self.lineEdit_lin_channel)


        self.verticalLayout_5.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_15 = QLabel(self.page_3)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_16.addWidget(self.label_15)

        self.lineEdit_lin_frameID = QLineEdit(self.page_3)
        self.lineEdit_lin_frameID.setObjectName(u"lineEdit_lin_frameID")

        self.horizontalLayout_16.addWidget(self.lineEdit_lin_frameID)


        self.verticalLayout_5.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_16 = QLabel(self.page_3)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_17.addWidget(self.label_16)

        self.lineEdit_lin_length = QLineEdit(self.page_3)
        self.lineEdit_lin_length.setObjectName(u"lineEdit_lin_length")

        self.horizontalLayout_17.addWidget(self.lineEdit_lin_length)


        self.verticalLayout_5.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_17 = QLabel(self.page_3)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_18.addWidget(self.label_17)

        self.lineEdit_lin_data = QLineEdit(self.page_3)
        self.lineEdit_lin_data.setObjectName(u"lineEdit_lin_data")

        self.horizontalLayout_18.addWidget(self.lineEdit_lin_data)


        self.verticalLayout_5.addLayout(self.horizontalLayout_18)


        self.gridLayout_5.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.stackedWidget_main.addWidget(self.page_3)
        self.ethernet = QWidget()
        self.ethernet.setObjectName(u"ethernet")
        self.gridLayout_7 = QGridLayout(self.ethernet)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.textBrowser = QTextBrowser(self.ethernet)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setReadOnly(False)

        self.gridLayout_7.addWidget(self.textBrowser, 0, 0, 1, 1)

        self.stackedWidget_main.addWidget(self.ethernet)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_8 = QGridLayout(self.page_4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_13 = QLabel(self.page_4)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_14.addWidget(self.label_13)

        self.lineEdit_canFD_channel = QLineEdit(self.page_4)
        self.lineEdit_canFD_channel.setObjectName(u"lineEdit_canFD_channel")

        self.horizontalLayout_14.addWidget(self.lineEdit_canFD_channel)


        self.verticalLayout_6.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_18 = QLabel(self.page_4)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_19.addWidget(self.label_18)

        self.lineEdit_canFD_frameID = QLineEdit(self.page_4)
        self.lineEdit_canFD_frameID.setObjectName(u"lineEdit_canFD_frameID")

        self.horizontalLayout_19.addWidget(self.lineEdit_canFD_frameID)


        self.verticalLayout_6.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_19 = QLabel(self.page_4)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_20.addWidget(self.label_19)

        self.lineEdit_canFD_length = QLineEdit(self.page_4)
        self.lineEdit_canFD_length.setObjectName(u"lineEdit_canFD_length")

        self.horizontalLayout_20.addWidget(self.lineEdit_canFD_length)


        self.verticalLayout_6.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_20 = QLabel(self.page_4)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_21.addWidget(self.label_20)

        self.lineEdit_canFD_data = QLineEdit(self.page_4)
        self.lineEdit_canFD_data.setObjectName(u"lineEdit_canFD_data")
        self.lineEdit_canFD_data.setMaxLength(128)

        self.horizontalLayout_21.addWidget(self.lineEdit_canFD_data)


        self.verticalLayout_6.addLayout(self.horizontalLayout_21)


        self.gridLayout_8.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        self.stackedWidget_main.addWidget(self.page_4)

        self.gridLayout.addWidget(self.stackedWidget_main, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox, 0, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.pushButton_cancel = QPushButton(Dialog_addSendFrame)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")

        self.horizontalLayout_5.addWidget(self.pushButton_cancel)

        self.pushButton_ok = QPushButton(Dialog_addSendFrame)
        self.pushButton_ok.setObjectName(u"pushButton_ok")

        self.horizontalLayout_5.addWidget(self.pushButton_ok)


        self.gridLayout_6.addLayout(self.horizontalLayout_5, 1, 0, 1, 2)


        self.retranslateUi(Dialog_addSendFrame)

        self.stackedWidget_main.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(Dialog_addSendFrame)
    # setupUi

    def retranslateUi(self, Dialog_addSendFrame):
        Dialog_addSendFrame.setWindowTitle(QCoreApplication.translate("Dialog_addSendFrame", u"Add Send Frame", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog_addSendFrame", u"BusType", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog_addSendFrame", u"parameter", None))
        self.label_5.setText(QCoreApplication.translate("Dialog_addSendFrame", u"Channel  ", None))
        self.lineEdit_can_channel.setInputMask(QCoreApplication.translate("Dialog_addSendFrame", u"0", None))
        self.lineEdit_can_channel.setText(QCoreApplication.translate("Dialog_addSendFrame", u"1", None))
        self.label_6.setText(QCoreApplication.translate("Dialog_addSendFrame", u"Frame ID", None))
        self.lineEdit_can_frameID.setInputMask(QCoreApplication.translate("Dialog_addSendFrame", u"HHHHHHHH", None))
        self.lineEdit_can_frameID.setText(QCoreApplication.translate("Dialog_addSendFrame", u"123", None))
        self.label_7.setText(QCoreApplication.translate("Dialog_addSendFrame", u"Length    ", None))
        self.lineEdit_can_length.setInputMask(QCoreApplication.translate("Dialog_addSendFrame", u"00", None))
        self.lineEdit_can_length.setText(QCoreApplication.translate("Dialog_addSendFrame", u"8", None))
        self.label_8.setText(QCoreApplication.translate("Dialog_addSendFrame", u"Data       ", None))
        self.lineEdit_can_data.setInputMask(QCoreApplication.translate("Dialog_addSendFrame", u"HHHHHHHHHHHHHHHH", None))
        self.lineEdit_can_data.setText(QCoreApplication.translate("Dialog_addSendFrame", u"FFFFFFFFFFFFFFFF", None))
        self.label_9.setText(QCoreApplication.translate("Dialog_addSendFrame", u"Channel  ", None))
        self.lineEdit_flexRay_channel.setInputMask(QCoreApplication.translate("Dialog_addSendFrame", u"0", None))
        self.lineEdit_flexRay_channel.setText(QCoreApplication.translate("Dialog_addSendFrame", u"1", None))
        self.label_10.setText(QCoreApplication.translate("Dialog_addSendFrame", u"Frame ID", None))
        self.lineEdit_flexRay_frameID.setInputMask(QCoreApplication.translate("Dialog_addSendFrame", u"HH", None))
        self.lineEdit_flexRay_frameID.setText(QCoreApplication.translate("Dialog_addSendFrame", u"1", None))
        self.label_11.setText(QCoreApplication.translate("Dialog_addSendFrame", u"Length    ", None))
        self.lineEdit_flexRay_length.setInputMask(QCoreApplication.translate("Dialog_addSendFrame", u"00", None))
        self.lineEdit_flexRay_length.setText(QCoreApplication.translate("Dialog_addSendFrame", u"64", None))
        self.label_12.setText(QCoreApplication.translate("Dialog_addSendFrame", u"Data       ", None))
        self.lineEdit_flexRay_data.setInputMask(QCoreApplication.translate("Dialog_addSendFrame", u"HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH", None))
        self.lineEdit_flexRay_data.setText(QCoreApplication.translate("Dialog_addSendFrame", u"FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF", None))
        self.label_14.setText(QCoreApplication.translate("Dialog_addSendFrame", u"Channel  ", None))
        self.label_15.setText(QCoreApplication.translate("Dialog_addSendFrame", u"Frame ID", None))
        self.label_16.setText(QCoreApplication.translate("Dialog_addSendFrame", u"Length    ", None))
        self.label_17.setText(QCoreApplication.translate("Dialog_addSendFrame", u"Data       ", None))
        self.label_13.setText(QCoreApplication.translate("Dialog_addSendFrame", u"Channel  ", None))
        self.lineEdit_canFD_channel.setInputMask(QCoreApplication.translate("Dialog_addSendFrame", u"0", None))
        self.lineEdit_canFD_channel.setText(QCoreApplication.translate("Dialog_addSendFrame", u"1", None))
        self.label_18.setText(QCoreApplication.translate("Dialog_addSendFrame", u"Frame ID", None))
        self.lineEdit_canFD_frameID.setInputMask(QCoreApplication.translate("Dialog_addSendFrame", u"HH", None))
        self.lineEdit_canFD_frameID.setText(QCoreApplication.translate("Dialog_addSendFrame", u"1", None))
        self.label_19.setText(QCoreApplication.translate("Dialog_addSendFrame", u"Length    ", None))
        self.lineEdit_canFD_length.setInputMask(QCoreApplication.translate("Dialog_addSendFrame", u"00", None))
        self.lineEdit_canFD_length.setText(QCoreApplication.translate("Dialog_addSendFrame", u"64", None))
        self.label_20.setText(QCoreApplication.translate("Dialog_addSendFrame", u"Data       ", None))
        self.lineEdit_canFD_data.setInputMask(QCoreApplication.translate("Dialog_addSendFrame", u"HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH", None))
        self.lineEdit_canFD_data.setText(QCoreApplication.translate("Dialog_addSendFrame", u"FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("Dialog_addSendFrame", u"cancel", None))
        self.pushButton_ok.setText(QCoreApplication.translate("Dialog_addSendFrame", u"ok", None))
    # retranslateUi


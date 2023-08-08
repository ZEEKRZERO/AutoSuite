# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_connectparamset.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import rc_resource

class Ui_Dialog_connectParamSet(object):
    def setupUi(self, Dialog_connectParamSet):
        if not Dialog_connectParamSet.objectName():
            Dialog_connectParamSet.setObjectName(u"Dialog_connectParamSet")
        Dialog_connectParamSet.resize(481, 424)
        icon = QIcon()
        icon.addFile(u":/icons/ConnectParamSet.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog_connectParamSet.setWindowIcon(icon)
        self.gridLayout_12 = QGridLayout(Dialog_connectParamSet)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.groupBox_6 = QGroupBox(Dialog_connectParamSet)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_10 = QGridLayout(self.groupBox_6)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.groupBox_6)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.comboBox_connectMode = QComboBox(self.groupBox)
        self.comboBox_connectMode.setObjectName(u"comboBox_connectMode")
        self.comboBox_connectMode.setMinimumSize(QSize(80, 20))

        self.gridLayout.addWidget(self.comboBox_connectMode, 0, 0, 1, 1)

        self.pushButton_reflsh_com = QPushButton(self.groupBox)
        self.pushButton_reflsh_com.setObjectName(u"pushButton_reflsh_com")

        self.gridLayout.addWidget(self.pushButton_reflsh_com, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_13.addLayout(self.verticalLayout_2)

        self.groupBox_2 = QGroupBox(self.groupBox_6)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget = QStackedWidget(self.groupBox_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_5 = QGridLayout(self.page)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(Qt.PlainText)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.comboBox_uartBuadRate = QComboBox(self.page)
        self.comboBox_uartBuadRate.setObjectName(u"comboBox_uartBuadRate")

        self.horizontalLayout_2.addWidget(self.comboBox_uartBuadRate)


        self.gridLayout_5.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_6 = QLabel(self.page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setTextFormat(Qt.PlainText)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_6)

        self.comboBox_uartStopBits = QComboBox(self.page)
        self.comboBox_uartStopBits.setObjectName(u"comboBox_uartStopBits")

        self.horizontalLayout_8.addWidget(self.comboBox_uartStopBits)


        self.gridLayout_5.addLayout(self.horizontalLayout_8, 2, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setTextFormat(Qt.PlainText)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.comboBox_uartDataBits = QComboBox(self.page)
        self.comboBox_uartDataBits.setObjectName(u"comboBox_uartDataBits")

        self.horizontalLayout_6.addWidget(self.comboBox_uartDataBits)


        self.gridLayout_5.addLayout(self.horizontalLayout_6, 3, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setTextFormat(Qt.PlainText)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_5)

        self.comboBox_uartCheakBits = QComboBox(self.page)
        self.comboBox_uartCheakBits.setObjectName(u"comboBox_uartCheakBits")

        self.horizontalLayout_7.addWidget(self.comboBox_uartCheakBits)


        self.gridLayout_5.addLayout(self.horizontalLayout_7, 4, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setTextFormat(Qt.PlainText)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.comboBox_uartPort = QComboBox(self.page)
        self.comboBox_uartPort.setObjectName(u"comboBox_uartPort")
        self.comboBox_uartPort.setMinimumSize(QSize(80, 20))

        self.horizontalLayout.addWidget(self.comboBox_uartPort)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)


        self.gridLayout_5.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_3 = QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 20))
        self.label_3.setFont(font)
        self.label_3.setTextFormat(Qt.PlainText)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_3)

        self.lineEdit_IPAddr = QLineEdit(self.page_2)
        self.lineEdit_IPAddr.setObjectName(u"lineEdit_IPAddr")
        self.lineEdit_IPAddr.setMinimumSize(QSize(200, 0))
        self.lineEdit_IPAddr.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_9.addWidget(self.lineEdit_IPAddr)


        self.gridLayout_3.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.label_47 = QLabel(self.page_2)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMaximumSize(QSize(16777215, 20))
        self.label_47.setFont(font)
        self.label_47.setTextFormat(Qt.PlainText)
        self.label_47.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_53.addWidget(self.label_47)

        self.lineEdit_IPPort = QLineEdit(self.page_2)
        self.lineEdit_IPPort.setObjectName(u"lineEdit_IPPort")
        self.lineEdit_IPPort.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_53.addWidget(self.lineEdit_IPPort)


        self.gridLayout_3.addLayout(self.horizontalLayout_53, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_4 = QGridLayout(self.page_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_7 = QLabel(self.page_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 20))
        self.label_7.setFont(font)
        self.label_7.setTextFormat(Qt.PlainText)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_7)

        self.lineEdit_VID = QLineEdit(self.page_3)
        self.lineEdit_VID.setObjectName(u"lineEdit_VID")

        self.horizontalLayout_4.addWidget(self.lineEdit_VID)


        self.gridLayout_4.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(self.page_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 20))
        self.label_8.setFont(font)
        self.label_8.setTextFormat(Qt.PlainText)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_8)

        self.lineEdit_PID = QLineEdit(self.page_3)
        self.lineEdit_PID.setObjectName(u"lineEdit_PID")

        self.horizontalLayout_5.addWidget(self.lineEdit_PID)


        self.gridLayout_4.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.horizontalLayout_13.addWidget(self.groupBox_2)


        self.gridLayout_10.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.groupBox_6, 0, 0, 1, 1)

        self.groupBox_7 = QGroupBox(Dialog_connectParamSet)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_11 = QGridLayout(self.groupBox_7)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.groupBox_4 = QGroupBox(self.groupBox_7)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_8 = QGridLayout(self.groupBox_4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_11.addWidget(self.label_9)

        self.comboBox_cfgFile = QComboBox(self.groupBox_4)
        self.comboBox_cfgFile.setObjectName(u"comboBox_cfgFile")
        self.comboBox_cfgFile.setMinimumSize(QSize(120, 20))

        self.horizontalLayout_11.addWidget(self.comboBox_cfgFile)

        self.pushButton_newNode = QPushButton(self.groupBox_4)
        self.pushButton_newNode.setObjectName(u"pushButton_newNode")

        self.horizontalLayout_11.addWidget(self.pushButton_newNode)


        self.gridLayout_8.addLayout(self.horizontalLayout_11, 0, 0, 1, 1)


        self.horizontalLayout_14.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.groupBox_7)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_7 = QGridLayout(self.groupBox_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_10 = QLabel(self.groupBox_5)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_12.addWidget(self.label_10)

        self.comboBox_canCfg_spd = QComboBox(self.groupBox_5)
        self.comboBox_canCfg_spd.setObjectName(u"comboBox_canCfg_spd")
        self.comboBox_canCfg_spd.setMinimumSize(QSize(80, 20))

        self.horizontalLayout_12.addWidget(self.comboBox_canCfg_spd)


        self.gridLayout_7.addLayout(self.horizontalLayout_12, 0, 0, 1, 1)

        self.checkBox_canCfg_r120 = QCheckBox(self.groupBox_5)
        self.checkBox_canCfg_r120.setObjectName(u"checkBox_canCfg_r120")

        self.gridLayout_7.addWidget(self.checkBox_canCfg_r120, 1, 0, 1, 1)


        self.horizontalLayout_14.addWidget(self.groupBox_5)


        self.gridLayout_11.addLayout(self.horizontalLayout_14, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.groupBox_7, 1, 0, 1, 1)

        self.groupBox_3 = QGroupBox(Dialog_connectParamSet)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_6 = QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalSpacer = QSpacerItem(491, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.pushButton_cancel = QPushButton(self.groupBox_3)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")

        self.horizontalLayout_10.addWidget(self.pushButton_cancel)

        self.pushButton_ok = QPushButton(self.groupBox_3)
        self.pushButton_ok.setObjectName(u"pushButton_ok")

        self.horizontalLayout_10.addWidget(self.pushButton_ok)


        self.gridLayout_6.addLayout(self.horizontalLayout_10, 0, 1, 1, 1)


        self.gridLayout_12.addWidget(self.groupBox_3, 2, 0, 1, 1)


        self.retranslateUi(Dialog_connectParamSet)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Dialog_connectParamSet)
    # setupUi

    def retranslateUi(self, Dialog_connectParamSet):
        Dialog_connectParamSet.setWindowTitle(QCoreApplication.translate("Dialog_connectParamSet", u"Set device parameters", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Dialog_connectParamSet", u"Connection parameter", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog_connectParamSet", u"connection mode", None))
        self.pushButton_reflsh_com.setText(QCoreApplication.translate("Dialog_connectParamSet", u"Refresh", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog_connectParamSet", u"Parameters", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_connectParamSet", u"Baudrate", None))
        self.label_6.setText(QCoreApplication.translate("Dialog_connectParamSet", u"Stop bit", None))
        self.label_4.setText(QCoreApplication.translate("Dialog_connectParamSet", u"Data bit", None))
        self.label_5.setText(QCoreApplication.translate("Dialog_connectParamSet", u"Check bit", None))
        self.label.setText(QCoreApplication.translate("Dialog_connectParamSet", u"COM", None))
        self.label_3.setText(QCoreApplication.translate("Dialog_connectParamSet", u"IP ", None))
        self.label_47.setText(QCoreApplication.translate("Dialog_connectParamSet", u"Port", None))
        self.lineEdit_IPPort.setInputMask(QCoreApplication.translate("Dialog_connectParamSet", u"0000", None))
        self.label_7.setText(QCoreApplication.translate("Dialog_connectParamSet", u"VID", None))
        self.label_8.setText(QCoreApplication.translate("Dialog_connectParamSet", u"PID", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Dialog_connectParamSet", u"Bus parameter configuration", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog_connectParamSet", u"FlexRay configuration", None))
        self.label_9.setText(QCoreApplication.translate("Dialog_connectParamSet", u"Node", None))
        self.pushButton_newNode.setText(QCoreApplication.translate("Dialog_connectParamSet", u"new node", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Dialog_connectParamSet", u"CAN/CANFD configuration", None))
        self.label_10.setText(QCoreApplication.translate("Dialog_connectParamSet", u"Bus rate", None))
        self.checkBox_canCfg_r120.setText(QCoreApplication.translate("Dialog_connectParamSet", u"Terminal resistance", None))
        self.groupBox_3.setTitle("")
        self.pushButton_cancel.setText(QCoreApplication.translate("Dialog_connectParamSet", u"Cancel", None))
        self.pushButton_ok.setText(QCoreApplication.translate("Dialog_connectParamSet", u"OK", None))
    # retranslateUi


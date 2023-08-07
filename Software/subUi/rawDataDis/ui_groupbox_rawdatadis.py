# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'groupbox_rawdatadis.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QTextBrowser,
    QVBoxLayout, QWidget)
import rc_resource

class Ui_GroupBox_rawDataDis(object):
    def setupUi(self, GroupBox_rawDataDis):
        if not GroupBox_rawDataDis.objectName():
            GroupBox_rawDataDis.setObjectName(u"GroupBox_rawDataDis")
        GroupBox_rawDataDis.resize(619, 460)
        icon = QIcon()
        icon.addFile(u":/icons/basicData.svg", QSize(), QIcon.Normal, QIcon.Off)
        GroupBox_rawDataDis.setWindowIcon(icon)
        self.gridLayout_2 = QGridLayout(GroupBox_rawDataDis)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.plainTextEdit_txData = QPlainTextEdit(GroupBox_rawDataDis)
        self.plainTextEdit_txData.setObjectName(u"plainTextEdit_txData")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_txData.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_txData.setSizePolicy(sizePolicy)
        self.plainTextEdit_txData.setMinimumSize(QSize(0, 40))

        self.verticalLayout_2.addWidget(self.plainTextEdit_txData)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_clearTx = QPushButton(GroupBox_rawDataDis)
        self.pushButton_clearTx.setObjectName(u"pushButton_clearTx")

        self.horizontalLayout_4.addWidget(self.pushButton_clearTx)

        self.checkBox_hexSend = QCheckBox(GroupBox_rawDataDis)
        self.checkBox_hexSend.setObjectName(u"checkBox_hexSend")

        self.horizontalLayout_4.addWidget(self.checkBox_hexSend)

        self.checkBox_sendNewLine = QCheckBox(GroupBox_rawDataDis)
        self.checkBox_sendNewLine.setObjectName(u"checkBox_sendNewLine")

        self.horizontalLayout_4.addWidget(self.checkBox_sendNewLine)

        self.spinBox_portTimeValue = QSpinBox(GroupBox_rawDataDis)
        self.spinBox_portTimeValue.setObjectName(u"spinBox_portTimeValue")
        self.spinBox_portTimeValue.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_4.addWidget(self.spinBox_portTimeValue)

        self.label_40 = QLabel(GroupBox_rawDataDis)
        self.label_40.setObjectName(u"label_40")
        font = QFont()
        font.setPointSize(12)
        self.label_40.setFont(font)
        self.label_40.setTextFormat(Qt.PlainText)
        self.label_40.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_40)

        self.checkBox_timerSend = QCheckBox(GroupBox_rawDataDis)
        self.checkBox_timerSend.setObjectName(u"checkBox_timerSend")

        self.horizontalLayout_4.addWidget(self.checkBox_timerSend)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.pushButton_tx = QPushButton(GroupBox_rawDataDis)
        self.pushButton_tx.setObjectName(u"pushButton_tx")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_tx.sizePolicy().hasHeightForWidth())
        self.pushButton_tx.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.pushButton_tx)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.gridLayout.addLayout(self.verticalLayout_2, 2, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_clearDisplay = QPushButton(GroupBox_rawDataDis)
        self.pushButton_clearDisplay.setObjectName(u"pushButton_clearDisplay")

        self.horizontalLayout_5.addWidget(self.pushButton_clearDisplay)

        self.checkBox_suspendDis = QCheckBox(GroupBox_rawDataDis)
        self.checkBox_suspendDis.setObjectName(u"checkBox_suspendDis")

        self.horizontalLayout_5.addWidget(self.checkBox_suspendDis)

        self.checkBox_hexDisplay = QCheckBox(GroupBox_rawDataDis)
        self.checkBox_hexDisplay.setObjectName(u"checkBox_hexDisplay")

        self.horizontalLayout_5.addWidget(self.checkBox_hexDisplay)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.textBrowser_rxData = QTextBrowser(GroupBox_rawDataDis)
        self.textBrowser_rxData.setObjectName(u"textBrowser_rxData")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.textBrowser_rxData.sizePolicy().hasHeightForWidth())
        self.textBrowser_rxData.setSizePolicy(sizePolicy2)
        self.textBrowser_rxData.setMinimumSize(QSize(0, 300))
        self.textBrowser_rxData.setStyleSheet(u"background-color: rgb(218, 218, 218)")

        self.verticalLayout_4.addWidget(self.textBrowser_rxData)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout_4, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(GroupBox_rawDataDis)

        QMetaObject.connectSlotsByName(GroupBox_rawDataDis)
    # setupUi

    def retranslateUi(self, GroupBox_rawDataDis):
        GroupBox_rawDataDis.setWindowTitle(QCoreApplication.translate("GroupBox_rawDataDis", u"Bytes stream", None))
        self.pushButton_clearTx.setText(QCoreApplication.translate("GroupBox_rawDataDis", u"Clear send", None))
        self.checkBox_hexSend.setText(QCoreApplication.translate("GroupBox_rawDataDis", u"Send in hex", None))
        self.checkBox_sendNewLine.setText(QCoreApplication.translate("GroupBox_rawDataDis", u"Send new line", None))
        self.label_40.setText(QCoreApplication.translate("GroupBox_rawDataDis", u"ms", None))
        self.checkBox_timerSend.setText(QCoreApplication.translate("GroupBox_rawDataDis", u"Cycle", None))
        self.pushButton_tx.setText(QCoreApplication.translate("GroupBox_rawDataDis", u"Send", None))
        self.pushButton_clearDisplay.setText(QCoreApplication.translate("GroupBox_rawDataDis", u"Clear", None))
        self.checkBox_suspendDis.setText(QCoreApplication.translate("GroupBox_rawDataDis", u"Suspend", None))
        self.checkBox_hexDisplay.setText(QCoreApplication.translate("GroupBox_rawDataDis", u"ASCII display", None))
    # retranslateUi


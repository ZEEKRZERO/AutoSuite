# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'groupbox_signalFuzz.ui'
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
    QHBoxLayout, QHeaderView, QLabel, QMdiArea,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QSplitter, QTabWidget, QTableView, QWidget)

class Ui_GroupBox_signalFuzz(object):
    def setupUi(self, GroupBox_signalFuzz):
        if not GroupBox_signalFuzz.objectName():
            GroupBox_signalFuzz.setObjectName(u"GroupBox_signalFuzz")
        GroupBox_signalFuzz.resize(1927, 806)
        self.gridLayout_4 = QGridLayout(GroupBox_signalFuzz)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.splitter_2 = QSplitter(GroupBox_signalFuzz)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.groupBox = QGroupBox(self.splitter_2)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QSize(800, 16777215))
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.mdiArea_querySignal = QMdiArea(self.groupBox)
        self.mdiArea_querySignal.setObjectName(u"mdiArea_querySignal")
        self.mdiArea_querySignal.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mdiArea_querySignal.sizePolicy().hasHeightForWidth())
        self.mdiArea_querySignal.setSizePolicy(sizePolicy1)
        self.mdiArea_querySignal.setMaximumSize(QSize(800, 16777215))
        self.mdiArea_querySignal.setViewMode(QMdiArea.TabbedView)
        self.mdiArea_querySignal.setDocumentMode(True)
        self.mdiArea_querySignal.setTabsClosable(False)
        self.mdiArea_querySignal.setTabsMovable(False)
        self.mdiArea_querySignal.setTabShape(QTabWidget.Rounded)
        self.mdiArea_querySignal.setTabPosition(QTabWidget.South)

        self.gridLayout_2.addWidget(self.mdiArea_querySignal, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_addNewSignal = QPushButton(self.groupBox)
        self.pushButton_addNewSignal.setObjectName(u"pushButton_addNewSignal")

        self.horizontalLayout.addWidget(self.pushButton_addNewSignal)

        self.pushButton_addNewSignal_2 = QPushButton(self.groupBox)
        self.pushButton_addNewSignal_2.setObjectName(u"pushButton_addNewSignal_2")

        self.horizontalLayout.addWidget(self.pushButton_addNewSignal_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.splitter_2.addWidget(self.groupBox)
        self.splitter = QSplitter(self.splitter_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.gridLayout_3 = QGridLayout(self.layoutWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_addSendSignal = QPushButton(self.layoutWidget)
        self.pushButton_addSendSignal.setObjectName(u"pushButton_addSendSignal")

        self.gridLayout_3.addWidget(self.pushButton_addSendSignal, 0, 0, 1, 1)

        self.splitter.addWidget(self.layoutWidget)
        self.groupBox_2 = QGroupBox(self.splitter)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableView_sendSignalList = QTableView(self.groupBox_2)
        self.tableView_sendSignalList.setObjectName(u"tableView_sendSignalList")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tableView_sendSignalList.sizePolicy().hasHeightForWidth())
        self.tableView_sendSignalList.setSizePolicy(sizePolicy2)
        self.tableView_sendSignalList.setMinimumSize(QSize(600, 0))
        self.tableView_sendSignalList.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.tableView_sendSignalList, 0, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_clearSendSignalList = QPushButton(self.groupBox_2)
        self.pushButton_clearSendSignalList.setObjectName(u"pushButton_clearSendSignalList")

        self.horizontalLayout_4.addWidget(self.pushButton_clearSendSignalList)

        self.spinBox_portTimeValue = QSpinBox(self.groupBox_2)
        self.spinBox_portTimeValue.setObjectName(u"spinBox_portTimeValue")
        self.spinBox_portTimeValue.setMinimumSize(QSize(80, 0))
        self.spinBox_portTimeValue.setMinimum(1000)
        self.spinBox_portTimeValue.setMaximum(99999)

        self.horizontalLayout_4.addWidget(self.spinBox_portTimeValue)

        self.label_40 = QLabel(self.groupBox_2)
        self.label_40.setObjectName(u"label_40")
        font = QFont()
        font.setPointSize(12)
        self.label_40.setFont(font)
        self.label_40.setTextFormat(Qt.PlainText)
        self.label_40.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_40)

        self.checkBox_timerSend = QCheckBox(self.groupBox_2)
        self.checkBox_timerSend.setObjectName(u"checkBox_timerSend")

        self.horizontalLayout_4.addWidget(self.checkBox_timerSend)

        self.pushButton_fuzzSetting = QPushButton(self.groupBox_2)
        self.pushButton_fuzzSetting.setObjectName(u"pushButton_fuzzSetting")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_fuzzSetting.sizePolicy().hasHeightForWidth())
        self.pushButton_fuzzSetting.setSizePolicy(sizePolicy3)

        self.horizontalLayout_4.addWidget(self.pushButton_fuzzSetting)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.pushButton_sendFuzzSignal = QPushButton(self.groupBox_2)
        self.pushButton_sendFuzzSignal.setObjectName(u"pushButton_sendFuzzSignal")
        sizePolicy3.setHeightForWidth(self.pushButton_sendFuzzSignal.sizePolicy().hasHeightForWidth())
        self.pushButton_sendFuzzSignal.setSizePolicy(sizePolicy3)

        self.horizontalLayout_4.addWidget(self.pushButton_sendFuzzSignal)


        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        self.splitter.addWidget(self.groupBox_2)
        self.splitter_2.addWidget(self.splitter)

        self.gridLayout_4.addWidget(self.splitter_2, 0, 0, 1, 1)


        self.retranslateUi(GroupBox_signalFuzz)

        QMetaObject.connectSlotsByName(GroupBox_signalFuzz)
    # setupUi

    def retranslateUi(self, GroupBox_signalFuzz):
        GroupBox_signalFuzz.setWindowTitle(QCoreApplication.translate("GroupBox_signalFuzz", u"Signal FUZZ", None))
        self.groupBox.setTitle(QCoreApplication.translate("GroupBox_signalFuzz", u"Signal list", None))
        self.pushButton_addNewSignal.setText(QCoreApplication.translate("GroupBox_signalFuzz", u"New signal", None))
        self.pushButton_addNewSignal_2.setText(QCoreApplication.translate("GroupBox_signalFuzz", u"R155 cybersecurity test", None))
        self.pushButton_addSendSignal.setText(QCoreApplication.translate("GroupBox_signalFuzz", u"-->", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("GroupBox_signalFuzz", u"Transmission signal list", None))
        self.pushButton_clearSendSignalList.setText(QCoreApplication.translate("GroupBox_signalFuzz", u"Clear list", None))
        self.label_40.setText(QCoreApplication.translate("GroupBox_signalFuzz", u"ms", None))
        self.checkBox_timerSend.setText(QCoreApplication.translate("GroupBox_signalFuzz", u"Cycle", None))
        self.pushButton_fuzzSetting.setText(QCoreApplication.translate("GroupBox_signalFuzz", u"fuzz parameter", None))
        self.pushButton_sendFuzzSignal.setText(QCoreApplication.translate("GroupBox_signalFuzz", u"Send signals", None))
    # retranslateUi


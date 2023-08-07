# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'groupbox_sniffdata.ui'
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
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QWidget)
import rc_resource

class Ui_GroupBox_sniffData(object):
    def setupUi(self, GroupBox_sniffData):
        if not GroupBox_sniffData.objectName():
            GroupBox_sniffData.setObjectName(u"GroupBox_sniffData")
        GroupBox_sniffData.resize(733, 544)
        icon = QIcon()
        icon.addFile(u":/icons/dataSniff.svg", QSize(), QIcon.Normal, QIcon.Off)
        GroupBox_sniffData.setWindowIcon(icon)
        self.gridLayout = QGridLayout(GroupBox_sniffData)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.checkBox_suspend = QCheckBox(GroupBox_sniffData)
        self.checkBox_suspend.setObjectName(u"checkBox_suspend")

        self.horizontalLayout_15.addWidget(self.checkBox_suspend)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.checkBox_rtSave = QCheckBox(GroupBox_sniffData)
        self.checkBox_rtSave.setObjectName(u"checkBox_rtSave")

        self.horizontalLayout_16.addWidget(self.checkBox_rtSave)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_16)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_14)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_4)

        self.pushButton_setting_2 = QPushButton(GroupBox_sniffData)
        self.pushButton_setting_2.setObjectName(u"pushButton_setting_2")

        self.horizontalLayout_13.addWidget(self.pushButton_setting_2)

        self.pushButton_clear_2 = QPushButton(GroupBox_sniffData)
        self.pushButton_clear_2.setObjectName(u"pushButton_clear_2")

        self.horizontalLayout_13.addWidget(self.pushButton_clear_2)


        self.gridLayout.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)

        self.tableView_mianTable = QTableView(GroupBox_sniffData)
        self.tableView_mianTable.setObjectName(u"tableView_mianTable")

        self.gridLayout.addWidget(self.tableView_mianTable, 1, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label = QLabel(GroupBox_sniffData)
        self.label.setObjectName(u"label")

        self.horizontalLayout_9.addWidget(self.label)

        self.lineEdit_itemsCnt = QLineEdit(GroupBox_sniffData)
        self.lineEdit_itemsCnt.setObjectName(u"lineEdit_itemsCnt")
        self.lineEdit_itemsCnt.setMaximumSize(QSize(80, 16777215))
        self.lineEdit_itemsCnt.setReadOnly(True)

        self.horizontalLayout_9.addWidget(self.lineEdit_itemsCnt)

        self.label_2 = QLabel(GroupBox_sniffData)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_9.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")

        self.horizontalLayout_11.addLayout(self.horizontalLayout_12)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_11)


        self.gridLayout.addLayout(self.horizontalLayout_9, 2, 0, 1, 1)


        self.retranslateUi(GroupBox_sniffData)

        QMetaObject.connectSlotsByName(GroupBox_sniffData)
    # setupUi

    def retranslateUi(self, GroupBox_sniffData):
        GroupBox_sniffData.setWindowTitle(QCoreApplication.translate("GroupBox_sniffData", u"Sinffing", None))
        self.checkBox_suspend.setText(QCoreApplication.translate("GroupBox_sniffData", u"Suspend", None))
        self.checkBox_rtSave.setText(QCoreApplication.translate("GroupBox_sniffData", u"Save to DB", None))
        self.pushButton_setting_2.setText(QCoreApplication.translate("GroupBox_sniffData", u"Sniff Setting", None))
        self.pushButton_clear_2.setText(QCoreApplication.translate("GroupBox_sniffData", u"Clear", None))
        self.label.setText(QCoreApplication.translate("GroupBox_sniffData", u"Total", None))
        self.lineEdit_itemsCnt.setInputMask(QCoreApplication.translate("GroupBox_sniffData", u"0000000000", None))
        self.label_2.setText(QCoreApplication.translate("GroupBox_sniffData", u"items", None))
    # retranslateUi


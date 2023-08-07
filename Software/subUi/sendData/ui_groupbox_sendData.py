# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'groupbox_sendData.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTableView, QWidget)
import rc_resource

class Ui_GroupBox_sendData(object):
    def setupUi(self, GroupBox_sendData):
        if not GroupBox_sendData.objectName():
            GroupBox_sendData.setObjectName(u"GroupBox_sendData")
        GroupBox_sendData.setWindowModality(Qt.NonModal)
        GroupBox_sendData.resize(551, 399)
        icon = QIcon()
        icon.addFile(u":/icons/zeekr.png", QSize(), QIcon.Normal, QIcon.Off)
        GroupBox_sendData.setWindowIcon(icon)
        self.gridLayout = QGridLayout(GroupBox_sendData)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(GroupBox_sendData)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.comboBox_busType = QComboBox(GroupBox_sendData)
        self.comboBox_busType.setObjectName(u"comboBox_busType")

        self.horizontalLayout_2.addWidget(self.comboBox_busType)

        self.pushButton_addData = QPushButton(GroupBox_sendData)
        self.pushButton_addData.setObjectName(u"pushButton_addData")

        self.horizontalLayout_2.addWidget(self.pushButton_addData)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.tableView_data = QTableView(GroupBox_sendData)
        self.tableView_data.setObjectName(u"tableView_data")

        self.gridLayout.addWidget(self.tableView_data, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_clearData = QPushButton(GroupBox_sendData)
        self.pushButton_clearData.setObjectName(u"pushButton_clearData")

        self.horizontalLayout.addWidget(self.pushButton_clearData)

        self.spinBox_repeatInterValue = QSpinBox(GroupBox_sendData)
        self.spinBox_repeatInterValue.setObjectName(u"spinBox_repeatInterValue")
        self.spinBox_repeatInterValue.setMaximum(99999)
        self.spinBox_repeatInterValue.setValue(1000)

        self.horizontalLayout.addWidget(self.spinBox_repeatInterValue)

        self.label = QLabel(GroupBox_sendData)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.checkBox_repeat = QCheckBox(GroupBox_sendData)
        self.checkBox_repeat.setObjectName(u"checkBox_repeat")

        self.horizontalLayout.addWidget(self.checkBox_repeat)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_sendData = QPushButton(GroupBox_sendData)
        self.pushButton_sendData.setObjectName(u"pushButton_sendData")

        self.horizontalLayout.addWidget(self.pushButton_sendData)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)


        self.retranslateUi(GroupBox_sendData)

        QMetaObject.connectSlotsByName(GroupBox_sendData)
    # setupUi

    def retranslateUi(self, GroupBox_sendData):
        GroupBox_sendData.setWindowTitle(QCoreApplication.translate("GroupBox_sendData", u"Send bus data", None))
        self.label_2.setText(QCoreApplication.translate("GroupBox_sendData", u"BusType", None))
        self.pushButton_addData.setText(QCoreApplication.translate("GroupBox_sendData", u"Add Data", None))
        self.pushButton_clearData.setText(QCoreApplication.translate("GroupBox_sendData", u"Clear Data", None))
        self.label.setText(QCoreApplication.translate("GroupBox_sendData", u"ms", None))
        self.checkBox_repeat.setText(QCoreApplication.translate("GroupBox_sendData", u"Repeat", None))
        self.pushButton_sendData.setText(QCoreApplication.translate("GroupBox_sendData", u"Send Data", None))
    # retranslateUi


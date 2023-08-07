# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_selectSignal.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QWidget)
import rc_resource

class Ui_dialog_selectSignal(object):
    def setupUi(self, dialog_selectSignal):
        if not dialog_selectSignal.objectName():
            dialog_selectSignal.setObjectName(u"dialog_selectSignal")
        dialog_selectSignal.resize(308, 107)
        icon = QIcon()
        icon.addFile(u":/icons/setting.svg", QSize(), QIcon.Normal, QIcon.Off)
        dialog_selectSignal.setWindowIcon(icon)
        self.gridLayout_2 = QGridLayout(dialog_selectSignal)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(dialog_selectSignal)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_selfDefineSignalName = QLineEdit(self.groupBox)
        self.lineEdit_selfDefineSignalName.setObjectName(u"lineEdit_selfDefineSignalName")

        self.horizontalLayout.addWidget(self.lineEdit_selfDefineSignalName)

        self.checkBox_isUseUB = QCheckBox(self.groupBox)
        self.checkBox_isUseUB.setObjectName(u"checkBox_isUseUB")

        self.horizontalLayout.addWidget(self.checkBox_isUseUB)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.pushButton_cancel = QPushButton(dialog_selectSignal)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")

        self.horizontalLayout_4.addWidget(self.pushButton_cancel)

        self.pushButton_ok = QPushButton(dialog_selectSignal)
        self.pushButton_ok.setObjectName(u"pushButton_ok")

        self.horizontalLayout_4.addWidget(self.pushButton_ok)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)


        self.retranslateUi(dialog_selectSignal)

        QMetaObject.connectSlotsByName(dialog_selectSignal)
    # setupUi

    def retranslateUi(self, dialog_selectSignal):
        dialog_selectSignal.setWindowTitle(QCoreApplication.translate("dialog_selectSignal", u"Edit signal", None))
        self.groupBox.setTitle(QCoreApplication.translate("dialog_selectSignal", u"Edit signal", None))
        self.label.setText(QCoreApplication.translate("dialog_selectSignal", u"Name", None))
        self.checkBox_isUseUB.setText(QCoreApplication.translate("dialog_selectSignal", u"UB", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("dialog_selectSignal", u"Cancel", None))
        self.pushButton_ok.setText(QCoreApplication.translate("dialog_selectSignal", u"OK", None))
    # retranslateUi


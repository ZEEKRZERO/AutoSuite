# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_fuzzSetting.ui'
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
    QGroupBox, QHBoxLayout, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import rc_resource

class Ui_Dialog_fuzzSetting(object):
    def setupUi(self, Dialog_fuzzSetting):
        if not Dialog_fuzzSetting.objectName():
            Dialog_fuzzSetting.setObjectName(u"Dialog_fuzzSetting")
        Dialog_fuzzSetting.resize(291, 134)
        icon = QIcon()
        icon.addFile(u":/icons/zeekr.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog_fuzzSetting.setWindowIcon(icon)
        self.gridLayout_2 = QGridLayout(Dialog_fuzzSetting)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(Dialog_fuzzSetting)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setTristate(True)

        self.horizontalLayout.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setTristate(True)

        self.horizontalLayout.addWidget(self.checkBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkBox_3 = QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setTristate(True)

        self.horizontalLayout_2.addWidget(self.checkBox_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButton_cancel = QPushButton(Dialog_fuzzSetting)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")

        self.horizontalLayout_3.addWidget(self.pushButton_cancel)

        self.pushButton_ok = QPushButton(Dialog_fuzzSetting)
        self.pushButton_ok.setObjectName(u"pushButton_ok")

        self.horizontalLayout_3.addWidget(self.pushButton_ok)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)


        self.retranslateUi(Dialog_fuzzSetting)

        QMetaObject.connectSlotsByName(Dialog_fuzzSetting)
    # setupUi

    def retranslateUi(self, Dialog_fuzzSetting):
        Dialog_fuzzSetting.setWindowTitle(QCoreApplication.translate("Dialog_fuzzSetting", u"Fuzz Setting", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog_fuzzSetting", u"Fuzz Setting", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog_fuzzSetting", u"random ID  ", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog_fuzzSetting", u"random Data", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog_fuzzSetting", u"random length", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("Dialog_fuzzSetting", u"cancel", None))
        self.pushButton_ok.setText(QCoreApplication.translate("Dialog_fuzzSetting", u"ok", None))
    # retranslateUi


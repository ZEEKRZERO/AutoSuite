# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_about.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import rc_resource

class Ui_Dialog_about(object):
    def setupUi(self, Dialog_about):
        if not Dialog_about.objectName():
            Dialog_about.setObjectName(u"Dialog_about")
        Dialog_about.setEnabled(True)
        Dialog_about.resize(491, 176)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog_about.sizePolicy().hasHeightForWidth())
        Dialog_about.setSizePolicy(sizePolicy)
        Dialog_about.setCursor(QCursor(Qt.ArrowCursor))
        icon = QIcon()
        icon.addFile(u":/icons/zeekr.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog_about.setWindowIcon(icon)
        Dialog_about.setAutoFillBackground(False)
        Dialog_about.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        Dialog_about.setSizeGripEnabled(False)
        self.gridLayout = QGridLayout(Dialog_about)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(Dialog_about)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(150, 150))
        self.label_3.setStyleSheet(u"image: url(:/icons/autoSuite.png);")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label = QLabel(Dialog_about)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        font = QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setTextFormat(Qt.AutoText)
        self.label.setOpenExternalLinks(True)
        self.label.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_2 = QLabel(Dialog_about)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Adobe Gothic Std B"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.label_2)

        self.label_5 = QLabel(Dialog_about)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(Dialog_about)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.label_4 = QLabel(Dialog_about)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)


        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)


        self.retranslateUi(Dialog_about)

        QMetaObject.connectSlotsByName(Dialog_about)
    # setupUi

    def retranslateUi(self, Dialog_about):
        Dialog_about.setWindowTitle(QCoreApplication.translate("Dialog_about", u"about AutoSuite", None))
        self.label_3.setText("")
        self.label.setText(QCoreApplication.translate("Dialog_about", u"<a href=\"www.autosuite.org\">AutoSuite</a>", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_about", u"www.autosuite.org", None))
        self.label_5.setText(QCoreApplication.translate("Dialog_about", u"version: 1.0", None))
        self.label_6.setText(QCoreApplication.translate("Dialog_about", u"Built on 2023/7/27", None))
        self.label_4.setText(QCoreApplication.translate("Dialog_about", u"Copyright 2023 The ZEEKR ZERO. All rights reserved.", None))
    # retranslateUi


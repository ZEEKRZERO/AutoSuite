# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_processStatus.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import rc_resource

class Ui_Dialog_processStatus(object):
    def setupUi(self, Dialog_processStatus):
        if not Dialog_processStatus.objectName():
            Dialog_processStatus.setObjectName(u"Dialog_processStatus")
        Dialog_processStatus.resize(297, 130)
        icon = QIcon()
        icon.addFile(u":/icons/zeekr.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog_processStatus.setWindowIcon(icon)
        self.gridLayout_2 = QGridLayout(Dialog_processStatus)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(Dialog_processStatus)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_tips = QLabel(self.groupBox)
        self.label_tips.setObjectName(u"label_tips")

        self.verticalLayout.addWidget(self.label_tips)

        self.progressBar = QProgressBar(self.groupBox)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_cancel = QPushButton(Dialog_processStatus)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")

        self.horizontalLayout.addWidget(self.pushButton_cancel)

        self.pushButton_ok = QPushButton(Dialog_processStatus)
        self.pushButton_ok.setObjectName(u"pushButton_ok")

        self.horizontalLayout.addWidget(self.pushButton_ok)


        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)


        self.retranslateUi(Dialog_processStatus)

        QMetaObject.connectSlotsByName(Dialog_processStatus)
    # setupUi

    def retranslateUi(self, Dialog_processStatus):
        Dialog_processStatus.setWindowTitle(QCoreApplication.translate("Dialog_processStatus", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog_processStatus", u"\u63d0\u793a", None))
        self.label_tips.setText(QCoreApplication.translate("Dialog_processStatus", u"\u63d0\u793a", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("Dialog_processStatus", u"\u53d6\u6d88", None))
        self.pushButton_ok.setText(QCoreApplication.translate("Dialog_processStatus", u"\u786e\u5b9a", None))
    # retranslateUi


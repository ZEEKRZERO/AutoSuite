# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_setQueryCondition.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QGridLayout, QGroupBox, QSizePolicy,
    QWidget)
import rc_resource

class Ui_dialog_setCondition(object):
    def setupUi(self, dialog_setCondition):
        if not dialog_setCondition.objectName():
            dialog_setCondition.setObjectName(u"dialog_setCondition")
        dialog_setCondition.resize(287, 285)
        icon = QIcon()
        icon.addFile(u":/icons/zeekr.png", QSize(), QIcon.Normal, QIcon.Off)
        dialog_setCondition.setWindowIcon(icon)
        self.gridLayout = QGridLayout(dialog_setCondition)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_setCondition = QGroupBox(dialog_setCondition)
        self.groupBox_setCondition.setObjectName(u"groupBox_setCondition")
        self.gridLayout_2 = QGridLayout(self.groupBox_setCondition)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.formLayout_setCondition = QFormLayout()
        self.formLayout_setCondition.setObjectName(u"formLayout_setCondition")

        self.gridLayout_2.addLayout(self.formLayout_setCondition, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_setCondition, 0, 0, 1, 1)

        self.buttonBox_okOrCancel = QDialogButtonBox(dialog_setCondition)
        self.buttonBox_okOrCancel.setObjectName(u"buttonBox_okOrCancel")
        self.buttonBox_okOrCancel.setOrientation(Qt.Horizontal)
        self.buttonBox_okOrCancel.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox_okOrCancel.setCenterButtons(False)

        self.gridLayout.addWidget(self.buttonBox_okOrCancel, 1, 0, 1, 1)


        self.retranslateUi(dialog_setCondition)
        self.buttonBox_okOrCancel.accepted.connect(dialog_setCondition.accept)
        self.buttonBox_okOrCancel.rejected.connect(dialog_setCondition.reject)

        QMetaObject.connectSlotsByName(dialog_setCondition)
    # setupUi

    def retranslateUi(self, dialog_setCondition):
        dialog_setCondition.setWindowTitle(QCoreApplication.translate("dialog_setCondition", u"Set query conditions", None))
        self.groupBox_setCondition.setTitle(QCoreApplication.translate("dialog_setCondition", u"Set query conditions", None))
    # retranslateUi


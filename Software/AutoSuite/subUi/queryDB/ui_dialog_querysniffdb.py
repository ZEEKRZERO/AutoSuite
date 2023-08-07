# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_querysniffdb.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
    QDialog, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTableView, QVBoxLayout,
    QWidget)
import rc_resource

class Ui_Dialog_querySniffDB(object):
    def setupUi(self, Dialog_querySniffDB):
        if not Dialog_querySniffDB.objectName():
            Dialog_querySniffDB.setObjectName(u"Dialog_querySniffDB")
        Dialog_querySniffDB.setWindowModality(Qt.WindowModal)
        Dialog_querySniffDB.setEnabled(True)
        Dialog_querySniffDB.resize(813, 601)
        icon = QIcon()
        icon.addFile(u":/icons/dataQuery.svg", QSize(), QIcon.Normal, QIcon.Off)
        Dialog_querySniffDB.setWindowIcon(icon)
        Dialog_querySniffDB.setSizeGripEnabled(False)
        Dialog_querySniffDB.setModal(False)
        self.gridLayout = QGridLayout(Dialog_querySniffDB)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_10 = QLabel(Dialog_querySniffDB)
        self.label_10.setObjectName(u"label_10")
        font = QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)

        self.horizontalLayout_12.addWidget(self.label_10)

        self.comboBox_swSqlLib = QComboBox(Dialog_querySniffDB)
        self.comboBox_swSqlLib.setObjectName(u"comboBox_swSqlLib")

        self.horizontalLayout_12.addWidget(self.comboBox_swSqlLib)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_12)

        self.label_4 = QLabel(Dialog_querySniffDB)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.comboBox_swtable = QComboBox(Dialog_querySniffDB)
        self.comboBox_swtable.setObjectName(u"comboBox_swtable")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_swtable.sizePolicy().hasHeightForWidth())
        self.comboBox_swtable.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.comboBox_swtable)

        self.pushButton_deleteTable = QPushButton(Dialog_querySniffDB)
        self.pushButton_deleteTable.setObjectName(u"pushButton_deleteTable")

        self.horizontalLayout_6.addWidget(self.pushButton_deleteTable)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBox_enableFilter = QCheckBox(Dialog_querySniffDB)
        self.checkBox_enableFilter.setObjectName(u"checkBox_enableFilter")

        self.horizontalLayout.addWidget(self.checkBox_enableFilter)

        self.pushButton_setQuerycondition = QPushButton(Dialog_querySniffDB)
        self.pushButton_setQuerycondition.setObjectName(u"pushButton_setQuerycondition")

        self.horizontalLayout.addWidget(self.pushButton_setQuerycondition)

        self.label_startTime = QLabel(Dialog_querySniffDB)
        self.label_startTime.setObjectName(u"label_startTime")
        self.label_startTime.setFont(font)

        self.horizontalLayout.addWidget(self.label_startTime)

        self.dateTimeEdit_start = QDateTimeEdit(Dialog_querySniffDB)
        self.dateTimeEdit_start.setObjectName(u"dateTimeEdit_start")
        self.dateTimeEdit_start.setDateTime(QDateTime(QDate(1752, 9, 14), QTime(0, 0, 0)))

        self.horizontalLayout.addWidget(self.dateTimeEdit_start)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_endTime = QLabel(Dialog_querySniffDB)
        self.label_endTime.setObjectName(u"label_endTime")
        self.label_endTime.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_endTime)

        self.dateTimeEdit_end = QDateTimeEdit(Dialog_querySniffDB)
        self.dateTimeEdit_end.setObjectName(u"dateTimeEdit_end")
        self.dateTimeEdit_end.setDateTime(QDateTime(QDate(2200, 1, 1), QTime(0, 0, 0)))

        self.horizontalLayout_3.addWidget(self.dateTimeEdit_end)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_8.addLayout(self.verticalLayout)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_outputcsv = QPushButton(Dialog_querySniffDB)
        self.pushButton_outputcsv.setObjectName(u"pushButton_outputcsv")

        self.verticalLayout_2.addWidget(self.pushButton_outputcsv)

        self.pushButton_dbcDecode = QPushButton(Dialog_querySniffDB)
        self.pushButton_dbcDecode.setObjectName(u"pushButton_dbcDecode")

        self.verticalLayout_2.addWidget(self.pushButton_dbcDecode)


        self.horizontalLayout_8.addLayout(self.verticalLayout_2)


        self.gridLayout.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)

        self.tableView_sniffdb = QTableView(Dialog_querySniffDB)
        self.tableView_sniffdb.setObjectName(u"tableView_sniffdb")

        self.gridLayout.addWidget(self.tableView_sniffdb, 1, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_8 = QLabel(Dialog_querySniffDB)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_8)

        self.lineEdit_linesofpage = QLineEdit(Dialog_querySniffDB)
        self.lineEdit_linesofpage.setObjectName(u"lineEdit_linesofpage")
        self.lineEdit_linesofpage.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_linesofpage.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_linesofpage)

        self.label_9 = QLabel(Dialog_querySniffDB)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_9)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_2)

        self.label_5 = QLabel(Dialog_querySniffDB)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setFont(font)

        self.horizontalLayout_11.addWidget(self.label_5)

        self.lineEdit_totalLine = QLineEdit(Dialog_querySniffDB)
        self.lineEdit_totalLine.setObjectName(u"lineEdit_totalLine")
        self.lineEdit_totalLine.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_totalLine.setReadOnly(True)

        self.horizontalLayout_11.addWidget(self.lineEdit_totalLine)

        self.label_6 = QLabel(Dialog_querySniffDB)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setFont(font)

        self.horizontalLayout_11.addWidget(self.label_6)

        self.lineEdit_allPages = QLineEdit(Dialog_querySniffDB)
        self.lineEdit_allPages.setObjectName(u"lineEdit_allPages")
        self.lineEdit_allPages.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_allPages.setReadOnly(True)

        self.horizontalLayout_11.addWidget(self.lineEdit_allPages)

        self.label_7 = QLabel(Dialog_querySniffDB)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.horizontalLayout_11.addWidget(self.label_7)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_11)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.spinBox_page = QSpinBox(Dialog_querySniffDB)
        self.spinBox_page.setObjectName(u"spinBox_page")
        self.spinBox_page.setMinimum(1)

        self.horizontalLayout_7.addWidget(self.spinBox_page)

        self.pushButton_prvePage = QPushButton(Dialog_querySniffDB)
        self.pushButton_prvePage.setObjectName(u"pushButton_prvePage")

        self.horizontalLayout_7.addWidget(self.pushButton_prvePage)

        self.pushButton_nextPage = QPushButton(Dialog_querySniffDB)
        self.pushButton_nextPage.setObjectName(u"pushButton_nextPage")

        self.horizontalLayout_7.addWidget(self.pushButton_nextPage)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_7)


        self.gridLayout.addLayout(self.horizontalLayout_10, 2, 0, 1, 1)


        self.retranslateUi(Dialog_querySniffDB)

        QMetaObject.connectSlotsByName(Dialog_querySniffDB)
    # setupUi

    def retranslateUi(self, Dialog_querySniffDB):
        Dialog_querySniffDB.setWindowTitle(QCoreApplication.translate("Dialog_querySniffDB", u"Data query", None))
        self.label_10.setText(QCoreApplication.translate("Dialog_querySniffDB", u"Database", None))
        self.label_4.setText(QCoreApplication.translate("Dialog_querySniffDB", u"Table", None))
        self.pushButton_deleteTable.setText(QCoreApplication.translate("Dialog_querySniffDB", u"Delete this table", None))
        self.checkBox_enableFilter.setText(QCoreApplication.translate("Dialog_querySniffDB", u"Query filtering", None))
        self.pushButton_setQuerycondition.setText(QCoreApplication.translate("Dialog_querySniffDB", u"Query condition", None))
        self.label_startTime.setText(QCoreApplication.translate("Dialog_querySniffDB", u"Start time", None))
        self.dateTimeEdit_start.setDisplayFormat(QCoreApplication.translate("Dialog_querySniffDB", u"yyyy-MM-dd HH:mm:ss", None))
        self.label_endTime.setText(QCoreApplication.translate("Dialog_querySniffDB", u"End time", None))
        self.dateTimeEdit_end.setDisplayFormat(QCoreApplication.translate("Dialog_querySniffDB", u"yyyy-MM-dd HH:mm:ss", None))
        self.pushButton_outputcsv.setText(QCoreApplication.translate("Dialog_querySniffDB", u"Export csv file", None))
        self.pushButton_dbcDecode.setText(QCoreApplication.translate("Dialog_querySniffDB", u"Parsing DBC files", None))
        self.label_8.setText(QCoreApplication.translate("Dialog_querySniffDB", u"One page", None))
        self.label_9.setText(QCoreApplication.translate("Dialog_querySniffDB", u"items\uff0c", None))
        self.label_5.setText(QCoreApplication.translate("Dialog_querySniffDB", u"total", None))
        self.label_6.setText(QCoreApplication.translate("Dialog_querySniffDB", u"items,", None))
        self.label_7.setText(QCoreApplication.translate("Dialog_querySniffDB", u"Pages", None))
        self.pushButton_prvePage.setText(QCoreApplication.translate("Dialog_querySniffDB", u"Previous", None))
        self.pushButton_nextPage.setText(QCoreApplication.translate("Dialog_querySniffDB", u"Next", None))
    # retranslateUi


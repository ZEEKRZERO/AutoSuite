# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass

from PySide6.QtWidgets import QMessageBox, QFileDialog, QMenu, QDialog, QLineEdit, QLabel, QAbstractItemView
from PySide6 import QtWidgets
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Signal, Slot, Qt, QSize, QThread
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel

from app.app_utilities import AppUtilitiesClass
from layers.appDataLay.dbcdecode import ThreadObj_App_dbcDecode

from subUi.queryDB.ui_dialog_querysniffdb import Ui_Dialog_querySniffDB
from subUi.queryDB.dialog_setQueryCondition import Dialog_setCondition
from subUi.signalFuzz.dialog_selectSignal import Dialog_selectSignal




class Dialog_querySniffDB(QtWidgets.QDialog):
    def __init__(self, mainWin, list_dbName=None, parent=None):
        super().__init__(parent)

        self.ui = Ui_Dialog_querySniffDB()
        self.ui.setupUi(self)

        self.ui.comboBox_swtable.blockSignals(True)
        self.ui.comboBox_swSqlLib.blockSignals(True)

        self.mainWin = mainWin

        # 设置数据查询显示列表表格被选整行
        self.ui.tableView_sniffdb.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 获取数据库名字
        self.get_sqlDatabaseNames(list_dbName)

        # 表字典，key是表名字，value是表信息字典
        self.tables_dict = {}
        
        # 当前选择的数据库
        self.sqlDatabaseName_current = None

        # 当前显示的表
        self.tableInfoDict_current = None

        # 获取数据库当中存在的表
        self.get_sniffDB_tableNames()

        self.ui.comboBox_swtable.blockSignals(False)
        self.ui.comboBox_swSqlLib.blockSignals(False)

        if len(self.tables_dict) == 0:
            # 数据库没有表可查，提示错误，并退出
            QMessageBox.information(None, "Database is empty", "Database is empty!")

        # 设置表格的右键菜单
        self.ui.tableView_sniffdb.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.tableView_sniffdb.customContextMenuRequested.connect(self.show_context_menu)
        # 创建右键菜单
        self.tableView_sniffdb_context_menu = QMenu(self)

        # 添加动作到菜单
        # delete_action = QAction("删除", self)
        # self.tableView_sniffdb_context_menu.addAction(delete_action)


        # 连接信号
    
        self.on_comboBox_swSqlLib_currentTextChanged()

    # 显示右键菜单栏
    @Slot(int)
    def show_context_menu(self, pos):

        # 获取当前行的索引
        current_row = self.ui.tableView_sniffdb.rowAt(pos.y())
        self.ui.tableView_sniffdb.selectRow(current_row)  # 选择整行
        # 在指定位置显示菜单
        self.tableView_sniffdb_context_menu.exec_(self.ui.tableView_sniffdb.mapToGlobal(pos))

    # 获取选择的一整行的数据
    @Slot()
    def get_seleteRowsData_slot(self):

        # 获取选中的行索引
        selectedIndexes = self.ui.tableView_sniffdb.selectionModel().selectedRows()
        # 获取选中行的行号
        selectedRows = [index.row() for index in selectedIndexes]

        list_tableHeader = self.tableInfoDict_current["list_tableHeader"]
        model = self.ui.tableView_sniffdb.model()
        data_list = []
        for row in selectedRows:
            # 获取该行的数据
            row_data_dict = {}
            for col in range(len(list_tableHeader)):
                item = model.data(model.index(row, col))
                if item is not None:
                    row_data_dict[list_tableHeader[col]] = item
                else:
                    row_data_dict[list_tableHeader[col]] = ""
            data_list.append(row_data_dict)
        # 发送获取结果
        self.signal_get_seleteRowsData_result.emit(data_list)

        # 返回获取的结果
        return data_list


    # 获取选择的一整行的数据，并进行编辑
    @Slot()
    def get_selectAndEditRowData_slot(self):
        # 获取选择的行号
        selected_Indexes = self.ui.tableView_sniffdb.selectedIndexes()
        selectedRow = selected_Indexes.pop().row()
        # 获取该行的数据
        row_data_dict = {}
        list_tableHeader = self.tableInfoDict_current["list_tableHeader"]
        model = self.ui.tableView_sniffdb.model()
        for col in range(len(list_tableHeader)):
            # item = self.ui.tableView_sniffdb.model().item(selectedRow, col)
            item = model.data(model.index(selectedRow, col))
            if item is not None:
                row_data_dict[list_tableHeader[col]] = item
            else:
                row_data_dict[list_tableHeader[col]] = ""
        # 编辑 获取的结果
        isNeedUB = row_data_dict["signal_name"][-3:] != "_UB"
        ## 弹出编辑对话框
        dialog = Dialog_selectSignal(isNeedUB)
        dialog.exec()
        cfgParam_dict = dialog.cfgParam_dict
        row_data_dict["name"] = cfgParam_dict["selfDefineSignalName"]
        isUseUB = cfgParam_dict["isUseUB"]
        
        if isNeedUB and isUseUB:
            # 查询数据库获取UB位
            tableName = self.tableInfoDict_current["tableName"]
            db = AppUtilitiesClass.sqlDB_connect(self.sqlDatabaseName_current)
            signalName_UB = row_data_dict["signal_name"] + "_UB"
            query = QSqlQuery(db)
            query.exec(f"SELECT * FROM {tableName} WHERE signal_name = '{signalName_UB}'")
            if query.next():
                row_data_dict["UB"] = query.value("start_bit")
            else:
                # 没有找到 UB 信号
                QMessageBox.critical(None, f"UB NOT FIND", f"the signal {signalName_UB} not find!")
                row_data_dict["UB"] = ""
            AppUtilitiesClass.sqlDB_disconnect(db)
        else:
            row_data_dict["UB"] = ""

        # 发送获取的结果
        self.signal_get_selectAndEditRowData_result.emit(row_data_dict)
        # 返回获取的结果
        return row_data_dict

    @Slot()
    # 获取当前可选的数据名称，并显示
    def get_sqlDatabaseNames(self, list_dbName):
        if list_dbName is None:
            list_sqlDatabaseNames = ["sniffDataDB", "dbcDataDB"]
        else :
            list_sqlDatabaseNames = list_dbName

        # 显示与添加存在的数据库
        for sqlDatabaseName in list_sqlDatabaseNames:
            self.ui.comboBox_swSqlLib.addItem(sqlDatabaseName)

    # 获取当前数据库当中存在的表，并显示
    @Slot()
    def get_sniffDB_tableNames(self):

        # 获取当前选择的数据库名称
        self.sqlDatabaseName_current = self.ui.comboBox_swSqlLib.currentText()
        # 与数据库建立连接
        db = AppUtilitiesClass.sqlDB_connect(self.sqlDatabaseName_current)
        list_tableNames = db.tables()

        self.ui.tableView_sniffdb.setModel(None)
        self.ui.comboBox_swtable.clear()
        if len(list_tableNames):
            # 显示与添加存在的表
            self.ui.comboBox_swtable.clear()
            for tableName in list_tableNames:
                self.ui.comboBox_swtable.addItem(tableName)
                self.tables_dict[tableName] = {
                "tableName" : tableName,
                "totalItems" : 0,
                "totalPages" : 0,
                "pageSize" : 200,
                "currentPage" : 1,
                "conditionString":"",
                "list_tableHeader":[],
                }
            self.ui.pushButton_deleteTable.setEnabled(True)
            self.on_comboBox_swtable_currentTextChanged()
        else:
            self.ui.pushButton_deleteTable.setEnabled(False)
            self.tables_dict = {}

        # 关闭数据库连接
        AppUtilitiesClass.sqlDB_disconnect(db)

    # 获取数据库当中的符合条件的数据信息，并进行显示
    @Slot()
    def get_info_sniffDB_slot(self):
        # 与数据库建立连接
        db = AppUtilitiesClass.sqlDB_connect(self.sqlDatabaseName_current)
        query = QSqlQuery(db)

        
        tableName = self.tableInfoDict_current["tableName"]
        conditionString = self.tableInfoDict_current["conditionString"]
        bbb = query.exec(f'SELECT COUNT(*) FROM {tableName} ' + conditionString)
        if query.next():
            recordCount = query.value(0)
            self.tableInfoDict_current["totalItems"] = recordCount
            self.tableInfoDict_current["totalPages"] = int(recordCount / self.tableInfoDict_current["pageSize"]);
            if recordCount % self.tableInfoDict_current["pageSize"] > 0 :
                self.tableInfoDict_current["totalPages"] = self.tableInfoDict_current["totalPages"] + 1

        else:
            self.tableInfoDict_current["totalItems"] = 0
            self.tableInfoDict_current["totalPages"] = 0
        
        self.tableInfoDict_current["currentPage"] = 1
        self.ui.spinBox_page.blockSignals(True)
        self.ui.spinBox_page.setValue(1)
        self.ui.spinBox_page.blockSignals(False)

        # 界面显示
        self.ui.lineEdit_totalLine.setText(str(self.tableInfoDict_current["totalItems"]))
        self.ui.lineEdit_allPages.setText(str(self.tableInfoDict_current["totalPages"]))
        self.ui.lineEdit_linesofpage.setText(str(self.tableInfoDict_current["pageSize"]))
        if self.tableInfoDict_current["totalPages"] > 0:
            self.ui.spinBox_page.setMaximum(self.tableInfoDict_current["totalPages"])
        else:
            self.ui.spinBox_page.setMaximum(1)

        # 关闭数据库连
        AppUtilitiesClass.sqlDB_disconnect(db)

    # 刷新并显示数据查询结果表格    
    @Slot()
    def reflash_sniffDB_queryData_slot(self):
        # 与数据库建立连接
        db = AppUtilitiesClass.sqlDB_connect(self.sqlDatabaseName_current)

        # 查询数据
        query_model = QSqlQueryModel()
        query = QSqlQuery(db)

        tableName = self.tableInfoDict_current["tableName"]
        conditionString = self.tableInfoDict_current["conditionString"]
        startIndex = (self.tableInfoDict_current["currentPage"] - 1) * self.tableInfoDict_current["pageSize"]

        query.prepare(f"SELECT * FROM {tableName} " + conditionString + " LIMIT :limit OFFSET :offset")
        
        # print(f"SELECT * FROM {tableName} " + conditionString + " LIMIT :limit OFFSET :offset")

        query.bindValue(":limit", self.tableInfoDict_current["pageSize"])
        query.bindValue(":offset", startIndex)

        aaa = query.exec()
        # print("aaa", aaa)

        query_model.setQuery(query)
        # 显示数据
        self.ui.tableView_sniffdb.setModel(query_model)

        # 获取表格的表头列表
        header = []
        header_view = self.ui.tableView_sniffdb.horizontalHeader()
        for column in range(self.ui.tableView_sniffdb.model().columnCount()):
            item = header_view.model().headerData(column, header_view.orientation())
            header.append(item)
        self.tableInfoDict_current["list_tableHeader"] = header

        # 关闭数据库连接
        AppUtilitiesClass.sqlDB_disconnect(db)


    # 设置查询条件
    @Slot()
    def set_sniffDB_queryCondition(self, isEnableFilter):

        conditionString = ""
        if isEnableFilter :
            # 获取查询条件
            startTime = self.ui.dateTimeEdit_start.text()
            endTime = self.ui.dateTimeEdit_end.text()
            time_conditionString = f"WHERE receiveTime >= '{startTime}' AND receiveTime <= '{endTime}'" 
            conditionString += time_conditionString
            

        # print(conditionString)
            
        self.tableInfoDict_current["conditionString"] = conditionString

        # 更新表格查询结果信息
        self.get_info_sniffDB_slot()

        # 更新表格显示
        self.reflash_sniffDB_queryData_slot()

    # 切换表
    @Slot()
    def on_comboBox_swtable_currentTextChanged(self):
        tableName = self.ui.comboBox_swtable.currentText()
        if tableName in list(self.tables_dict.keys()):
            self.tableInfoDict_current = self.tables_dict[tableName]
            self.get_info_sniffDB_slot()
            self.reflash_sniffDB_queryData_slot()
            
    # 切换数据库
    @Slot()
    def on_comboBox_swSqlLib_currentTextChanged(self):
        if self.ui.comboBox_swSqlLib.currentText() == "sniffDataDB":
            self.ui.label_startTime.setVisible(True)
            self.ui.label_endTime.setVisible(True)
            self.ui.dateTimeEdit_start.setVisible(True)
            self.ui.dateTimeEdit_end.setVisible(True)
        else:
            self.ui.label_startTime.setVisible(False)
            self.ui.label_endTime.setVisible(False)
            self.ui.dateTimeEdit_start.setVisible(False)
            self.ui.dateTimeEdit_end.setVisible(False)
        self.get_sniffDB_tableNames()

    @Slot()
    def on_pushButton_prvePage_clicked(self):
        value = self.ui.spinBox_page.value() - 1
        if value == 0 :
            value = 1
        self.ui.spinBox_page.setValue(value)
    
    @Slot()
    def on_pushButton_nextPage_clicked(self):
        value_max = self.tableInfoDict_current["totalPages"]
        value = self.ui.spinBox_page.value() + 1
        if value > value_max:
            value = value_max
        self.ui.spinBox_page.setValue(value)

    @Slot()
    def on_spinBox_page_valueChanged(self):
        self.tableInfoDict_current["currentPage"] = self.ui.spinBox_page.value()
        self.reflash_sniffDB_queryData_slot()

    @Slot()
    def on_checkBox_enableFilter_stateChanged(self):
        self.set_sniffDB_queryCondition(self.ui.checkBox_enableFilter.isChecked())

    @Slot()
    def on_pushButton_dbcDecode_clicked(self):
        # 创建文件选择对话框实例
        file_dialog = QFileDialog(self)
        # 设置对话框选项
        file_dialog.setDirectory("./data/opendbc")
        file_dialog.setFileMode(QFileDialog.ExistingFile) 
        # 显示对话框并获取选择的文件
        selected_file, _ = file_dialog.getOpenFileName(caption="Open dbc File",filter="DBC files (*.dbc)")
        if selected_file:
            # 创建一个解析 DBC 文件的线程
            ## 创建线程
            self.thread_dbcDecode = QThread(self)
            self.threadObj_dbcDecode = ThreadObj_App_dbcDecode()
            self.threadObj_dbcDecode.moveToThread(self.thread_dbcDecode)
            self.thread_dbcDecode.finished.connect(self.thread_dbcDecode.deleteLater)
            self.thread_dbcDecode.finished.connect(self.threadObj_dbcDecode.deleteLater)

            # 信号连接
            self.threadObj_dbcDecode.base_connect(self.mainWin) # 基本信号连接
            self.singal_statrDbcDecode.connect(self.threadObj_dbcDecode.parse_dbc_file)
            self.threadObj_dbcDecode.signal_dbcDecode_complete.connect(self.thread_dbcDecode.quit) # 解析完成退出这个线程
            self.threadObj_dbcDecode.signal_dbcDecode_complete.connect(lambda tableName :(
                self.get_sniffDB_tableNames(), # 解析完成刷新数据查询显示
                self.ui.comboBox_swtable.setCurrentText(tableName) # 切换显示最新解析出的表格
            ))
            # 启动线程
            self.thread_dbcDecode.start()
  
            # 发送解析信号，开始解析
            self.singal_statrDbcDecode.emit(selected_file, self.sqlDatabaseName_current)

    @Slot()
    def on_pushButton_deleteTable_clicked(self):
        # 获取表格名称
        tableName = self.ui.comboBox_swtable.currentText()

        # 创建消息对话框
        msg_box = QMessageBox()
        msg_box.setText(f"Confirm deletion table:{tableName}?")
        msg_box.setWindowTitle("Tips")
        msg_box.setIcon(QMessageBox.Information)
        msg_box.addButton("OK", QMessageBox.AcceptRole)
        msg_box.addButton("Cancel", QMessageBox.RejectRole)
        icon = QIcon()
        icon.addFile(u":/icons/zeekr", QSize(), QIcon.Normal, QIcon.Off)
        msg_box.setWindowIcon(icon)

        # 弹出对话框并等待用户操作
        response = msg_box.exec()
        if response == 0:
            self.singal_tipsPrint.emit(f"Start deleting table [{tableName}]")
            self.singal_tipsPrint.emit(f"Deleting table [{tableName}] ......")
            db = AppUtilitiesClass.sqlDB_connect(self.sqlDatabaseName_current)
            AppUtilitiesClass.sqlDB_delete_table(db, tableName)
            AppUtilitiesClass.sqlDB_disconnect(db)
            self.get_sniffDB_tableNames()
            self.singal_tipsPrint.emit(f"Successfully deleted table [{tableName}] ！")

    # 弹出设置查询条件对话框
    @Slot()
    def on_pushButton_setQuerycondition_clicked(self):
        # 弹出对话框
        dialog = Dialog_setCondition(self)
        ## 向对话框添加设置表项
        for header in self.tableInfoDict_current["list_tableHeader"]:
            dialog.ui.formLayout_setCondition.addRow(f"{header}= ",QLineEdit("123", objectName=f"lineEdit_{header}", parent=dialog))
        dialog.ui.formLayout_setCondition.addRow(f"SQL = ", QLineEdit("123", objectName="lineEdit_sql", parent=dialog))
        dialog.setup_editFormConnect()
        dialog.exec()
        pass


    # 开始进行dbc解析 第一个str为解析的DBC文件路径, 第二个 str 为选择保存的数据库
    singal_statrDbcDecode = Signal(str, str)

    # 发送获取多行选择的结果
    signal_get_seleteRowsData_result = Signal(list)

    # 发送获取选择的一整行的数据，并进行编辑的结果
    signal_get_selectAndEditRowData_result = Signal(dict)

    # 输出提示信息信号
    singal_tipsPrint = Signal(str)
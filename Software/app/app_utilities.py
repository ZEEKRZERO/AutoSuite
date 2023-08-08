
import json,re,struct
from PySide6.QtWidgets import QMessageBox

from PySide6 import QtCore, QtSql
from PySide6.QtSql import QSqlDatabase, QSqlQuery

import datetime

from layers.appDataLay.flexray_config import (config_to_c_struct, map_frame_id_to_tx_msg_buf_idx,nodesend_fr_config,noderecv_fr_config)
from layers.appDataLay.constants import *

cfgParam_connect_filePath = "cfg/connectParam.cfg"
cfgParam_sniffData_filePath = "cfg/sniffDataParam.cfg"

sqlDB_filePath = "data/sniffData.db"
sqlDB_filePath_dbc = "data/dbcData.db"
sqlDB_filePath_fuzzFunc = "data/fuzzFuncData.db"

PacketHeader_fr = b'\xfa\x57'
PacketEnd_fr = b'\x58\xfb'

PacketHeader_can = b'\xfa\x51'
PacketChannel_can = b'\x00'
PacketEnd_can = b'\x52\xfb'
PacketCs_can = b'\x06\x08\x52\x42'

# 工具类函数
class AppUtilitiesClass :


    """
    配置参数加载相关
    """
    # 加载 Json 配置文件
    @staticmethod
    def cfgParam_load(file_path):
        try:
            with open(file_path, "r") as file:
                param = json.load(file)
                return param
        except Exception as e:
            QMessageBox.critical(None, "Error", str(e))
            return None
        
    # 保存Json 配置文件
    @staticmethod
    def cfgParam_save(file_path, paramDict):  
        try:
            with open(file_path, "w") as file:
                json.dump(paramDict, file, indent=4)
        except Exception as e:
            QMessageBox.critical(None, "Error", str(e))


    # 加载Json配置文件   连接配置
    @staticmethod
    def cfgParam_connect_load():
        file_path = cfgParam_connect_filePath
        return AppUtilitiesClass.cfgParam_load(file_path)
        
    # 保存Json配置文件   连接配置
    @staticmethod
    def cfgParam_connect_save(paramDict):  
        file_path = cfgParam_connect_filePath
        AppUtilitiesClass.cfgParam_save(file_path, paramDict)
    

    # 加载Json配置文件   抓取数据配置
    @staticmethod
    def cfgParam_sniffData_load():
        file_path = cfgParam_sniffData_filePath
        return AppUtilitiesClass.cfgParam_load(file_path)
        
    # 保存Json配置文件   抓取数据配置
    @staticmethod
    def cfgParam_sniffData_save(paramDict):  
        file_path = cfgParam_sniffData_filePath
        AppUtilitiesClass.cfgParam_save(file_path, paramDict)

    """
    设备参数相关
    """
    @staticmethod
    def convert_CANpacket2Bytes(packet_data, frame_id):
        Length = len(packet_data)
        canDataBytes = PacketHeader_can + PacketChannel_can + PacketCs_can  + struct.pack('>IB',frame_id,Length) + packet_data + PacketEnd_can
        return canDataBytes
    
    @staticmethod
    def convert_FRpacket2Bytes(msg_type, packet_data, frame_id=0):
        packet_data_len = len(packet_data)
        pkt = struct.pack('>HH', SIZEOF_PACKET_HEADER + packet_data_len, (msg_type << 11) | (frame_id & 0x7FF)) + packet_data
        newpkt = PacketHeader_fr + pkt + PacketEnd_fr

        return newpkt

    @staticmethod
    def device_get_cfgParamBytes(whichNode):
        if whichNode == "NodeSend":
            fr_config = nodesend_fr_config
        elif whichNode == "NodeRecv":
            fr_config = noderecv_fr_config
        else:
            fr_config = nodesend_fr_config
            pass
        
        return AppUtilitiesClass.convert_FRpacket2Bytes(PACKET_TYPE_START_DRIVER, config_to_c_struct(fr_config))
    
    @staticmethod
    def get_device_frConfig():
        whichNode = AppUtilitiesClass.cfgParam_connect_load()["FRCfg"]["NODE"]
        if whichNode == "Node1":
            return nodesend_fr_config
        elif whichNode == "Node2":
            return noderecv_fr_config
        else:
            return nodesend_fr_config
    
    @staticmethod
    def device_get_healthChkBytes():
        return AppUtilitiesClass.convert_FRpacket2Bytes(PACKET_TYPE_HEALTH, b'')



    """
    数据库操作相关
    """
    # 连接数据库
    @staticmethod
    def sqlDB_connect(whichDb = "sniffDataDB"):
        db = QSqlDatabase.addDatabase("QSQLITE", "defalut_connect")
        if whichDb == "sniffDataDB":
            db.setDatabaseName(sqlDB_filePath)
        elif whichDb == "dbcDataDB":
            db.setDatabaseName(sqlDB_filePath_dbc)
        elif whichDb == "fuzzFuncDB":
            db.setDatabaseName(sqlDB_filePath_fuzzFunc)
        else:
            return None
        try:
            db.open()
            return db
        except:
            return None
        

    # 关闭数据库连接
    @staticmethod
    def sqlDB_disconnect(db):
        db.close()
        
            

    # 往数据库插入数据
    @staticmethod
    def sqlDB_insert_sniffData(db, tableName, data_dict):

        if db is None:
            return
        if not data_dict:
            return
        
        # 查询表是否存在
        query = QtSql.QSqlQuery(db)

        # 如果表不存在，则创建表
        create_table_query = f"CREATE TABLE IF NOT EXISTS {tableName} (No INTEGER PRIMARY KEY, \
                                                                        busType TEXT, \
                                                                        channel TEXT, \
                                                                        receiveTime TEXT, \
                                                                        frameID TEXT, \
                                                                        frameType TEXT, \
                                                                        dataLength TEXT, \
                                                                        data TEXT, \
                                                                        timestamp TEXT)"
        query.exec(create_table_query)
       
        # 往表当中插入数据
        insert_string = f"INSERT INTO {tableName} (busType, channel, receiveTime, frameID, frameType, dataLength, data, timestamp) \
                          VALUES (:busType, :channel, :receiveTime, :frameID, :frameType, :dataLength, :data, :timestamp)"

        query.prepare(insert_string)
        query.bindValue(":busType", data_dict["busType"])
        query.bindValue(":channel", data_dict["channel"])
        query.bindValue(":receiveTime", data_dict["receiveTime"])
        query.bindValue(":frameID", data_dict["frameID"])
        query.bindValue(":frameType", data_dict["frameType"])
        query.bindValue(":dataLength", data_dict["dataLength"])
        query.bindValue(":data", data_dict["data"])
        query.bindValue(":timestamp", data_dict["timestamp"])

        query.exec()

    # 往数据库插入数据
    @staticmethod
    def sqlDB_insert_dbcDecodeData(db, tableName, data_dict):

        if db is None:
            return
        
        # 查询表是否存在
        query = QtSql.QSqlQuery(db)

        # 如果表不存在，则创建表
        create_table_query = f"CREATE TABLE IF NOT EXISTS {tableName} ( signal_name TEXT PRIMARY KEY, \
                                                                        frame_id TEXT,\
                                                                        start_bit TEXT,\
                                                                        len_bit TEXT,\
                                                                        byte_order TEXT)"
        query.exec(create_table_query)

        # 往表当中插入数据
        query.prepare(f"SELECT * FROM {tableName} WHERE signal_name = :signal_name")
        query.bindValue(":signal_name", data_dict["signal_name"]) 
        query.exec()
        if query.first():
            # 表中存在这个信号，进行更新
            insertOrUpdate_string = f"UPDATE {tableName}  SET \
                        signal_name = :signal_name, \
                        frame_id = :frame_id, \
                        start_bit = :start_bit, \
                        len_bit = :len_bit,\
                        byte_order = :byte_order \
                        WHERE signal_name = :signal_name"     
        else:
            insertOrUpdate_string = f"INSERT INTO {tableName} (signal_name, frame_id, start_bit, len_bit, byte_order) \
                VALUES (:signal_name, :frame_id, :start_bit, :len_bit, :byte_order)"
        
        query.prepare(insertOrUpdate_string)
        query.bindValue(":signal_name", data_dict["signal_name"])
        query.bindValue(":frame_id", data_dict["frame_id"])
        query.bindValue(":start_bit", data_dict["start_bit"])
        query.bindValue(":len_bit", data_dict["len_bit"])
        query.bindValue(":byte_order", data_dict["byte_order"])

        query.exec()

    # 往数据库插入数据
    @staticmethod
    def sqlDB_insert_fuzzFuncData(db, tableName, data_dict):

        if db is None:
            return
        
        # 查询表是否存在
        query = QtSql.QSqlQuery(db)

        # 如果表不存在，则创建表
        create_table_query = f"CREATE TABLE IF NOT EXISTS {tableName} ( name TEXT, \
                                                                        signal_name TEXT PRIMARY KEY, \
                                                                        frame_id TEXT,\
                                                                        start_bit TEXT,\
                                                                        len_bit TEXT,\
                                                                        byte_order TEXT,\
                                                                        UB TEXT)"
        query.exec(create_table_query)

        # 往表当中插入数据
        query.prepare(f"SELECT * FROM {tableName} WHERE signal_name = :signal_name")
        query.bindValue(":signal_name", data_dict["signal_name"]) 
        query.exec()
        if query.first():
            # 表中存在这个信号，进行更新
            insertOrUpdate_string = f"UPDATE {tableName}  SET \
                        name = : name, \
                        signal_name = :signal_name, \
                        frame_id = :frame_id, \
                        start_bit = :start_bit, \
                        len_bit = :len_bit,\
                        byte_order = :byte_order, \
                        UB = :UB \
                        WHERE signal_name = :signal_name"     
        else:
            insertOrUpdate_string = f"INSERT INTO {tableName} (name, signal_name, frame_id, start_bit, len_bit, byte_order, UB) \
                VALUES (:name, :signal_name, :frame_id, :start_bit, :len_bit, :byte_order, :UB)"
        
        query.prepare(insertOrUpdate_string)
        query.bindValue(":name", data_dict["name"])
        query.bindValue(":signal_name", data_dict["signal_name"])
        query.bindValue(":frame_id", data_dict["frame_id"])
        query.bindValue(":start_bit", data_dict["start_bit"])
        query.bindValue(":len_bit", data_dict["len_bit"])
        query.bindValue(":byte_order", data_dict["byte_order"])
        query.bindValue(":UB", data_dict["UB"])

        query.exec()



    
    # 删除数据库当中的某张表
    @staticmethod
    def sqlDB_delete_table(db, tableName):
        if db is None:
            return
        
        # 删除表
        query = QSqlQuery(db)
        query.exec(f"DROP TABLE {tableName}")

        # 关闭数据库连接
        AppUtilitiesClass.sqlDB_disconnect(db)


    # 往数据库插入数据示例
    @staticmethod
    def sqlDB_insert_sniffData_example(tableName):

        data_dict = {
            "channel" : "1",
            "receiveTime" : "",
            "busType" : "can",
            "frameID" : "",
            "frameType" : "data",
            "dataLength" : "8",
            "data" : "",
            "timestamp" : ""
        }
        # 连接数据库
        db = AppUtilitiesClass.sqlDB_connect("sniffDataDB")

        for i in range(1000):
            data_dict ["receiveTime"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data_dict ["frameID"] = hex(i)[2:]
            data_dict ["data"] = "1122334455667788"
            data_dict ["timestamp"] = str(i)
            if i % 100 == 0 :
                data_dict ["channel"] = str(i / 100)

            # 插入数据
            AppUtilitiesClass.sqlDB_insert_sniffData(db, tableName, data_dict)

        # 关闭数据库连接
        AppUtilitiesClass.sqlDB_disconnect(db)

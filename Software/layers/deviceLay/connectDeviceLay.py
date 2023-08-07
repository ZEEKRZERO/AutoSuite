# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass

from PySide6.QtNetwork import QTcpSocket,QAbstractSocket
from PySide6.QtCore import Signal, Slot
from PySide6.QtCore import QTimer

from abc import abstractmethod
import hid
import serial

from layers.threadObj_base import ThreadObj_base

from app.app_utilities import AppUtilitiesClass


"""
    物理层，线程对象类
"""

# 物理层，物理设备连接对象类
class ThreadObj_IODevice_base(ThreadObj_base):
    def __init__(self):
        super().__init__()

        self.connectDeviceParamDict = {}  # 设备连接参数字典

    # 连接设备
    @abstractmethod
    @Slot()
    def devices_open_slot(self):
        pass

    # 关闭设备
    @abstractmethod
    @Slot()
    def devices_close_slot(self):
        pass

    # 设置连接设备参数
    @abstractmethod
    @Slot()
    def devices_setConnectParam_slot(self, param):
        pass

    # 发送字节流数据
    @abstractmethod
    @Slot()
    def devices_sendByteArrays_slot(self, byteArrays):
        pass

    # 接收字节流数据，需要返回收到的字节流数据
    @abstractmethod
    @Slot()
    def devices_readByteArrays_slot(self):
        pass

    @abstractmethod
    @Slot()
    def devices_connectStatus_slot(self):
        pass


# 物理层，WIFI设备
class ThreadObj_IODevice_WIFI(ThreadObj_IODevice_base):
    def __init__(self, connectParam):
        super().__init__()

        self.connectDeviceParamDict = connectParam

    # 连接设备
    def devices_open_slot(self):
        self.socket = QTcpSocket()
        self.socket.connectToHost(self.connectDeviceParamDict["IP"], int(self.connectDeviceParamDict["PORT"]))
        return self.socket.waitForConnected(500)


    # 关闭设备
    def devices_close_slot(self):
        self.socket.close()


    # 设置连接设备参数
    def devices_setConnectParam_slot(self, param):
        self.connectDeviceParamDict["IP"] = param["IP"]
        self.connectDeviceParamDict["PORT"] = param["PORT"]

    # 发送字节流数据， 返回是否发送成功
    def devices_sendByteArrays_slot(self, byteArrays):
        bytes_written = -1
        if self.socket.isValid():
            bytes_written = self.socket.write(byteArrays)
        
        if bytes_written == -1:
            return False
        else:
            return True

    # 接收字节流数据，需要返回收到的字节流数据
    def devices_readByteArrays_slot(self):
        if self.socket.isValid():
            return self.socket.readAll()
        else:
            return None
        
    def devices_connectStatus_slot(self):
        if self.socket.state() == QAbstractSocket.ConnectedState :
            return True
        else:
            return False
        


# 物理层，USB HID设备
class ThreadObj_IODevice_USBHid(ThreadObj_IODevice_base):
    def __init__(self, connectParam):
        super().__init__()

        self.connectDeviceParamDict = connectParam
        self.dev = None

    # 连接设备
    def devices_open_slot(self):
        # self.dev = hid.device(self.connectDeviceParamDict["VID"], self.connectDeviceParamDict["PID"])
        self.dev = hid.device(vendor_id=0x0808, product_id=0x8081)
        # dev = usb.core.find(idVendor=0x0000, idProduct=0x0000)

        # self.dev = hid.
        print(self.dev)
        if self.dev is not None:
            try:
                self.dev.open()
#                manufacturer = self.dev.get_manufacturer_string()
#                product = self.dev.get_product_string()
#                serial_number = self.dev.get_serial_number_string()
            except Exception as e:
                print(e)


            # print("Manufacturer:", manufacturer)
            # print("Product:", product)
            # print("Serial Number:", serial_number)
            return True
        else:
            return False

    # 关闭设备
    def devices_close_slot(self):
        self.dev.close()

    # 设置连接设备参数
    def devices_setConnectParam_slot(self, param):
        self.connectDeviceParamDict["VID"] = param["VID"]
        self.connectDeviceParamDict["PID"] = param["PID"]

    # 发送字节流数据
    def devices_sendByteArrays_slot(self, byteArrays):
        if self.dev is not None:
            self.dev.write(byteArrays)


    # 接收字节流数据，需要返回收到的字节流数据
    def devices_readByteArrays_slot(self):
        if self.dev is not None:
            return self.dev.read(64)
        else:
            return None


# 物理层，uart 设备
class ThreadObj_IODevice_UART(ThreadObj_IODevice_base):
    def __init__(self, connectParam):
        super().__init__()

        self.serialDev = None
        self.devices_setConnectParam_slot(connectParam)

    # 连接设备
    def devices_open_slot(self):
        try:
            self.serialDev = serial.Serial(self.connectDeviceParamDict["com"], int(self.connectDeviceParamDict["baudRate"]), timeout=1)
            return True
        except serial.SerialException:
            return False


    # 关闭设备
    def devices_close_slot(self):
        if self.serialDev is None:
            return

        self.serialDev.close()

    # 设置连接设备参数
    def devices_setConnectParam_slot(self, param):
        self.connectDeviceParamDict = param

    # 发送字节流数据
    def devices_sendByteArrays_slot(self, byteArrays):
        self.serialDev.write(byteArrays)


    # 接收字节流数据，需要返回收到的字节流数据
    def devices_readByteArrays_slot(self):
        return self.serialDev.read_all()


# 物理层，设备管理类
class ThreadObj_IOManage(ThreadObj_base):

    def __init__(self, connectParam):
        super().__init__()

        self.deivceObj  = None

        # 默认连接参数字典
        self.connectParamDict = {
            "connectMode" : "WIFI",
            "USB" : {
                "VID" : "0808",
                "PID" : "8081",
            },
            "WIFI" : {
                "IP" : "192.168.0.1",
                "PORT": "3333",
            },
            "UART" : {
                "com" : "com3",
                "baudRate" : "115200",
                "dataBits" : "8",
                "parity" : "0",
                "stopBits" : "1",
            }
        }
        # 定时读取数据
        self.timerisCreated_toReadData = False


        # 定时发送心跳包
        self.timerisCreated_toSendHealthClk = False


        # 加载设备连接参数
        self.connectParamDict = AppUtilitiesClass.cfgParam_connect_load()

        # 设备的连接状态， True 表示连接成功
        self.connectStatus = False



    # 连接设备
    @Slot()
    def devices_open_slot(self):

        # 定时读取数据
        if self.timerisCreated_toReadData == False:
            self.timerisCreated_toReadData = True
            self.timer_toReadData = QTimer()
            self.timer_toReadData.setInterval(20)   # 每20ms去读取数据
            self.timer_toReadData.timeout.connect(self.devices_readByteArrays_slot)
            self.destroyed.connect(self.timer_toReadData.deleteLater)

        if self.timerisCreated_toSendHealthClk == False:
            self.timerisCreated_toSendHealthClk = True
            self.timer_toSendHealthClk = QTimer()
            self.timer_toSendHealthClk.setInterval(1000)   
            self.timer_toSendHealthClk.timeout.connect(self.devices_send_healthClk_slot)
            self.destroyed.connect(self.timer_toSendHealthClk.deleteLater)

        result = False
        self.singal_tipsPrint.emit(f"The currently selected device connection mode is:{self.connectParamDict['connectMode']}")
        self.singal_tipsPrint.emit("Device connecting...")

        if self.connectParamDict["connectMode"] == "WIFI":
            self.deivceObj = ThreadObj_IODevice_WIFI(self.connectParamDict["WIFI"])
        elif self.connectParamDict["connectMode"] == "USB":
            self.deivceObj = ThreadObj_IODevice_USBHid(self.connectParamDict["USB"])
        elif self.connectParamDict["connectMode"] == "UART":
            self.deivceObj = ThreadObj_IODevice_UART(self.connectParamDict["UART"])

        result = self.deivceObj.devices_open_slot()
        if result:
            self.connectStatus = True
            self.timer_toReadData.start()
            self.singal_tipsPrint.emit("Device connected!")

            # 发送设备配置文件给设备
            cfgParamBytes = AppUtilitiesClass.device_get_cfgParamBytes(self.connectParamDict["FRCfg"]["NODE"])
            self.devices_sendByteArrays_slot(cfgParamBytes)

            # 定时发送心跳包
            self.timer_toSendHealthClk.start()
        else :
            self.connectStatus = False
            self.timer_toReadData.stop()
            self.timer_toSendHealthClk.stop()
            self.singal_tipsPrint.emit("Device connect failed!")
            self.signal_devices_info_disconnect.emit()

        self.signal_devices_info_connectState.emit(result)


    # 关闭设备
    @Slot()
    def devices_close_slot(self):
        if self.deivceObj is None :
            self.signal_devices_info_disconnect.emit()
            return    
        
        # 定时读取数据
        if self.timerisCreated_toReadData == False:
            self.timerisCreated_toReadData = True
            self.timer_toReadData = QTimer()
            self.timer_toReadData.setInterval(20)   # 每20ms去读取数据
            self.timer_toReadData.timeout.connect(self.devices_readByteArrays_slot)
            self.destroyed.connect(lambda:(
                self.timer_toReadData.stop(),
                self.timer_toReadData.deleteLater()
            ))

        if self.timerisCreated_toSendHealthClk == False:
            self.timerisCreated_toSendHealthClk = True
            self.timer_toSendHealthClk = QTimer()
            self.timer_toSendHealthClk.setInterval(1000)   
            self.timer_toSendHealthClk.timeout.connect(self.devices_send_healthClk_slot)
            self.destroyed.connect(lambda:(
                self.timer_toSendHealthClk.stop(),
                self.timer_toSendHealthClk.deleteLater()
            ))
        self.singal_tipsPrint.emit("Connection closing....")
        self.timer_toReadData.stop()
        self.timer_toSendHealthClk.stop()
        self.deivceObj.devices_close_slot()
        self.singal_tipsPrint.emit("disconnected")
        self.signal_devices_info_disconnect.emit()
        self.deivceObj = None
        self.connectStatus = False



    # 更新设备连接参数
    @Slot(dict)
    def devices_updateConnectParam_slot(self):

        # 关闭设备
        self.devices_close_slot()
        # 更新加载参数
        self.connectParamDict = AppUtilitiesClass.cfgParam_connect_load()
        self.singal_tipsPrint.emit("Device connection parameters have been updated")

    # 发送字节流数据
    @Slot(bytes)
    def devices_sendByteArrays_slot(self, byteArrays):
        
        if self.deivceObj is None or self.connectStatus == False:
            # 提示设备未连接, 尝试进行连接
            self.devices_open_slot()
            return
        
        status = self.deivceObj.devices_sendByteArrays_slot(byteArrays)
        if status == False:
            # 发送失败，设备连接断开
            self.devices_close_slot()

    # 接收字节流数据，需要返回收到的字节流数据
    @Slot()
    def devices_readByteArrays_slot(self):
        if self.deivceObj is None:
            return
        data = self.deivceObj.devices_readByteArrays_slot()
        if len(data) > 0:
            self.signal_devices_readData.emit(data)

    @Slot()
    def devices_connectStatus_slot(self):
        print("get result")
        result =  self.deivceObj.devices_connectStatus_slot()
        print("connect status",result)
        self.signal_devices_info_connectState.emit(result)

    @Slot()
    def devices_send_healthClk_slot(self):
        # 获取心跳包字节流
        healthClkBytes = AppUtilitiesClass.device_get_healthChkBytes()
        self.devices_sendByteArrays_slot(healthClkBytes)


    # 连接状态信号，参数表示是否成功连接
    signal_devices_info_connectState = Signal(bool)

    # 关闭设备完成信号
    signal_devices_info_disconnect = Signal()

    # 读取数据信号
    signal_devices_readData = Signal(bytes)















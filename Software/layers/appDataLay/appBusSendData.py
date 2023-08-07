from layers.appDataLay.flexray_config import (config_to_c_struct, map_frame_id_to_tx_msg_buf_idx)
from layers.appDataLay.constants import *
from app.app_utilities import AppUtilitiesClass
from PySide6.QtCore import Signal, Slot, QTimer
from layers.threadObj_base import ThreadObj_base


class ThreadObj_App_busSendData(ThreadObj_base):
    def __init__(self):
        super().__init__()
        self.fr_config = AppUtilitiesClass.get_device_frConfig()
        self.frame_id_to_tx_msg_buf_idx = map_frame_id_to_tx_msg_buf_idx(self.fr_config)
        
    @Slot(list)
    def packAndSendBusData_slot(self,data_list):

        for data in data_list:
            busType = data['busType']
            if busType == 'Can':
                self.canBusSendData(data)
            elif busType == 'FlexRay':
                self.frBusSendData(data)
            elif busType == 'Lin':
                self.linBusSendData(data)
            else:
                print("not define bus type")
            
            # 发送到物理层任务完成
            self.signal_busSendDataComplete.emit()


    def canBusSendData(self, data):
        print("can data", data)
        # get data
        frame_id = int(data["FrameID"],16)
        Length = int(data['Length'],10)
        payload = bytes.fromhex(data['Data'])
        # check length
        if Length > len(payload):
            payload += b'\x00' * (Length - len(payload))
        elif Length < len(payload):
            payload = payload[:Length]
        # pack data
        canDataBytes = AppUtilitiesClass.convert_CANpacket2Bytes(payload, frame_id)
        self.signal_busSendData.emit(canDataBytes)


    def frBusSendData(self,data):
        # get data
        print("fr data", data)
        frame_id = int(data["FrameID"],16)
        Length = int(data['Length'],10)
        payload = bytes.fromhex(data['Data'])
        # check length
        if Length > len(payload):
            payload += b'\x00' * (Length - len(payload))
        elif Length < len(payload):
            payload = payload[:Length]
        # pack data
        self.send_FRframe(frame_id, payload)


    def linBusSendData(self,dataList):
        pass


    def send_FRframe(self, frame_id, payload):
        print("send frame",frame_id)
        print(self.frame_id_to_tx_msg_buf_idx)
        if len(payload) == 0:
            return 0
        if frame_id not in self.frame_id_to_tx_msg_buf_idx:
            print("error1")
            return 0
        msg_buf_idx = self.frame_id_to_tx_msg_buf_idx[frame_id]
        if self.fr_config['TxMsgBufs'][msg_buf_idx]['FrameId'] > self.fr_config['gNumberOfStaticSlots']:
            if len(payload) > self.fr_config['pPayloadLengthDynMax'] * 2:
                # Truncate the byte string
                payload = payload[0:(self.fr_config['pPayloadLengthDynMax'] * 2)]
        else:
            if len(payload) < self.fr_config['gPayloadLengthStatic'] * 2:
                # padding with zero
                payload = payload.ljust(self.fr_config['gPayloadLengthStatic'] * 2, b'\0')
            elif len(payload) > self.fr_config['gPayloadLengthStatic'] * 2:
                # Truncate the byte string
                payload = payload[0:(self.fr_config['gPayloadLengthStatic'] * 2)]
        frFrameBytes = AppUtilitiesClass.convert_FRpacket2Bytes(PACKET_TYPE_FLEXRAY_FRAME, payload, frame_id=msg_buf_idx)
        self.signal_busSendData.emit(frFrameBytes)
        print("payload",payload)
        print("frameid",msg_buf_idx)


    signal_busSendData = Signal(bytes)

    # 信号，通知已经完成数据发送到物理层
    signal_busSendDataComplete = Signal()
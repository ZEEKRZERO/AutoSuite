import socket,subprocess,re
import struct
import threading
import datetime
from select import select
from layers.appDataLay.flexray_config import (config_to_c_struct, map_frame_id_to_tx_msg_buf_idx,default_fr_config)
from layers.appDataLay.constants import *
from app.app_utilities import AppUtilitiesClass
from PySide6.QtCore import Signal, Slot, QTimer
from layers.threadObj_base import ThreadObj_base




frheader = b'\xfa\x57'
frend = b'\x58\xfb'


class ThreadObj_App_busReslove(ThreadObj_base):
    def __init__(self):
        super().__init__()

        self.fr_config = default_fr_config
        self.frame_id_to_tx_msg_buf_idx = map_frame_id_to_tx_msg_buf_idx(self.fr_config)

        self.read_buf = b''
        self.sta = 0
        self.decoded_dict = {
            "channel" : "1",
            "receiveTime" : "",
            "busType" : "can",
            "frameID" : "",
            "frameType" : "data",
            "dataLength" : "8",
            "data" : "",
            "timestamp" : ""
        }      

        self.suspendDecodeBusData = False
        self.suspendSaveData2DB = False

    @Slot(bytes)  
    def receive_packet_slot(self,byteArrys):
        if self.suspendDecodeBusData:
            return
        
        self.can_receiver(byteArrys)
        self.lin_receiver(byteArrys)
        self.fr_receiver(byteArrys)

    # recive all data on CAN bus
    def can_receiver(self,bytearrys):
        db = AppUtilitiesClass.sqlDB_connect()

        # message = conn.receive_packet()
        pattern1 =re.compile(b'\xfaQ.+?R\xfb') 
        matches = pattern1.findall(bytearrys)
        for match in matches:
            decoded_dict = self.CANDecode(match)

            if decoded_dict :
                if self.suspendSaveData2DB == False:
                    AppUtilitiesClass.sqlDB_insert_sniffData(db,"sniffData",decoded_dict)
                self.signal_busDataDecodedReslut.emit(decoded_dict)


        AppUtilitiesClass.sqlDB_disconnect(db)
        

    def CANDecode(self,data):
        decoded_dict = {}

        # print("can data decoding")
        timeNow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # print("can data len",len(data))
        if len(data) == 22:
            heade,chn,cs,cmdid,paylen = struct.unpack('>HBIIB',data[:(len(data)-10)])
            payload = data[(len(data)-10):(len(data)-10+paylen)]


            decoded_dict["channel"] = str(chn)
            decoded_dict["receiveTime"] = timeNow
            decoded_dict["busType"] = "can"
            decoded_dict["frameID"] = hex(cmdid)
            decoded_dict["frameType"] = "data"
            decoded_dict["dataLength"] = str(paylen)
            decoded_dict["data"] = payload.hex()
            decoded_dict["timestamp"] = timeNow
            # print(decoded_dict)

        return decoded_dict


    # recive all data on CAN bus
    def lin_receiver(self,bytearrys):
        db = AppUtilitiesClass.sqlDB_connect()

        pattern =re.compile(b'\xfa\x53.*?\x54\xfb')
        matches = pattern.findall(bytearrys)
        for match in matches:
            if len(match) > 6:
                decoded_dict = self.LINDecode(match)

                if decoded_dict :
                    if self.suspendSaveData2DB == False:
                        AppUtilitiesClass.sqlDB_insert_sniffData(db,"sniffData",decoded_dict)
                    self.signal_busDataDecodedReslut.emit(decoded_dict)


        AppUtilitiesClass.sqlDB_disconnect(db)
        
    def LINDecode(self,data):
        decoded_dict = {}

        #print("lin data decoding")
        timeNow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        data = data[3:(len(data)-3)] # drop the header and end

        cmdid = data[0]&0x3f #the max lin id is 0x3f
        payload = data[1:]

        # print("LIN id",hex(cmdid))
        # print("LIN data",payload.hex())
        # print("LIN data len",len(payload))
        if len(payload)>8:
            print("error msg!!!!!!!!!!!!!")
    
        else:
            decoded_dict["channel"] = str(1)
            decoded_dict["receiveTime"] = timeNow
            decoded_dict["busType"] = "lin"
            decoded_dict["frameID"] = hex(cmdid)
            decoded_dict["frameType"] = "data"
            decoded_dict["dataLength"] = str(len(payload))
            decoded_dict["data"] = payload.hex()
            decoded_dict["timestamp"] = timeNow

        return self.decoded



    def fr_receiver (self,bytearrys):
        db = AppUtilitiesClass.sqlDB_connect()

        pattern = re.compile(b'\xfa\x57.+?\x58\xfb')
        matches = pattern.findall(bytearrys)
        for match in matches:
            # print("FR match",match.hex())
            # print("FR length",len(match))

            if(len(match)>32):
                decoded_dict = self.FRDecode(match)
                if decoded_dict :
                    if self.suspendSaveData2DB == False:
                        AppUtilitiesClass.sqlDB_insert_sniffData(db,"sniffData",decoded_dict)
                    self.signal_busDataDecodedReslut.emit(decoded_dict)

        AppUtilitiesClass.sqlDB_disconnect(db)
        

    def FRDecode(self,data):
        decoded_dict = {}

        # print("FR data decoding")
        timeNow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if len(data) > 40:
            data = data[2:(len(data)-2)]
            # print("cuted data",data.hex())
            header = struct.unpack('>HH', data[0:SIZEOF_PACKET_HEADER])
            payload_length = header[0] - SIZEOF_PACKET_HEADER
            if SIZEOF_PACKET_HEADER + payload_length == len(data):
                print("fr test1")
                # tuple: (packet type, packet payload)
                pkt_type = header[1] >> 11
                if pkt_type == PACKET_TYPE_FLEXRAY_FRAME:
                    print("fr test2")

                    frameid = header[1] & 0x07ff
                    payload = data[SIZEOF_PACKET_HEADER:]
                        
                    # print("FR ID",frameid)
                    # print("FR data",payload)
                # decoded = {'devId':str(1),'cmdId':0x00,'time':1,'len':8,'payload':'0','chn':str(1),'bus':1}
                    decoded_dict["channel"] = str(1)
                    decoded_dict["receiveTime"] = timeNow
                    decoded_dict["busType"] = "flexray"
                    decoded_dict["frameID"] = hex(frameid)
                    decoded_dict["frameType"] = "data"
                    decoded_dict["dataLength"] = str(len(payload))
                    decoded_dict["data"] = payload.hex()
                    decoded_dict["timestamp"] = timeNow
                    # print(decoded_dict)
                
            return decoded_dict      


    def send_packet(self, msg_type, packet_data, frame_id=0):
        packet_data_len = len(packet_data)
        pkt = struct.pack('>HH', SIZEOF_PACKET_HEADER + packet_data_len, (msg_type << 11) | (frame_id & 0x7FF)) + packet_data
        newpkt = frheader + pkt + frend
    

            
        self.signal_sendBytes.emit(newpkt)

     



    @staticmethod
    def parse_fr_frame_packet(payload):
        if len(payload) <= SIZEOF_UINT16:
            raise RuntimeError("parse_fr_frame_packet, payload len error: {}".format(len(payload)))
        frame_payload_len = len(payload) - SIZEOF_UINT16
        t = struct.unpack('>H{}B'.format(frame_payload_len), payload)
        return t[0], t[1:]

    @staticmethod
    def parse_health_packet(payload):
        if len(payload) == 0:
            return None
        if len(payload) % SIZEOF_UINT16 != 0:
            raise RuntimeError("Invalid payload len for health packet: {}".format(len(payload)))
        reg_vals = 6
        corrections = 4
        if len(payload) // SIZEOF_UINT16 < (reg_vals + corrections):
            raise RuntimeError("Invalid payload len for health packet: {}".format(len(payload)))
        t = struct.unpack('>{}H{}h{}h'.format(reg_vals, corrections, len(payload) // SIZEOF_UINT16 - reg_vals - corrections), payload)
        a_even_cnt = (t[5] & 0x0F00) >> 8
        b_even_cnt = (t[5] & 0xF000) >> 12
        a_odd_cnt = t[5] & 0x000F
        b_odd_cnt = (t[5] & 0x00F0) >> 4
        # PSR0, PSR1, PSR2, PSR3, PIFR0,
        # max_rate_correction, max_offset_correction, min_rate_correction, min_offset_correction,
        # a_even_cnt, b_even_cnt, a_even_cnt, a_even_cnt, sync frame table
        return t[0], t[1], t[2], t[3], t[4], t[6], t[7], t[8], t[9], a_even_cnt, b_even_cnt, a_odd_cnt, b_odd_cnt, t[10:]

    def send_frame(self, frame_id, payload):
        print("send frame")
        if len(payload) == 0:
            return 0
        if frame_id not in self.frame_id_to_tx_msg_buf_idx:
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
        self.send_packet(PACKET_TYPE_FLEXRAY_FRAME, payload, frame_id=msg_buf_idx)
        print("payload",payload)
        print("frameid",msg_buf_idx)
        return len(payload)
    
    
    signal_sendBytes = Signal(bytes)

    signal_busDataDecodedReslut = Signal(dict)

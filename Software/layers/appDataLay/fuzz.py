from app.app_utilities import AppUtilitiesClass
from PySide6.QtCore import Signal, Slot, QTimer
from layers.threadObj_base import ThreadObj_base
import random,struct
        


class ThreadObj_App_fuzz(ThreadObj_base):

    def __init__(self):
        super().__init__()
        self.canHeader = b'\xfa\x51'
        self.canChn = b'\x00'
        self.canEnd = b'\x52\xfb'
        self.canCs = b'\x06\x08\x52\x42'
        # CAN数据包定义
        self.CAN_PACKET = bytearray([0x00]*8)

        # CAN数据包的总位数
        self.CAN_PACKET_SIZE = 64

        # 随机翻转位的概率
        self.FLIP_PROBABILITY = 0.5

    @Slot(list)
    def fuzz_slot(self,funclist):
        for func in funclist:
            frame_id = int(func["frame_id"],16)
            start_bit = int(func["start_bit"],10)
            length = int(func["len_bit"],10)
            byte_order = func["byte_order"]
            ub = func["UB"]
            fuzzed_bytes = self.afl_template_fuzz(self.CAN_PACKET,start_bit,length,byte_order)
            if ub:
                ub = int(ub,10)
                fuzzed_bytes = bytearray(fuzzed_bytes)
                fuzzed_bytes[ub//8] |= 1 << (ub%8)  # set ub
            fuzzed_bytes = bytes(fuzzed_bytes)

            can_msg = self.canHeader+ self.canChn + self.canCs + struct.pack('>IB',frame_id,len(fuzzed_bytes)) + fuzzed_bytes + self.canEnd
            self.signal_fuzzData.emit(can_msg)

    # 将CAN数据格式化为二进制串
    def format_can_data(self,can_data):
        binary_string = ''
        for byte in can_data:
            binary_string += format(byte, '08b')
        return binary_string

    # 随机翻转指定位置的位
    def fuzz_can_data(self,start_bit, length, binary_string,byte_order):
        binary_list = list(binary_string)
        flipped_bits = set()
        if byte_order == "big_endian":
            for i in range(start_bit, start_bit+length):
                if random.random() < self.FLIP_PROBABILITY:
                    binary_list[i] = '1' if binary_list[i] == '0' else '0'
                    flipped_bits.add(i)
        else:
            for i in range(start_bit, start_bit+length):
                if random.random() < self.FLIP_PROBABILITY:
                    binary_list[i] = '1' if binary_list[i] == '0' else '0'
                    flipped_bits.add(i)   
                    
        return ''.join(binary_list), flipped_bits

    # AFL模板fuzz
    def afl_template_fuzz(self,input_bytes,START_BIT,LENGTH,byte_order):
        binary_string = self.format_can_data(input_bytes)
        fuzzed_binary_string, flipped_bits = self.fuzz_can_data(START_BIT, LENGTH, binary_string,byte_order)
    
        return bytes(int(fuzzed_binary_string[i:i+8], 2) for i in range(0, len(fuzzed_binary_string), 8))


    signal_fuzzData = Signal(bytes)


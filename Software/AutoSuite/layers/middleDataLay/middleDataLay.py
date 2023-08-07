# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass





from PySide6.QtCore import Signal, Slot

from layers.threadObj_base import ThreadObj_base

import binascii


"""
    中间数据层，线程对象类
"""


class ThreadObj_MiddleData(ThreadObj_base):
    def __init__(self):
        super().__init__()

        self.isDisplay_hex = True
        self.isDisplay_rawData_suspend = False

        self.bytePool = bytes()

    # 接收物理层设备数据的槽
    @Slot(bytes)
    def receive_raw_data_slot(self, byteArrays):

        if len(byteArrays) == 0 :
            return

        self.bytePool += byteArrays

        if self.isDisplay_rawData_suspend is not False :
            string = ""
            if self.isDisplay_hex:
                string = string + ' '.join([byte.hex().upper() for byte in byteArrays])
            else:
                string = string + byteArrays.data().decode('latin-1')

            if string :
                self.signal_ui_flash_raw_data.emit(string, False)
                

        # 发送数据给应用层

        pass

    @Slot(bool)
    def set_isDisplay_hex_slot(self, isHex):
        self.isDisplay_hex = not isHex


    @Slot(bool)
    def set_isDisplay_Suspend_slot(self, isSuspend):
        self.isDisplay_rawData_suspend = not isSuspend
        print(self.isDisplay_rawData_suspend)



    # 通知界面刷新原始数据信号, str表示要显示的数据， bool类型变量表示是否清除显示
    signal_ui_flash_raw_data = Signal(str, bool)


    



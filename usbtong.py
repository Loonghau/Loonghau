# -*- coding: utf-8 -*-
""" 
@Time : 2021/4/13 16:45
@Author : Loonghau XU
@FileName: usbtong.py
@SoftWare: PyCharm
"""
import usb.util

# find our device
dev = usb.core.find(idVendor=0x0C2E, idProduct=0x0B61)
print(dev)
# was it found?
if dev is None:
    raise ValueError('Device not found')

# dev.set_configuration()
#myinput = bytes([0X16, 0X54, 0X0D])  # 需要发送"S"
#dev.write(myinput)  # 用write函数向串口发送数据

def rx_loop():
    while (True):
        try:
            data = dev.read(0x86, 512, 1000)  # read(endpoint, size_or_buffer, timeout = None)
            print(data)
        except Exception as e:
            print(e)

def tx_loop():
    while (True):
        try:
            data = dev.write(0x88, 0x55, 1000)  # write(endpoint, data, timeout = None)
            print(data)
        except Exception as e:
            print(e)

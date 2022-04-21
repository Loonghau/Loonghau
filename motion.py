# -*- coding: utf-8 -*-
""" 
@Time : 2021/3/17 8:53
@Author : Loonghau XU
@FileName: motion.py
@SoftWare: PyCharm
"""
import serial
import serial.tools.list_ports

from zmcwrapper import ZMCWrapper

zmc = ZMCWrapper()


class Action:
    def qrcode(self):
        y = serial.Serial('com14', 115200, timeout=1)
        myinput = bytes([0X16, 0X54, 0X0D])  # 需要发送"S"
        y.write(myinput)  # 用write函数向串口发送数据
        try:
            myout = y.read(13)  # 提取接收缓冲区中的前7个字节数
            ban = int(myout)
            print(ban)
            y.close()
        except:
            ban="请收到输入"
            print(ban)
            y.close()
        return ban

    def weight(self):
        y = serial.Serial('com11', 9600, timeout=1)
        myinput = bytes([0X53, 0X0A, 0X0D])  # 需要发送"S"
        y.write(myinput)  # 用write函数向串口发送数据
        myout1 = y.read(25)  # 提取接收缓冲区中的前7个字节数
        ban = str(myout1[6:14], encoding='utf-8')
        print(ban)
        y.close()

    def tem_hum(self):
        x = serial.Serial('com13', 2400, timeout=1)
        myinput = bytes([0X53, 0X30, 0X31, 0X39, 0X39, 0X41])  # 需要发送的十六进制数据
        x.write(myinput)  # 用write函数向串口发送数据
        myout = x.read(25)  # 提取接收缓冲区中的前7个字节数
        datas = ''.join(map(lambda x: ('/x' if len(hex(x)) >= 4 else '/x0') + hex(x)[2:], myout))
        new_datas = datas[2:].split('/x')  # 由于datas变量中的数据前两

        tem = (int(new_datas[3], 16) + int(new_datas[4], 16) * 256 + int(new_datas[5], 16) * 65536 + int(
            new_datas[6],
            16) * 16777216) / 100
        hum = (int(new_datas[11], 16) + int(new_datas[12], 16) * 256 + int(new_datas[13], 16) * 65536 + int(
            new_datas[14],
            16) * 16777216) / 100
        print("现在温度：", tem)
        print("现在湿度：", hum)
        x.close()

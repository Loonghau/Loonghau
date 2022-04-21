# -*- coding: utf-8 -*-
""" 
@Time : 2020/12/26 9:00
@Author : Loonghau XU
@FileName: pyserial_demo.py
@SoftWare: PyCharm
"""
import sys

import serial
import serial.tools.list_ports
from PyQt5 import QtWidgets

from balance import Ui_Form


class Pyqt5_Serial(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(Pyqt5_Serial, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("串口小助手")
        self.slot_init()

    def slot_init(self):  # 设置槽函数
        self.pushButton.clicked.connect(self.data_send)

    # 发送数据
    def data_send(self):
        global tem
        x = serial.Serial('com29', 9600, timeout=1)

        myinput = bytes([0X53, 0X0A, 0X0D])  # 需要发送"S"
        x.write(myinput)  # 用write函数向串口发送数据
        myout = x.read(25)  # 提取接收缓冲区中的前7个字节数
        tem = str(myout[6:14], encoding='utf-8')
        # print(tem)
        x.close()
        # self.lineEdit.clear()
        self.lineEdit.setText(str(tem))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myshow = Pyqt5_Serial()
    myshow.show()
    sys.exit(app.exec_())

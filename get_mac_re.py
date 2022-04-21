# -*- coding: utf-8 -*-
""" 
@Time : 2020/12/29 15:51
@Author : Loonghau XU
@FileName: tem_hum_new.py
@SoftWare: PyCharm
"""
import os
import re
import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal

from mac_get import Ui_Form


class Pyqt5_Serial(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(Pyqt5_Serial, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("获取电脑mac地址")
        self.mythread = MyThread()  # 实例化线程
        self.mythread.signal_mac.connect(self.callback_mac)  # 连接线程类中自定义信号槽到本类的自定义槽函数
        self.mythread.start()  # 开启线程不是调用run函数而是调用start函数

    def callback_mac(self, mac):
        self.lineEdit.setText(mac)


class MyThread(QThread):
    global mac
    signal_mac = pyqtSignal(str)  # 自定义一个pyqtSignal信号,信号参数是个字符串str类型

    def __init__(self):
        super(MyThread, self).__init__()

    def run(self):
        global ret
        if os.name == 'nt':
            try:
                ret = ''
                CmdLine = 'ipconfig /all'
                r = os.popen(CmdLine).read()
                print(r)
                if r:
                    L = re.findall(
                        '物理地址.*?([0-9,A-F]{2}-[0-9,A-F]{2}-[0-9,A-F]{2}-[0-9,A-F]{2}-[0-9,A-F]{2}-[0-9,A-F]{2})',
                        r)
                    if len(L) > 0:
                        ret = L[0]
            except:
                pass

        # Linux/Unix下
        elif os.name == "posix":
            try:
                ret = ''
                CmdLine = 'ifconfig'
                r = os.popen(CmdLine).read()
                if r:
                    L = re.findall(
                        'HWaddr.*?([0-9,A-F]{2}:[0-9,A-F]{2}:[0-9,A-F]{2}:[0-9,A-F]{2}:[0-9,A-F]{2}:[0-9,A-F]{2})', r)
                    if len(L) > 0:
                        ret = L[0]
            except:
                pass
        else:
            pass
        self.signal_mac.emit(str(ret))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = Pyqt5_Serial()
    myshow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-
""" 
@Time : 2020/12/29 15:51
@Author : Loonghau XU
@FileName: tem_hum_new.py
@SoftWare: PyCharm
"""
import sys

import serial
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal, QTimer

from temp_set import Ui_Form_temset

x = serial.Serial('com21', 2400, timeout=0.5)


class Pyqt5_Serial(QtWidgets.QWidget, Ui_Form_temset):
    def __init__(self):
        super(Pyqt5_Serial, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("全自动恒温恒湿称重系统")
        self.temhum_set_read()
        self.time_temp = QTimer()
        self.time_temp.timeout.connect(self.temp_humi)
        self.time_temp.start(2000)
        self.pushButton_3.clicked.connect(self.tem_set)
        self.pushButton_4.clicked.connect(self.hum_set)

    def temhum_set_read(self):
        # self.time_temp.stop()
        if x.isOpen() == True:
            x.close()
        else:
            pass
        self.mythread_read = MyThread_Read()
        self.mythread_read.start()
        self.mythread_read.signal_read.connect(self.temhum_read)

    def temp_humi(self):
        self.mythread = MyThread()  # 实例化线程
        self.mythread.signal_tem_hum.connect(self.callback_Blance)  # 连接线程类中自定义信号槽到本类的自定义槽函数
        self.mythread.start()  # 开启线程不是调用run函数而是调用start函数

    def tem_set(self):
        self.time_temp.stop()
        x.close()
        temset = self.doubleSpinBox_2.value()
        temset = format(temset, '.2f')
        self.mythread_tem_set = MyThread_TemSet(temset)
        self.mythread_tem_set.start()
        self.mythread_tem_set.msg_temset.connect(self.time_qtimer)

    def hum_set(self):
        self.time_temp.stop()
        x.close()
        humset = self.doubleSpinBox.value()
        humset = format(humset, '.1f')
        self.mythread_hum_set = MyThread_HumSet(humset)
        self.mythread_hum_set.start()
        self.mythread_hum_set.msg_humset.connect(self.time_qtimer)

    def start(self, start_stop):
        if start_stop:
            self.time_temp.stop()
            x.close()
            self.mythread_start = MyThread_Start()  # 实例化线程
            self.mythread_start.start()  # 开启线程不是调用run函数而是调用start函数
            self.mythread_start.msg_start.connect(self.time_qtimer)
            self.pushButton.setText("停止")
        else:
            self.time_temp.stop()
            x.close()
            self.mythread_stop = MyThread_Stop()  # 实例化线程
            self.mythread_stop.start()  # 开启线程不是调用run函数而是调用start函数
            self.mythread_stop.msg_stop.connect(self.time_qtimer)
            self.pushButton.setText("启动")

    def stop(self, start_stop):
        if start_stop:
            self.time_temp.stop()
            x.close()
            self.mythread_stop = MyThread_Stop()  # 实例化线程
            self.mythread_stop.start()  # 开启线程不是调用run函数而是调用start函数
            self.mythread_stop.msg_stop.connect(self.time_qtimer)
            self.pushButton.setText("启动")
        else:
            self.time_temp.stop()
            x.close()
            self.mythread_start = MyThread_Start()  # 实例化线程
            self.mythread_start.start()  # 开启线程不是调用run函数而是调用start函数
            self.mythread_start.msg_start.connect(self.time_qtimer)
            self.pushButton.setText("停止")

    def time_qtimer(self):
        self.time_temp.start(2000)

    def callback_Blance(self, tem, hum):
        self.label.setText(tem)
        self.label_3.setText(hum)

    def temhum_read(self, tem_set, hum_set, station):
        self.doubleSpinBox_2.setValue(float(tem_set))
        self.doubleSpinBox.setValue(float(hum_set))
        self.time_temp.start(2000)
        if int(station) == 3:
            self.pushButton.setText("停止")
            self.pushButton.clicked[bool].connect(self.stop)
        elif int(station) == 2:
            self.pushButton.setText("启动")
            self.pushButton.clicked[bool].connect(self.start)


class MyThread_Start(QThread):
    msg_start = pyqtSignal()

    def __init__(self):
        super(MyThread_Start, self).__init__()

    def run(self):
        # x = serial.Serial('com21', 2400, timeout=0.5)
        x.open()
        myinput = bytes([0X45, 0X30, 0X31, 0X23, 0X39, 0X39, 0X23, 0X31, 0X23, 0X41])  # 需要发送的十六进制数据E01#99#1#A
        x.write(myinput)  # 用write函数向串口发送数据
        x.flushInput()
        x.read(1)
        x.flushOutput()
        x.close()
        self.msg_start.emit()


class MyThread_Stop(QThread):
    msg_stop = pyqtSignal()

    def __init__(self):
        super(MyThread_Stop, self).__init__()

    def run(self):
        # x = serial.Serial('com21', 2400, timeout=0.5)
        x.open()
        myinput = bytes([0X45, 0X30, 0X31, 0X23, 0X39, 0X39, 0X23, 0X32, 0X23, 0X41])  # 需要发送的十六进制数据E01#99#2#A
        x.write(myinput)  # 用write函数向串口发送数据
        x.flushInput()
        x.read(1)
        x.flushOutput()
        x.close()
        self.msg_stop.emit()


class MyThread_TemSet(QThread):
    msg_temset = pyqtSignal()

    def __init__(self, temset):
        super(MyThread_TemSet, self).__init__()
        self.temset = temset

    def run(self):
        tem_set = str(self.temset)
        tem_set = 'E01#62#01#02#' + tem_set + '#A'
        myinput = bytes(tem_set.encode('utf-8'))
        # x = serial.Serial('com21', 2400, timeout=0.5)
        x.open()
        x.write(myinput)  # 用write函数向串口发送数据
        x.flushInput()
        x.read(1)
        x.flushOutput()
        x.close()
        self.msg_temset.emit()


class MyThread_HumSet(QThread):
    msg_humset = pyqtSignal()

    def __init__(self, humset):
        super(MyThread_HumSet, self).__init__()
        self.humset = humset

    def run(self):
        humset = str(self.humset)
        hum_set = 'E01#62#02#02#' + humset + '#A'
        myinput = bytes(hum_set.encode('utf-8'))
        # x = serial.Serial('com21', 2400, timeout=0.5)
        x.open()
        x.write(myinput)  # 用write函数向串口发送数据
        x.flushInput()
        x.read(1)
        x.flushOutput()
        x.close()
        self.msg_humset.emit()


class MyThread(QThread):
    signal_tem_hum = pyqtSignal(str, str)  # 自定义一个pyqtSignal信号,信号参数是个字符串str类型

    def __init__(self):
        super(MyThread, self).__init__()

    def run(self):
        try:
            # x = serial.Serial('com21', 2400, timeout=0.8)
            tem_set = 'S0199A'
            myinput = bytes(tem_set.encode('utf-8'))
            x.open()
            x.write(myinput)  # 用write函数向串口发送数据
            x.flushInput()
            myout = x.read(20)  # 提取接收缓冲区中的前7个字节数
            x.flushOutput()
            datas = ''.join(map(lambda x: ('/x' if len(hex(x)) >= 4 else '/x0') + hex(x)[2:], myout))
            new_datas = datas[2:].split('/x')  # 由于datas变量中的数据前两
            tem = (int(new_datas[3], 16) + int(new_datas[4], 16) * 256 + int(new_datas[5], 16) * 65536 + int(
                new_datas[6],
                16) * 16777216) / 100
            hum = (int(new_datas[11], 16) + int(new_datas[12], 16) * 256 + int(new_datas[13], 16) * 65536 + int(
                new_datas[14],
                16) * 16777216) / 100
            tem = format(tem, '.1f')
            hum = format(hum, '.1f')
            self.signal_tem_hum.emit(str(tem), str(hum))
            x.close()
        except:
            self.signal_tem_hum.emit('', '')


class MyThread_Read(QThread):
    signal_read = pyqtSignal(str, str, str)  # 自定义一个pyqtSignal信号,信号参数是个字符串str类型

    def __init__(self):
        super(MyThread_Read, self).__init__()

    def run(self):
        try:
            # x = serial.Serial('com21', 2400, timeout=0.8)
            tem_set = 'S0199A'
            myinput = bytes(tem_set.encode('utf-8'))
            x.open()
            x.write(myinput)  # 用write函数向串口发送数据
            x.flushInput()
            myout = x.read(20)  # 提取接收缓冲区中的前7个字节数
            x.flushOutput()
            datas = ''.join(map(lambda x: ('/x' if len(hex(x)) >= 4 else '/x0') + hex(x)[2:], myout))
            new_datas = datas[2:].split('/x')  # 由于datas变量中的数据前两
            tem_set = (int(new_datas[7], 16) + int(new_datas[8], 16) * 256 + int(new_datas[9], 16) * 65536 + int(
                new_datas[10],
                16) * 16777216) / 100
            hum_set = (int(new_datas[15], 16) + int(new_datas[16], 16) * 256 + int(new_datas[17], 16) * 65536 + int(
                new_datas[18],
                16) * 16777216) / 100
            station = int(new_datas[2], 16)
            print(station)
            tem_set = format(tem_set, '.2f')
            hum_set = format(hum_set, '.1f')
            self.signal_read.emit(str(tem_set), str(hum_set), str(station))
            x.close()
        except:
            self.signal_read.emit('', '', '')
            x.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = Pyqt5_Serial()
    myshow.show()
    sys.exit(app.exec_())

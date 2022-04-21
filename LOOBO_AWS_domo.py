# -*- coding: utf-8 -*-
""" 
@Time : 2020/12/29 15:51
@Author : Loonghau XU
@FileName: LB_AWS02.py
@SoftWare: PyCharm
"""
import sys

from PyQt5 import QtWidgets
from PyQt5.Qt import QThread

from loobo_aws import Ui_Form
from zmcwrapper import ZMCWrapper

zmc = ZMCWrapper()  # 实例化类、封装控制器类函数
ip_2048 = "192.168.0.11"  # 控制器IP地址
zmc.connect(ip_2048)  # 连接控制器
zmc.set_axis_type()  # 设定控制器轴类型“7”
zmc.set_axis_units()  # 设定轴脉冲当量


class Pyqt5_Serial(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(Pyqt5_Serial, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("全自动恒温恒湿称重系统调试软件")
        self.slot_init()  # 设置槽函数

    def slot_init(self):  # 设置槽函数
        self.pushButton.clicked.connect(self.PushB01)
        self.pushButton_2.clicked.connect(self.PushB02)
        self.pushButton_3.clicked.connect(self.PushB03)
        self.pushButton_4.clicked.connect(self.PushB04)
        self.pushButton_5.clicked.connect(self.PushB05)
        self.pushButton_6.clicked.connect(self.PushB06)
        self.pushButton_7.clicked.connect(self.PushB07)
        self.pushButton_8.clicked.connect(self.PushB08)
        self.pushButton_9.clicked.connect(self.PushB09)
        self.pushButton_10.clicked.connect(self.PushB10)
        self.pushButton_11.clicked.connect(self.PushB11)
        self.pushButton_12.clicked.connect(self.PushB12)
        self.pushButton_13.clicked.connect(self.PushB13)
        self.pushButton_14.clicked.connect(self.PushB14)
        self.pushButton_15.clicked.connect(self.PushB15)
        self.pushButton_16.clicked.connect(self.PushB16)
        self.pushButton_17.clicked.connect(self.PushB17)
        self.pushButton_18.clicked.connect(self.PushB18)
        self.pushButton_19.clicked.connect(self.PushB19)
        self.pushButton_20.clicked.connect(self.PushB20)

    def PushB01(self):
        self.thread_1 = Thread_1()  # 创建线程
        self.thread_1.start()  # 开始线程

    def PushB02(self):
        self.thread_2 = Thread_2()  # 创建线程
        self.thread_2.start()  # 开始线程

    def PushB03(self):
        self.thread_3 = Thread_3()  # 创建线程
        self.thread_3.start()  # 开始线程

    def PushB04(self):
        self.thread_4 = Thread_4()  # 创建线程
        self.thread_4.start()  # 开始线程

    def PushB05(self):
        self.thread_5 = Thread_5()  # 创建线程
        self.thread_5.start()  # 开始线程

    def PushB06(self):
        self.thread_6 = Thread_6()  # 创建线程
        self.thread_6.start()  # 开始线程

    def PushB07(self):
        self.thread_7 = Thread_7()  # 创建线程
        self.thread_7.start()  # 开始线程

    def PushB08(self):
        self.thread_8 = Thread_8()  # 创建线程
        self.thread_8.start()  # 开始线程

    def PushB09(self):
        self.thread_9 = Thread_9()  # 创建线程
        self.thread_9.start()  # 开始线程

    def PushB10(self):
        self.thread_10 = Thread_10()  # 创建线程
        self.thread_10.start()  # 开始线程

    def PushB11(self):
        self.thread_11 = Thread_11()  # 创建线程
        self.thread_11.start()  # 开始线程

    def PushB12(self):
        self.thread_12 = Thread_12()  # 创建线程
        self.thread_12.start()  # 开始线程

    def PushB13(self):
        self.thread_13 = Thread_13()  # 创建线程
        self.thread_13.start()  # 开始线程

    def PushB14(self):
        self.thread_14 = Thread_14()  # 创建线程
        self.thread_14.start()  # 开始线程

    def PushB15(self):
        self.thread_15 = Thread_15()  # 创建线程
        self.thread_15.start()  # 开始线程

    def PushB16(self):
        self.thread_16 = Thread_16()  # 创建线程
        self.thread_16.start()  # 开始线程

    def PushB17(self):
        self.thread_17 = Thread_17()  # 创建线程
        self.thread_17.start()  # 开始线程

    def PushB18(self):
        self.thread_18 = Thread_18()  # 创建线程
        self.thread_18.start()  # 开始线程

    def PushB19(self):
        self.thread_19 = Thread_19()  # 创建线程
        self.thread_19.start()  # 开始线程

    def PushB20(self):
        self.thread_20 = Thread_20()  # 创建线程
        self.thread_20.start()  # 开始线程


class Thread_1(QThread):  # 2轴移动一位--ok
    def __init__(self):
        super(Thread_1, self).__init__()

    def run(self):
        ip_2048 = "192.168.0.11"
        zmc.connect(ip_2048)  # 连接控制器
        # zmc.read_info()  # 读取控制器信息
        zmc.set_axis_type()
        zmc.set_axis_units()
        zmc.set_op(7, 0)
        zmc.axis_2_move(8572)


class Thread_2(QThread):  # 1轴上升至天平顶--ok
    def __init__(self):
        super(Thread_2, self).__init__()

    def run(self):
        ip_2048 = "192.168.0.11"
        zmc.connect(ip_2048)  # 连接控制器
        # zmc.read_info()  # 读取控制器信息
        zmc.set_axis_type()
        zmc.set_axis_units()
        zmc.set_op(7, 0)
        zmc.axis_1_up(76000)


class Thread_3(QThread):  # 1轴上升至天平底--ok
    def __init__(self):
        super(Thread_3, self).__init__()

    def run(self):
        ip_2048 = "192.168.0.11"
        zmc.connect(ip_2048)  # 连接控制器
        # zmc.read_info()  # 读取控制器信息
        zmc.set_axis_type()
        zmc.set_axis_units()
        zmc.set_op(7, 0)
        zmc.axis_1_up(62000)


class Thread_4(QThread):  # 1轴点动--ok
    def __init__(self):
        super(Thread_4, self).__init__()

    def run(self):
        ip_2048 = "192.168.0.11"
        zmc.connect(ip_2048)  # 连接控制器
        # zmc.read_info()  # 读取控制器信息
        zmc.set_axis_type()
        zmc.set_axis_units()
        zmc.set_op(7, 0)
        zmc.axis_1_move(1000)


class Thread_5(QThread):  # 2轴开始运行--ok
    def __init__(self):
        super(Thread_5, self).__init__()

    def run(self):
        ip_2048 = "192.168.0.11"
        zmc.connect(ip_2048)  # 连接控制器
        # zmc.read_info()  # 读取控制器信息
        zmc.set_axis_type()
        zmc.set_axis_units()
        zmc.set_op(7, 0)
        zmc.set_move(2, 1)


class Thread_6(QThread):  # 2轴停止运行--ok
    def __init__(self):
        super(Thread_6, self).__init__()

    def run(self):
        ip_2048 = "192.168.0.11"
        zmc.connect(ip_2048)  # 连接控制器
        # zmc.read_info()  # 读取控制器信息
        zmc.set_axis_type()
        zmc.set_axis_units()
        zmc.set_op(7, 0)
        zmc.set_cancel(2, 0)


class Thread_7(QThread):  # 1轴位置-样品ok
    def __init__(self):
        super(Thread_7, self).__init__()

    def run(self):
        ip_2048 = "192.168.0.11"
        zmc.connect(ip_2048)  # 连接控制器
        # zmc.read_info()  # 读取控制器信息
        zmc.set_axis_type()
        zmc.set_axis_units()
        zmc.set_op(7, 0)
        zmc.axis_0_move(-2642)


class Thread_8(QThread):  # ok
    def __init__(self):
        super(Thread_8, self).__init__()

    def run(self):
        ip_2048 = "192.168.0.11"
        zmc.connect(ip_2048)  # 连接控制器
        # zmc.read_info()  # 读取控制器信息
        zmc.set_axis_type()
        zmc.set_axis_units()
        zmc.set_op(7, 0)
        zmc.axis_0_move(8540)


class Thread_9(QThread):  # 天平罩上升--ok
    def __init__(self):
        super(Thread_9, self).__init__()

    def run(self):
        ip_2048 = "192.168.0.11"
        zmc.connect(ip_2048)  # 连接控制器
        # zmc.read_info()  # 读取控制器信息
        zmc.set_axis_type()
        zmc.set_units(3, 3)
        zmc.set_op(7, 0)
        zmc.axis_3_up()


class Thread_10(QThread):  # 天平罩下降--ok
    def __init__(self):
        super(Thread_10, self).__init__()

    def run(self):
        ip_2048 = "192.168.0.11"
        zmc.connect(ip_2048)  # 连接控制器
        # zmc.read_info()  # 读取控制器信息
        zmc.set_axis_type()
        zmc.set_units(3, 3)
        zmc.set_op(7, 0)
        zmc.axis_3_down()


class Thread_11(QThread):  # 机械臂左旋--ok
    def __init__(self):
        super(Thread_11, self).__init__()

    def run(self):
        ip_2048 = "192.168.0.11"
        zmc.connect(ip_2048)  # 连接控制器
        # zmc.read_info()  # 读取控制器信息
        zmc.set_axis_type()
        zmc.set_axis_units()
        # zmc.set_op(7, 0)
        zmc.set_move(0, -1)


class Thread_12(QThread):  # 机械臂右旋--ok
    def __init__(self):
        super(Thread_12, self).__init__()

    def run(self):
        ip_2048 = "192.168.0.11"
        zmc.connect(ip_2048)  # 连接控制器
        # zmc.read_info()  # 读取控制器信息
        zmc.set_axis_type()
        zmc.set_axis_units()
        # zmc.set_op(7, 0)
        zmc.set_move(0, 1)


class Thread_13(QThread):  # O轴上升
    def __init__(self):
        super(Thread_13, self).__init__()

    def run(self):
        ip_2048 = "192.168.0.11"
        zmc.connect(ip_2048)  # 连接控制器
        # zmc.read_info()  # 读取控制器信息
        zmc.set_axis_type()
        zmc.set_axis_units()
        zmc.set_op(7, 0)
        zmc.set_speed(1, 4000)
        zmc.set_move(1, 1)


class Thread_14(QThread):  # O轴下降
    def __init__(self):
        super(Thread_14, self).__init__()

    def run(self):
        ip_2048 = "192.168.0.11"
        zmc.connect(ip_2048)  # 连接控制器
        # zmc.read_info()  # 读取控制器信息
        zmc.set_axis_type()
        zmc.set_axis_units()
        zmc.set_op(7, 0)
        zmc.set_speed(1, 4000)
        zmc.set_move(1, -1)


class Thread_15(QThread):  # 旋转停止
    def __init__(self):
        super(Thread_15, self).__init__()

    def run(self):
        ip_2048 = "192.168.0.11"
        zmc.connect(ip_2048)  # 连接控制器
        # zmc.read_info()  # 读取控制器信息
        zmc.set_axis_type()
        zmc.set_axis_units()
        zmc.set_op(7, 0)
        zmc.set_cancel(0, 0)


class Thread_16(QThread):  # 上升下降回复
    def __init__(self):
        super(Thread_16, self).__init__()

    def run(self):
        ip_2048 = "192.168.0.11"
        zmc.connect(ip_2048)  # 连接控制器
        # zmc.read_info()  # 读取控制器信息
        zmc.set_axis_type()
        zmc.set_axis_units()
        zmc.set_op(7, 0)
        zmc.axis_1_back()


class Thread_17(QThread):  # 样品架旋转复位--ok
    def __init__(self):
        super(Thread_17, self).__init__()

    def run(self):
        ip_2048 = "192.168.0.11"
        zmc.connect(ip_2048)  # 连接控制器
        # zmc.read_info()  # 读取控制器信息
        zmc.set_axis_type()
        zmc.set_axis_units()
        zmc.set_op(7, 0)
        zmc.axis_2_back()


class Thread_18(QThread):  # 上下运动复位ok
    def __init__(self):
        super(Thread_18, self).__init__()

    def run(self):
        ip_2048 = "192.168.0.11"
        zmc.connect(ip_2048)  # 连接控制器
        # zmc.read_info()  # 读取控制器信息
        zmc.set_axis_type()
        zmc.set_axis_units()
        zmc.set_op(7, 0)
        zmc.set_op(0, 1)


class Thread_19(QThread):  # 上下运动停止ok
    def __init__(self):
        super(Thread_19, self).__init__()

    def run(self):
        ip_2048 = "192.168.0.11"
        zmc.connect(ip_2048)  # 连接控制器
        # zmc.read_info()  # 读取控制器信息
        zmc.set_axis_type()
        zmc.set_axis_units()
        zmc.set_op(7, 0)
        zmc.set_cancel(1, 0)


class Thread_20(QThread):  # 上下运动停止ok
    def __init__(self):
        super(Thread_20, self).__init__()

    def run(self):
        ip_2048 = "192.168.0.11"
        zmc.connect(ip_2048)  # 连接控制器
        # zmc.read_info()  # 读取控制器信息
        zmc.set_axis_type()
        zmc.set_axis_units()
        zmc.set_op(7, 0)
        zmc.axis_0_move(12000)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = Pyqt5_Serial()
    myshow.show()
    sys.exit(app.exec_())

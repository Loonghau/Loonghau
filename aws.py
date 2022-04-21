# -*- coding: utf-8 -*-
""" 
@Time : 2020/12/24 13:02
@Author : Loonghau XU
@FileName: test.py
@SoftWare: PyCharm
"""
import time

from zmcwrapper import ZMCWrapper

zmc = ZMCWrapper()  # 实例化类
iplist, num = zmc.search()
zmc.connect(iplist[0])  # 连接控制器
zmc.set_axis_type()
zmc.set_axis_units()
zmc.set_input()
for i in range(200):
    print(i)
    zmc.axis_1_up(34000)  # Z轴上升至样品底部高度
    time.sleep(0.5 + 34000 / zmc.get_speed(1))
    zmc.axis_0_move(-2557)  # Z轴旋转至样品底部
    time.sleep(0.5 + 2557 / zmc.get_speed(0))
    zmc.axis_1_up(53000)  # Z轴升高，托住样品
    time.sleep(0.5 + (53000 - 34000) / zmc.get_speed(1))
    zmc.axis_0_move(0)  # Z轴旋转至初始位置
    time.sleep(0.5 + 2557 / zmc.get_speed(0))
    zmc.axis_1_up(82000)
    time.sleep(0.5 + (82000 - 53000) / zmc.get_speed(1))
    zmc.axis_0_move(8540)
    time.sleep(0.5 + 8540 / zmc.get_speed(0))
    zmc.axis_1_up(68000)
    time.sleep(0.5 + (82000 - 68000) / zmc.get_speed(1))
    zmc.axis_0_move(12000)
    time.sleep(0.5 + (12000 - 8540) / zmc.get_speed(0))
    zmc.axis_3_down()
    time.sleep(25)
    zmc.axis_3_up()
    # time.sleep(25)
    zmc.axis_0_move(8540)
    time.sleep(0.5 + (12000 - 8540) / zmc.get_speed(0))
    zmc.axis_1_up(82000)
    time.sleep(0.5 + (82000 - 68000) / zmc.get_speed(1))
    zmc.axis_0_move(0)  # Z轴旋转至初始位置
    time.sleep(0.5 + 8540 / zmc.get_speed(0))
    zmc.axis_1_up(53000)  # Z轴升高，托住样品
    time.sleep(0.5 + (82000 - 53000) / zmc.get_speed(1))
    zmc.axis_0_move(-2557)  # Z轴旋转至样品底部
    time.sleep(0.5 + 2557 / zmc.get_speed(0))
    zmc.axis_1_up(34000)  # Z轴上升至样品底部高度
    time.sleep(0.5 + (53000 - 34000) / zmc.get_speed(1))
    zmc.axis_0_move(0)  # Z轴旋转至初始位置
    time.sleep(0.5 + 2557 / zmc.get_speed(0))
    zmc.axis_1_back()
    time.sleep(0.5 + (34000 - 0) / zmc.get_speed(1))
    zmc.axis_2_move(8572)
    time.sleep(0.5 + 8572 / zmc.get_speed(2))

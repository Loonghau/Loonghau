# -*- coding: utf-8 -*-
""" 
@Time : 2021/1/8 15:58
@Author : Loonghau XU
@FileName: romantic_2.py
@SoftWare: PyCharm
"""
import time

from zmcwrapper import ZMCWrapper

zmc = ZMCWrapper()  # 实例化类
iplist, num = zmc.search()
ip_2048 = "192.168.0.11"
zmc.connect(ip_2048)  # 连接控制器
zmc.read_info()  # 读取控制器信息
zmc.set_axis_type()
zmc.set_axis_units()


zmc.set_move(0,-1)


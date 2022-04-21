# -*- coding: utf-8 -*-
""" 
@Time : 2021/1/11 13:05
@Author : Loonghau XU
@FileName: test_3_2.py
@SoftWare: PyCharm
"""
from zmcwrapper import ZMCWrapper

ip_2048 = "192.168.0.11"
zmc = ZMCWrapper()  # 实例化类
zmc.connect(ip_2048)
zmc.set_axis_type()
zmc.set_axis_units()
zmc.set_input()
zmc.reset_ban()

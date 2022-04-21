# -*- coding: utf-8 -*-
""" 
@Time : 2021/1/11 13:05
@Author : Loonghau XU
@FileName: test_3_2.py
@SoftWare: PyCharm
"""
from zmcwrapper import ZMCWrapper
import time

zmc = ZMCWrapper()  # 实例化类
iplist, num = zmc.search()

ip_2048 = "192.168.0.11"
zmc.connect(ip_2048)

zmc.set_op(7,1)
time.sleep(5)
zmc.set_op(7,0)

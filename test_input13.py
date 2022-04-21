# -*- coding: utf-8 -*-
""" 
@Time : 2021/1/11 13:05
@Author : Loonghau XU
@FileName: test_3_2.py
@SoftWare: PyCharm
"""
from zmcwrapper import ZMCWrapper
import threading,time

zmc = ZMCWrapper()  # 实例化类
iplist, num = zmc.search()

ip_2048 = "192.168.0.11"
zmc.connect(ip_2048)

for i in range(100000000):
    if zmc.get_input(13) == 0:
        continue
    elif zmc.get_input(13)==1:
        zmc.set_move(2,1)
    time.sleep(60)

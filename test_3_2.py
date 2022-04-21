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

axis_3=zmc.axis_3_fwdin()
#axis_3=zmc.axis_3_revin()
axis_2=zmc.axis_2_moveabs(20000)
#axis_2_b=zmc.axis_2_back()


thead_3 = threading.Thread(target=axis_3)
theat_2 = threading.Thread(target=axis_2)
#thead_2_b=threading.Thread(target=axis_2_b)
thead_3.start()
theat_2.start()
time.sleep(10)
#thead_2_b.start()
eatT = thead_3.join()
playT = theat_2.join()
#xxT=thead_2_b.join()

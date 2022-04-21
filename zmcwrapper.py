# -*- coding: utf-8 -*-
"""
@Time : 2020/12/25 9:18
@Author : Loonghau XU
@FileName: zmcwrapper.py
@SoftWare: PyCharm
"""
import configparser
import ctypes
import os
import platform
import sys
import time

import serial

BASE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))
conf = configparser.RawConfigParser()
conf.read(os.path.join(BASE_DIR, 'setting_aws.ini'))

systype = platform.system()  # 判断系统型号
if systype == 'Windows':
    if platform.architecture()[0] == '64bit':
        # Windows平台上，实例即加载好的动态链接库ZAux_
        zauxdll = ctypes.WinDLL('./zauxdll.dll')
        zmcdll = ctypes.WinDLL('./zmotion.dll')  # Windows平台上，实例即加载好的动态链接库ZMC_
        print('Windows x64')
    else:
        zmcdll = ctypes.WinDLL('./zmotion.dll')  # Windows平台上，实例即加载好的动态链接库
        print('Windows x86')
elif systype == 'Darwin':
    zmcdll = ctypes.CDLL('./zmotion.dylib')
    print("macOS")
elif systype == 'Linux':
    zmcdll = ctypes.CDLL('./zmotion.so')
    print("Linux")
else:
    print("OS Not Supported!!")


class ZMCWrapper:  # 封装运动函数类
    def __init__(self):
        self.handle = ctypes.c_void_p()
        self.sys_ip = ""
        self.sys_info = ""
        self.is_connected = False

    def search(self, console=None):  # 搜索当前网段下的控制器 IP
        if console is None:
            console = []
        # create_string_buffer创建的是一个 ANSI 标准的 C类型字符串
        iplist = ctypes.create_string_buffer(b'', 1024)
        zauxdll.ZAux_SearchEthlist(ctypes.byref(iplist), 1024, 200)
        s = iplist.value.decode()
        str_iplist = s.split()
        num = len(str_iplist)
        print(num, "Controller(s) Found:")
        print(*str_iplist, sep='\n')
        console.append("Searching...")
        console.append(str(num) + " Controller(s) Found:")
        return str_iplist, num

    def connect(self, ip, console=None):  # 连接控制器
        if console is None:
            console = []
        if self.handle.value is not None:
            self.disconnect()
        ip_bytes = ip.encode('utf-8')
        p_ip = ctypes.c_char_p(ip_bytes)
        print("Connecting to", ip, "...")
        ret = zauxdll.ZAux_OpenEth(p_ip, ctypes.pointer(self.handle))
        msg = "Connected"
        if ret == 0:
            # print("Connected")
            msg = ip + " Connected"
            self.sys_ip = ip
            self.is_connected = True
        else:
            # print("Error", ret)
            msg = "Connection Failed, Error " + str(ret)
            self.is_connected = False
        console.append(msg)
        console.append(self.sys_info)
        return ret

    def disconnect(self):  # 断开控制器
        ret = zauxdll.ZAux_Close(self.handle)
        self.is_connected = False
        return ret

    def read_info(self):
        cname = ctypes.create_string_buffer(b'', 32)
        fVersion = ctypes.c_float()
        date = ctypes.c_uint32()
        zmcdll.ZMC_GetSoftVersion(
            self.handle,
            ctypes.byref(fVersion),
            ctypes.byref(cname),
            ctypes.byref(date))
        print("%.2f" % fVersion.value, cname.value, date.value)
        info = cname.value.decode() + " Version:" + str("%.2f" %
                                                        fVersion.value) + " Date:" + str(date.value)
        print(info)
        return info

    # 单轴持续运动
    def vmove(self, iaxis, idir):
        cmdbuffer = (ctypes.c_char * 2048)()
        str1 = "VMOVE(%d) AXIS(%d)" % (idir, iaxis)
        cmd = ctypes.c_char_p(bytes(str1, 'utf-8'))
        zmcdll.ZMC_DirectCommand(self.handle, cmd, cmdbuffer, 2048)
        return

    # 设置轴类型
    def set_atype(self, iaxis, iValue):  # 7 脉冲方向方式步进或伺服+EZ 信号输入
        ret = zauxdll.ZAux_Direct_SetAtype(self.handle, iaxis, iValue)
        if ret == 0:
            print("Set Axis (", iaxis, ") Atype:", iValue)
        else:
            print("Set Axis (", iaxis, ") Atype fail!")
        return ret

    # 设置脉冲当量
    def set_units(self, iaxis, iValue):
        ret = zauxdll.ZAux_Direct_SetUnits(
            self.handle, iaxis, ctypes.c_float(iValue))
        if ret == 0:
            print("Set Axis (", iaxis, ") Units:", iValue)
        else:
            print("Set Axis (", iaxis, ") Units fail!")
        return ret

    # 设置轴加速度
    def set_accel(self, iaxis, iValue):
        ret = zauxdll.ZAux_Direct_SetAccel(
            self.handle, iaxis, ctypes.c_float(iValue))
        if ret == 0:
            print("Set Axis (", iaxis, ") Accel:", iValue)
        else:
            print("Set Accel (", iaxis, ") Accel fail!")
        return ret

    # 设置轴DPOS（初始位置）
    def set_DPOS(self, iaxis, position):
        ret = zauxdll.ZAux_Direct_SetDpos(
            self.handle, iaxis, ctypes.c_float(position))
        if ret == 0:
            print("Set Axis(", iaxis, ") Position:", position)
        else:
            print("Set Axis(", iaxis, ") Position fail")
        return ret

    # 设置轴减速度

    def set_decel(self, iaxis, iValue):
        ret = zauxdll.ZAux_Direct_SetDecel(
            self.handle, iaxis, ctypes.c_float(iValue))
        if ret == 0:
            print("Set Axis (", iaxis, ") Decel:", iValue)
        else:
            print("Set Axis (", iaxis, ") Decel fail!")
        return ret

    # 设置轴运行速度

    def set_speed(self, iaxis, iValue):
        ret = zauxdll.ZAux_Direct_SetSpeed(
            self.handle, iaxis, ctypes.c_float(iValue))
        if ret == 0:
            print("Set Axis (", iaxis, ") Speed:", iValue)
        else:
            print("Set Axis (", iaxis, ") Speed fail!")
        return ret

    # 设置轴爬行速度

    def set_creep(self, iaxis, iValue):
        ret = zauxdll.ZAux_Direct_SetCreep(
            self.handle, iaxis, ctypes.c_float(iValue))
        if ret == 0:
            print("Set Axis (", iaxis, ") creep:", iValue)
        else:
            print("Set Axis (", iaxis, ") creep fail!")
        return ret

    def set_datumin(self, iaxis, ivalue):  # 设置轴原点信号
        ret = zauxdll.ZAux_Direct_SetDatumIn(self.handle, iaxis, ivalue)
        if ret == 0:
            print("Set Axis (", iaxis, ") DatumIn:", ivalue)
        else:
            print("Set Axis (", iaxis, ") DatumIn fail!")
        return ret

    def set_move(self, iaxis, idir):  # 单轴连续运动指令，iaxis轴号，idir：运动方向，1，正向，-1，负向
        ret = zauxdll.ZAux_Direct_Single_Vmove(self.handle, iaxis, idir)
        if ret == 0:
            print("Set Axis (", iaxis, ") Vmove:", idir)
        else:
            print("Set Axis (", iaxis, ") Vmove fail!")
            print(ret)
        return ret

    def set_singelmoveabs(self, iaxis, idistance):  # 单周绝对运动
        ret = zauxdll.ZAux_Direct_Single_MoveAbs(
            self.handle, iaxis, ctypes.c_float(idistance))
        if ret == 0:
            print("Set Axis (", iaxis, ") distance:", idistance)
        else:
            print("Set Axis (", iaxis, ") distance fail!")
            print(ret)
        return ret

    def set_singelmove(self, iaxis, idistance):  # 单周相对运动
        ret = zauxdll.ZAux_Direct_Single_Move(
            self.handle, iaxis, ctypes.c_float(idistance))
        if ret == 0:
            print("Set Axis (", iaxis, ") distance:", idistance)
        else:
            print("Set Axis (", iaxis, ") distance fail!")
            print(ret)
        return ret

    def set_fwdin(self, iaxis, ivalue):  # 设置轴正限位输入的对应输入口
        ret = zauxdll.ZAux_Direct_SetFwdIn(self.handle, iaxis, ivalue)
        if ret == 0:
            print("Set Axis (", iaxis, ") FwdIn:", ivalue)
        else:
            print("Set Axis (", iaxis, ") FwdIn fail!")
        return ret

    def set_revin(self, iaxis, ivalue):
        ret = zauxdll.ZAux_Direct_SetRevIn(self.handle, iaxis, ivalue)
        if ret == 0:
            print("Set Axis (", iaxis, ") RevIn:", ivalue)
        else:
            print("Set Axis (", iaxis, ") RevIn fail!")
        return ret

    def set_single_datum(self, iaxis, imode):  # 单轴回零运动
        ret = zauxdll.ZAux_Direct_Single_Datum(self.handle, iaxis, imode)
        if ret == 0:
            print("Set Axis (", iaxis, ") Datum:", ret)
        else:
            print("Set Axis (", iaxis, ") Datum fail!")
        return ret

    # 轴运动停止
    def set_cancel(self, iaxis, imode):
        ret = zauxdll.ZAux_Direct_Single_Cancel(self.handle, iaxis, imode)
        if ret == 0:
            print("Set Axis (", iaxis, ") Cancel OK!")
        else:
            print("Set Axis (", iaxis, ") DCancel fail!")
        return ret

    def set_op(self, iout, idir):  # 设置输出口值
        ret = zauxdll.ZAux_Direct_SetOp(
            self.handle, iout, ctypes.c_uint32(idir))
        if ret == 0:
            print("Set Out (", iout, ") Output:", idir)
        else:
            print("Set Out (", iout, ") Output fail!")
        return ret

    def get_op(self, iout):
        iValue = (ctypes.c_int)()
        ret = zauxdll.ZAux_Direct_GetOp(
            self.handle, iout, ctypes.byref(iValue))
        if ret == 0:
            print("Get Out (", iout, ") Stay:", iValue.value)
        else:
            print("Get Out (", iout, ") Stay fail!")
        return iValue.value

    # 读取轴类型
    def get_atype(self, iaxis):
        iValue = (ctypes.c_int)()
        ret = zauxdll.ZAux_Direct_GetAtype(
            self.handle, iaxis, ctypes.byref(iValue))
        if ret == 0:
            print("Get Axis (", iaxis, ") Atype:", iValue.value)
        else:
            print("Get Axis (", iaxis, ") Atype fail!")
        return iValue.value

    def get_input(self, inx):  # 读取输入口状态
        iValue = (ctypes.c_int)()
        ret = zauxdll.ZAux_Direct_GetIn(self.handle, inx, ctypes.byref(iValue))
        if ret == 0:
            print("Get In (", inx, ") Stay:", iValue.value)
        else:
            print("Get In (", inx, ") Stay fail!")
        return iValue.value

    # 读取轴脉冲当量
    def get_units(self, iaxis):
        iValue = (ctypes.c_float)()
        ret = zauxdll.ZAux_Direct_GetUnits(
            self.handle, iaxis, ctypes.byref(iValue))
        if ret == 0:
            print("Get Axis (", iaxis, ") Units:", iValue.value)
        else:
            print("Get Axis (", iaxis, ") Units fail!")
        return iValue.value

    # 读取轴加速度
    def get_accel(self, iaxis):
        iValue = (ctypes.c_float)()
        ret = zauxdll.ZAux_Direct_GetAccel(
            self.handle, iaxis, ctypes.byref(iValue))
        if ret == 0:
            print("Get Axis (", iaxis, ") Accel:", iValue.value)
        else:
            print("Get Axis (", iaxis, ") Accel fail!")
        return iValue.value

    # 读取轴减速度
    def get_decel(self, iaxis):
        iValue = (ctypes.c_float)()
        ret = zauxdll.ZAux_Direct_GetDecel(
            self.handle, iaxis, ctypes.byref(iValue))
        if ret == 0:
            print("Get Axis (", iaxis, ") Decel:", iValue.value)
        else:
            print("Get Axis (", iaxis, ") Decel fail!")
        return iValue.value

    # 读取轴运行速度
    def get_speed(self, iaxis):
        iValue = (ctypes.c_float)()
        ret = zauxdll.ZAux_Direct_GetSpeed(
            self.handle, iaxis, ctypes.byref(iValue))
        if ret == 0:
            print("Get Axis (", iaxis, ") Speed:", iValue.value)
        else:
            print("Get Axis (", iaxis, ") Speed fail!")
        return iValue.value

    # 获取轴DPOS（位置）
    def get_DPOS(self, iaxis):
        iValue = (ctypes.c_float)()
        ret = zauxdll.ZAux_Direct_GetDpos(
            self.handle, iaxis, ctypes.byref(iValue))
        if ret == 0:
            print("Get Axis(", iaxis, ") Position:", iValue.value)
        else:
            print("Get Axis(", iaxis, ") Position fail")
        return iValue.value

    def get_datumin(self, iaxis):
        iValue = (ctypes.c_int)()
        ret = zauxdll.ZAux_Direct_GetDatumIn(
            self.handle, iaxis, ctypes.byref(iValue))
        if ret == 0:
            print("Get Axis (", iaxis, ") DatumIn:", iValue.value)
        else:
            print("Get Axis (", iaxis, ") DatumIn fail!")
        return iValue.value

    # 获取设置正向限位输入的值
    def get_fwdin(self, iaxis):
        iValue = (ctypes.c_int)()
        ret = zauxdll.ZAux_Direct_GetFwdIn(
            self.handle, iaxis, ctypes.byref(iValue))
        if ret == 0:
            print("Get Axis (", iaxis, ") Fwdin:", iValue.value)
        else:
            print("Get Axis (", iaxis, ") Fwdin fail!")
        return iValue.value

    # 获取设置负向限位输入的值
    def get_revin(self, iaxis):
        iValue = (ctypes.c_int)()
        ret = zauxdll.ZAux_Direct_GetRevIn(
            self.handle, iaxis, ctypes.byref(iValue))
        if ret == 0:
            print("Get Axis (", iaxis, ") Revin:", iValue.value)
        else:
            print("Get Axis (", iaxis, ") Revin fail!")
        return iValue.value

    def set_axis_type(self):  # 设置轴类型
        self.set_atype(0, 7)
        self.set_atype(1, 7)
        self.set_atype(2, 7)
        self.set_atype(3, 7)

    def set_axis_units(self):  # 设置轴脉冲当量
        self.set_units(0, 1)
        self.set_units(1, 1)
        self.set_units(2, 1)
        self.set_units(3, 1)

    def set_input(self):
        self.set_datumin(1, 4)
        self.set_revin(1, 4)
        self.set_fwdin(1, 5)
        self.set_datumin(3, 8)
        self.set_fwdin(3, 8)
        self.set_revin(3, 9)
        self.set_datumin(2, 7)

    def axis_3_up(self):  # 定义3轴上运动至限位点
        distance = self.get_DPOS(3)
        self.set_fwdin(3, 8)
        self.set_speed(3, 5000)
        self.set_single_datum(3, 8)
        time.sleep(0.5 + abs(distance) / self.get_speed(3))

    def axis_3_down(self):  # 定义3轴下运动至限位点
        self.set_revin(3, 9)
        self.set_speed(3, 5000)
        self.set_move(3, -1)

    def axis_2_moveabs(self, distance):  # 定义2轴连续运动绝对距离
        self.set_speed(2, 3000)  # 运动速度
        self.set_singelmoveabs(2, distance)  # 运动绝对距离

    def axis_2_move(self, distance):  # 定义2轴连续运动相对距离
        self.set_speed(2, 3000)  # 运动速度
        self.set_singelmove(2, distance)  # 运动相对距离

    def axis_2_back(self):  # 定义2轴回零运动
        self.set_datumin(2, 7)
        self.set_speed(2, 3000)
        self.set_single_datum(2, 8)
        time.sleep(120000 / self.get_speed(2))

    def axis_2_pointmove(self):
        while True:
            if self.get_input(13) == 0:
                break
            else:
                self.axis_2_move(10000)

    def axis_1_back(self):
        self.set_speed(1, 5000)
        self.set_datumin(1, 4)
        self.set_single_datum(1, 9)

    def axis_1_up(self, distance):
        self.set_speed(1, 5000)
        self.set_singelmoveabs(1, distance)

    def axis_0_move(self, distance):
        self.set_speed(0, 1000)
        self.set_singelmoveabs(0, distance)

    def axis_0_back(self):
        self.axis_0_move(0)

    def axis_1_move(self, distance):
        self.set_speed(1, 1000)
        self.set_singelmove(1, distance)

    def code_ban(self):
        com_balance = conf.get('COM', 'com_code')
        baud_rate_ba = int(conf.get('COM', 'baud_rate_co'))
        y = serial.Serial("com" + com_balance, baud_rate_ba, timeout=0.1)  # 扫码
        myinput = bytes([0X16, 0X54, 0X0D])  # 需要发送"S"
        y.write(myinput)  # 用write函数向串口发送数据
        try:
            myout = y.read(18)  # 提取接收缓冲区中的前7个字节数
            ban = int(myout)
        except BaseException:
            ban = " "
        y.close()
        return ban

    def weight_ban(self):
        com_balance = conf.get('COM', 'com_balance')
        baud_rate_ba = int(conf.get('COM', 'baud_rate_ba'))
        y = serial.Serial("com" + com_balance, baud_rate_ba, timeout=0.1)  # 扫码
        myinput = bytes([0X53, 0X0A, 0X0D])  # 需要发送"S"
        y.write(myinput)  # 用write函数向串口发送数据
        try:
            myout = y.read(15)  # 提取接收缓冲区中的前7个字节数
            ban = str(myout[6:14], encoding='utf-8')
        except BaseException:
            ban = " "
        y.close()
        return ban

    def reset_ban(self):
        com_balance = conf.get('COM', 'com_balance')
        baud_rate_ba = int(conf.get('COM', 'baud_rate_ba'))
        y = serial.Serial("com" + com_balance, baud_rate_ba, timeout=0.1)  # 扫码
        myinput = bytes([0X5A, 0X0A, 0X0D])  # 需要发送"Z"
        y.write(myinput)  # 用write函数向串口发送数据
        myout = y.read(15)  # 提取接收缓冲区中的前7个字节数
        y.close()

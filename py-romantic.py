import platform
import ctypes

systype = platform.system()  # 判断系统型号
if systype == 'Windows':
    if platform.architecture()[0] == '64bit':
        zmcdll = ctypes.WinDLL('./zmotion.dll')  # Windows平台上，实例即加载好的动态链接库
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


class ZMCWrapper:
    def __init__(self):
        self.handle = ctypes.c_void_p()
        self.sys_ip = ""
        self.sys_info = ""
        self.is_connected = False

    def search(self, console=[]):  # 搜索当前网段下的控制器 IP
        iplist = ctypes.create_string_buffer(b'', 1024)  # create_string_buffer创建的是一个 ANSI 标准的 C类型字符串
        zmcdll.ZMC_SearchEth(ctypes.byref(iplist), 1024, 200)
        s = iplist.value.decode()
        str_iplist = s.split()
        num = len(str_iplist)
        print(num, "Controller(s) Found:")
        print(*str_iplist, sep='\n')
        console.append("Searching...")
        console.append(str(num) + " Controller(s) Found:")
        return str_iplist, num

    def connect(self, ip, console=[]):  # 连接控制器
        if self.handle.value is not None:
            self.disconnect()
        ip_bytes = ip.encode('utf-8')
        p_ip = ctypes.c_char_p(ip_bytes)
        print("Connecting to", ip, "...")
        ret = zmcdll.ZMC_OpenEth(p_ip, ctypes.pointer(self.handle))
        msg = "Connected"
        if ret == 0:
            # print("Connected")
            msg = ip + " Connected"
            self.sys_info = self.read_info()
            self.sys_ip = ip
            self.is_connected = True
        else:
            # print("Error", ret)
            msg = "Connection Failed, Error " + str(ret)
            self.is_connected = False
        console.append(msg)
        console.append(self.sys_info)
        return ret

    def disconnect(self):
        ret = zmcdll.ZMC_Close(self.handle)
        self.is_connected = False
        return ret

    def read_info(self):
        cname = ctypes.create_string_buffer(b'', 32)
        fVersion = ctypes.c_float()
        date = ctypes.c_uint32()
        zmcdll.ZMC_GetSoftVersion(self.handle, ctypes.byref(fVersion), ctypes.byref(cname), ctypes.byref(date))
        print("%.2f" % fVersion.value, cname.value, date.value)
        info = cname.value.decode() + " Version:" + str("%.2f" % fVersion.value) + " Date:" + str(date.value)
        print(info)
        return info

    def get_ax_pos(self, ax_num):
        # ZMC_Modbus_Get4x(handle, 11000, imaxaxises*2, (uint16 *)pValueList);
        ax_pos = (ctypes.c_float * ax_num)()
        zmcdll.ZMC_Modbus_Get4x(self.handle, 11000, ax_num * 2, ctypes.byref(ax_pos))  # 读取多个轴的mpos
        return ax_pos

    def set_4x_pos(self, addr, anum):
        # ZMC_Modbus_Get4x(handle, 11000, imaxaxises*2, (uint16 *)pValueList);
        sx_pos = (ctypes.c_ushort * anum)()
        sx_pos[0] = 300
        sx_pos[1] = 400
        sx_pos[2] = 500
        sx_pos[3] = 600

        result = zmcdll.ZMC_Modbus_Set4x(self.handle, addr, anum, ctypes.byref(sx_pos))
        print(*sx_pos)
        return sx_pos

    def get_4x_pos(self, addr, anum):
        gx_pos = (ctypes.c_ushort * anum)()
        result = zmcdll.ZMC_Modbus_Get4x(self.handle, addr, anum, ctypes.byref(gx_pos))
        return gx_pos

    def vmove(self, iaxis, idir):  # 单轴持续运动

        cmdbuffer = (ctypes.c_char * 2048)()
        str1 = "VMOVE(%d) AXIS(%d)" % (idir, iaxis)
        cmd = ctypes.c_char_p(bytes(str1, 'utf-8'))
        zmcdll.ZMC_DirectCommand(self.handle, cmd, cmdbuffer, 2048)
        return

    def get_dpos(self, iaxis):
        cmdbuffer = (ctypes.c_char * 2048)()
        str(cmdbuffer, encoding='utf-8')
        str1 = "?units"
        cmd = ctypes.c_char_p(bytes(str1, 'utf-8'))

        zmcdll.ZMC_DirectCommand(self.handle, cmd, cmdbuffer, 2048)

        a = list(cmdbuffer)

        b = b''.join(a)
        # print(b)
        c = b.decode().strip(b'\x00'.decode())
        return c

        #str(*cmdbuffer, encoding='utf-8')
        #bytes.decode(*cmdbuffer)
        #print(*cmdbuffer)

        print(list[1])


    #it = re.finditer(r"\d+", str1)
    #for match in it:
       #print(match.group())

zmc = ZMCWrapper()

iplist, num = zmc.search()

ip_2048 = "192.168.0.11"
zmc.connect(ip_2048)  # 连接控制器
zmc.read_info()  # 读取控制器信息
pos = zmc.get_ax_pos(2)
print("Axis 0 MPOS:", pos[0])
print("Axis 1 MPOS:", pos[1])

pos1 = zmc.set_4x_pos(0, 5)

pos2 = zmc.get_4x_pos(200, 1)
print(pos2[0])

zmc.vmove(1, 1)
number = zmc.get_dpos(0)
print(number)

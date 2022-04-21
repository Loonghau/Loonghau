import os
import re


def GetMac():
    # Windows下的
    if os.name == 'nt':
        try:
            ret = ''
            CmdLine = 'ipconfig /all'
            r = os.popen(CmdLine).read()
            print(r)
            if r:
                L = re.findall('物理地址.*?([0-9,A-F]{2}-[0-9,A-F]{2}-[0-9,A-F]{2}-[0-9,A-F]{2}-[0-9,A-F]{2}-[0-9,A-F]{2})',
                               r)
                if len(L) > 0:
                    ret = L[0]
        except:
            pass

    # Linux/Unix下
    elif os.name == "posix":
        try:
            ret = ''
            CmdLine = 'ifconfig'
            r = os.popen(CmdLine).read()
            if r:
                L = re.findall(
                    'HWaddr.*?([0-9,A-F]{2}:[0-9,A-F]{2}:[0-9,A-F]{2}:[0-9,A-F]{2}:[0-9,A-F]{2}:[0-9,A-F]{2})', r)
                if len(L) > 0:
                    ret = L[0]
        except:
            pass
    else:
        pass
    return ret


if __name__ == '__main__':
    mac = GetMac()
    print(mac)

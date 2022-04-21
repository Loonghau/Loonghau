# -*- coding: utf-8 -*-
""" 
@Time : 2021/8/13 13:50
@Author : Loonghau XU
@FileName: date_up.py
@SoftWare: PyCharm
"""
import paramiko

# 创建ssh对象
ssh = paramiko.SSHClient()
# ssh.load_host_keys("C:/Users/Administrator/.ssh/known_hosts")
# 允许连接不在know_hosts文件的主机上
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
filename = ['2021-08-09 10-53.xlsx']
# 本地文件路径
for i in filename:
    localpath = "/Users/taihe/Desktop/" + i
    # 服务器的文件路径
    remotepath = "/data/tdc_data/" + i
    # 可设置多台服务器，尽量服务器的密码保持一致
    server = "xxxxxx"
    # words = server.split(",")
    # for word in words:
    # 连接服务器
    print(server, '开始数据传输')
    ssh.connect(server, username="xxxxx", password="xxxxxx")
    sftp = ssh.open_sftp()
    sftp.put(localpath, remotepath, callback=None)
    # 关闭连接
    ssh.close()
    print('数据传输完成')

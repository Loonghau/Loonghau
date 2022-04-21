# -*- coding: utf-8 -*-
""" 
@Time : 2021/12/30 10:41
@Author : Loonghau XU
@FileName: call_UI_gamsyzs.py
@SoftWare: PyCharm
"""
import configparser
import os
import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from UI_logo import Ui_Form_logo
from UI_register import Ui_MainWindow


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("软件注册")  # 窗口名称
        self.setWindowIcon(QIcon('./images/register_04.ico'))
        self.pushButton.clicked.connect(self.mac_get)
        self.action_1.triggered.connect(self.about)

    def mac_get(self):
        mac = self.mac_addres()
        self.lineEdit.setText(mac)
        date_avai = self.dateEdit.date().toString("yyyyMMdd")
        self.date_availability(date_avai, mac)

    def mac_addres(self):
        mac = None
        if sys.platform == 'win32':
            for line in os.popen('ipconfig/all'):
                if line.lstrip().startswith('物理地址'):
                    mac = line.split(':')[1].strip().replace("-", ":").lower()
                    break
        else:
            for line in os.popen('ipconfig/all'):
                if 'Ether' in line:
                    mac = line.split()[4]
                    break
        return mac

    def date_availability(self, date_avai, mac):
        BASE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))
        conf = configparser.RawConfigParser()
        conf.read(os.path.join(BASE_DIR, 'setting_cr.ini'))
        date_avai = int(date_avai)
        date_avai = oct(date_avai)
        date_avai = date_avai[2:]
        conf.set('ABOUT', 'hex_d', date_avai)
        conf.set('ABOUT', 'mac_address', mac)

        with open('setting_cr.ini', 'w') as configfile: conf.write(configfile)

        msg = QMessageBox.information(self,"软件注册","注册成功！",QMessageBox.Yes)
        print(msg)
        if msg == 16384:
            self.close()

    def about(self):
        self.child = LogoWindow()
        self.child.show()


class LogoWindow(QtWidgets.QWidget, Ui_Form_logo):
    def __init__(self, parent=None):
        super(LogoWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())

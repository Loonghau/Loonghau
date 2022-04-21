# -*- coding: utf-8 -*-
""" 
@Time : 2021/8/5 16:56
@Author : Loonghau XU
@FileName: printer.py
@SoftWare: PyCharm
"""
from PyQt5.QtGui import QFont, QTextDocument, QTextCursor
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QSizePolicy, QAction, QDialog
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
import sys

################################################
#######打印文本---《心经》
################################################
the_text = '''
观自在菩萨，行深般若波罗蜜多时，照见五蕴皆空，度一切苦厄。
舍利子，色不异空，空不异色，色即是空，空即是色，受想行识亦复如是。
舍利子，是诸法空相，不生不灭，不垢不净，不增不减。
是故空中无色，无受想行识，无眼耳鼻舌身意，无色声香味触法，无眼界乃至无意识界，无无明亦无无明尽，乃至无老死，亦无老死尽，无苦集灭道，无智亦无得。
以无所得故，菩提萨埵，依般若波罗蜜多故，心无挂碍；无挂碍故，无有恐怖，远离颠倒梦想，究竟涅槃。
三世诸佛，依般若波罗蜜多故，得阿耨多罗三藐三菩提。
故知般若波罗蜜多，是大神咒，是大明咒，是无上咒，是无等等咒，能除一切苦，真实不虚。
故说般若波罗蜜多咒，即说咒曰：揭谛揭谛，波罗揭谛，波罗僧揭谛，菩提萨婆诃。
'''


################################################
#######创建主窗口
################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle(self.tr("打印功能"))

        # 创建文本框
        self.label = QLabel()
        self.label.setFont(QFont("Roman times", 12, QFont.Bold))
        self.label.setText(the_text)
        self.setCentralWidget(self.label)

        # 创建菜单栏
        self.createMenus()

    def createMenus(self):
        # 创建动作一
        self.printAction1 = QAction(self.tr("打印无预留"), self)
        self.printAction1.triggered.connect(self.on_printAction1_triggered)

        # 创建动作二
        self.printAction2 = QAction(self.tr("打印有预留"), self)
        self.printAction2.triggered.connect(self.on_printAction2_triggered)

        # 创建动作三
        self.printAction3 = QAction(self.tr("直接打印"), self)
        self.printAction3.triggered.connect(self.on_printAction3_triggered)

        # 创建动作四
        self.printAction4 = QAction(self.tr("打印到PDF"), self)
        self.printAction4.triggered.connect(self.on_printAction4_triggered)

        # 创建菜单，添加动作
        self.printMenu = self.menuBar().addMenu(self.tr("打印"))
        self.printMenu.addAction(self.printAction1)
        self.printMenu.addAction(self.printAction2)
        self.printMenu.addAction(self.printAction3)
        self.printMenu.addAction(self.printAction4)

    # 动作一：打印，无预览
    def on_printAction1_triggered(self):
        printer = QPrinter()
        printDialog = QPrintDialog(printer, self)
        if printDialog.exec_() == QDialog.Accepted:
            self.handlePaintRequest(printer)

    # 动作二：打印，有预览
    def on_printAction2_triggered(self):
        dialog = QPrintPreviewDialog()
        dialog.paintRequested.connect(self.handlePaintRequest)
        dialog.exec_()

    # 动作三：直接打印
    def on_printAction3_triggered(self):
        printer = QPrinter()
        self.handlePaintRequest(printer)

    # 动作四：打印到pdf
    def on_printAction4_triggered(self):
        printer = QPrinter()
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName("D:/pdf打印测试.pdf")
        self.handlePaintRequest(printer)

    ## 打印函数
    def handlePaintRequest(self, printer):
        document = QTextDocument()
        cursor = QTextCursor(document)
        cursor.insertText(self.label.text())
        document.print(printer)


################################################
#######程序入门
################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

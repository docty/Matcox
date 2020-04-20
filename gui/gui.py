# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 19:20:06 2020

@author: Lenovo G50
"""

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Henry')
window.setGeometry(100,100, 280, 80)
window.move(60,15)
helloMsg = QLabel('<h1>HENRY</h1>', parent=window)
helloMsg.move(60,15)
window.show()
sys.exit(app.exec())
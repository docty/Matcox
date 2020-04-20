from PyQt5 import QtWidgets

from gui.mainscreen import Ui_MainWindow  # importing our generated file

import sys




file = open('./board.mc', 'r')
text = file.read()
file.close()




app = QtWidgets.QApplication([])
window = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window, text)
window.show()
sys.exit(app.exec()) 
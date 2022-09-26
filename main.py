#import sys

from PyQt5 import QtWidgets
from view.homescreen import Ui_MainWindow   
from controller.home import HomeController 






app = QtWidgets.QApplication([]) # Initialise The Application
window = QtWidgets.QMainWindow() # Initialise The Window
ui = Ui_MainWindow()             # Initialise The Main View
ui.setupUi(window)               # Setup The Uis
hc = HomeController(ui)          # Initialise The Home Controller
hc.registerEvents()              # Register All Events
window.show()
app.exec_()



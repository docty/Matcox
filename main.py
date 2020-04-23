import sys

from PyQt5 import QtWidgets
from view.homescreen import Ui_MainWindow   
from controller.home import HomeController 
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

# mathText=r'$\sum^5_3$'
# _figure=Figure()
# _canvas=FigureCanvas(_figure)
# _figure.suptitle(mathText)

# self.layout = QtWidgets.QVBoxLayout(self.centralwidget)
# self.layout.addWidget(_canvas)



app = QtWidgets.QApplication([]) # Initialise The Application
window = QtWidgets.QMainWindow() # Initialise The Window
ui = Ui_MainWindow()             # Initialise The Main View
ui.setupUi(window)               # Setup The Uis
hc = HomeController(ui)          # Initialise The Home Controller
hc.registerEvents()              # Register All Events
window.show()
sys.exit(app.exec())



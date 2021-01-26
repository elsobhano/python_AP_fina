import sys
import os
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QVBoxLayout
import random
import matplotlib
import numpy as np
from time import sleep
import sqlite3
matplotlib.use("Qt5Agg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

form = uic.loadUiType(os.path.join(os.getcwd(),"Form.ui"))[0]
class IntroWindow(QMainWindow,form):
    def __init__(self):
        super(IntroWindow,self).__init__()
        self.setupUi(self)
        self.conn = sqlite3.connect("patient.db")
        self.c = self.conn.cursor()
        self.EntButton.clicked.connect(self.sign_up)
        #self.conn.close()

    def sign_up(self):
        self.c.execute('INSERT INTO patients (First_Name, Last_Name, Password, Phone) VALUES (self.FirstEdit.text(), self.LastEdit.text(), self.PassEdit.text(),self.PhoneEdit.text()); ')
        print(self.c.fetchall())
        self.conn.close()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    w = IntroWindow()
    w.show()
    sys.exit(app.exec_())
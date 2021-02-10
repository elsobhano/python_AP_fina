from os.path import supports_unicode_filenames
import sys
import os
from PyQt5 import uic, QtCore,Qt
from PyQt5.QtWidgets import QApplication,QGroupBox,QRadioButton,QVBoxLayout ,QLineEdit,QLabel ,QWidget,QPushButton, QMainWindow, QVBoxLayout ,QStackedWidget,QTableWidgetItem
from PyQt5.QtGui import QPixmap
import random
import datetime
import matplotlib
from matplotlib.backends.backend_qt5 import MainWindow
import numpy as np
from time import sleep
import sqlite3
form1=uic.loadUiType(os.path.join(os.getcwd(),"DocPortal.ui"))[0]


class DocPort(QMainWindow,form1):
    def __init__(self,input ,parent=None):
        super(DocPort, self).__init__(parent)
        print(input)
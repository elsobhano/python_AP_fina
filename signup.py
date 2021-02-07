import sys
import os
from PyQt5 import uic, QtCore,Qt
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QPushButton, QMainWindow, QVBoxLayout ,QStackedWidget
import random

import matplotlib
from matplotlib.backends.backend_qt5 import MainWindow
import numpy as np
from time import sleep
import sqlite3
matplotlib.use("Qt5Agg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QObject,Signal,Slot
import asyncio
from setAppointment import setAppointmentWindow

form = uic.loadUiType(os.path.join(os.getcwd(),"Form.ui"))[0]
form1=uic.loadUiType(os.path.join(os.getcwd(),"GUI_BASE.ui"))[0]


class Second(QMainWindow,form1):
    def __init__(self, parent=None):
        super(Second, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        

class IntroWindow(QMainWindow,form):
    

    def __init__(self):
        super(IntroWindow,self).__init__()
        self.setupUi(self)
        self.StackWidget.setCurrentIndex(2)
        self.EntButton.setEnabled(False)
        self.EntButton_2.setEnabled(False)
        self.PassEdit.setEchoMode(QLineEdit.Password)
        self.PassEdit.setMaxLength(20)
        self.PassEdit_2.setEchoMode(QLineEdit.Password)
        self.PassEdit_2.setMaxLength(20)
        self.PhoneEdit.setInputMask('99999999999')
        self.PassEdit_2.setMaxLength(20)
        self.PhoneEdit_2.setInputMask('99999999999')
        self.FirstEdit.textEdited.connect(self.validate)
        self.PassEdit.textEdited.connect(self.validate)
        self.LastEdit.textEdited.connect(self.validate)
        self.PhoneEdit.textEdited.connect(self.validate)

        self.PassEdit_2.textEdited.connect(self.validate_2)
        self.PhoneEdit_2.textEdited.connect(self.validate_2)

        self.conn = sqlite3.connect("patient.db")
        self.c = self.conn.cursor()
        self.PatButton.clicked.connect(self.sign1)
        self.DocButton.clicked.connect(self.sign2)
        self.RadioButton.clicked.connect(self.sign3)
        self.EntButton.clicked.connect(self.sign_up)
        self.SignUpButton.clicked.connect(self.go_to_sign_up)
        self.BackButton.clicked.connect(self.go_to_sign_in)
        self.EntButton_2.clicked.connect(self.sign_in)
        # self.conn.close()
    def sign1(self):
        self.id = 1
        self.StackWidget.setCurrentIndex(1)
    def sign2(self):
        self.id = 2
        self.StackWidget.setCurrentIndex(1)
    def sign3(self):
        self.id = 3
        self.StackWidget.setCurrentIndex(1)
    def sign_up(self):
        self.c.execute("SELECT * FROM patients")
        print(self.c.fetchall())
        sql = "INSERT INTO patients (First_Name, Last_Name,Password,Phone) VALUES (?,?,?,?)"
        val = (self.FirstEdit.text(), self.LastEdit.text(),self.PassEdit.text(),self.PhoneEdit.text())
        print(val)
        self.c.execute(sql, val)
        self.c.execute("SELECT * FROM patients")
        print(self.c.fetchall())
        self.conn.commit()
        self.conn.close()
        self.StackWidget.setCurrentIndex(1)

    def sign_in(self):
        self.conn = sqlite3.connect("patient.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM patients")
        check = self.c.fetchall()
        self.LoadingLabel.setText('Loading ... ')
        flag = False
        for i in check:
            if i[3]==self.PhoneEdit_2.text() and i[2]==self.PassEdit_2.text():
                self.Name_User = i[0] + ' ' + i[1]
                self.Phone_User = i[3]
                print(self.Name_User)
                print(self.Phone_User)
                flag = True
            
        if flag :
            self.signInOk = True
            self.close()
            
            
            
        else:
            self.signInNotOk = False
            self.LoadingLabel.setText('nOk')
                 
        self.conn.close()


    def validate(self):
        if (self.FirstEdit.text() != '' and self.LastEdit.text() != '' and self.PassEdit.text() != '' and self.PhoneEdit.hasAcceptableInput()):
            self.EntButton.setEnabled(True)
        else :
            self.EntButton.setEnabled(False)

    def validate_2(self):
        if (self.PassEdit_2.text() != '' and self.PhoneEdit_2.hasAcceptableInput()):
            self.EntButton_2.setEnabled(True)
        else :
            self.EntButton_2.setEnabled(False)

    def go_to_sign_up(self):
        self.StackWidget.setCurrentIndex(0)

    def go_to_sign_in(self):
        self.StackWidget.setCurrentIndex(1)

class addAppointmentWindow(QObject):
    def __init__(self,User_Name,User_Phone):
        QObject.__init__(self)
        self.User_Name = User_Name
        self.User_Phone = User_Phone

    async def showAppointmentWindow(self):
        # app = QApplication(sys.argv)
        # app.setStyle("Fusion")
        w = setAppointmentWindow()
        w.show()
        # app.exec_() 

    @Slot()
    def openAppointment(self):
        w = setAppointmentWindow(self.User_Name,self.User_Phone)
        w.show()
        #TODO : درست کردن آسینک آیو
        app = asyncio.get_running_loop()
        app.run_in_executor()
        # loop=asyncio.new_event_loop()
        # loop.run_until_complete(self.showAppointmentWindow())

    setName = Signal(str)
    setPhone = Signal(str)

    @Slot()
    def setUserName(self):
        self.setName.emit(self.User_Name)  


async def runSignUp():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    w = IntroWindow()
    w.show()
    app.exec_()
    return w.Name_User,w.Phone_User
    

async def runPortal(Name_User,Phone_User):
    app = QApplication(sys.argv)     
    engine = QQmlApplicationEngine()
    
    #Get context
    main = addAppointmentWindow(Name_User,Phone_User)
    engine.rootContext().setContextProperty("backend",main)
    
    
    engine.load(os.path.join(os.path.dirname(__file__), "FINAL/qml/main.qml"))
    main.setName.emit(Name_User)
    if not engine.rootObjects():
        sys.exit(-1)

    
    app.exec_()

loop = asyncio.get_event_loop()
Name_User,Phone_User=(loop.run_until_complete(runSignUp()))
print(loop.run_until_complete(runPortal(Name_User,Phone_User)))
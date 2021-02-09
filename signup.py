from os.path import supports_unicode_filenames
import sys
import os
from PyQt5 import uic, QtCore,Qt
from PyQt5.QtWidgets import QApplication,QLabel ,QLineEdit, QWidget, QPushButton, QMainWindow, QVBoxLayout ,QStackedWidget
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
from PySide2.QtCore import QObject,Signal,Slot,QDir,QAbstractTableModel
from PySide2.QtSql import QSqlDatabase, QSqlQuery, QSqlRecord, QSqlTableModel
import logging
import asyncio
from setAppointment import setAppointmentWindow
from PatientPortal import PatPort

logging.basicConfig(filename="chat.log", level=logging.DEBUG)
logger = logging.getLogger("logger")

form = uic.loadUiType(os.path.join(os.getcwd(),"Form.ui"))[0]

        

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
        print(self.id)
    def sign2(self):
        self.id = 2
        self.StackWidget.setCurrentIndex(1)
        print(self.id)
    def sign3(self):
        self.id = 3
        self.StackWidget.setCurrentIndex(1)
        print(self.id)
    def sign_up(self):
        if self.id == 1:
            print('Im a patient')
            self.conn = sqlite3.connect("patient.db")
            self.c = self.conn.cursor()
            self.c.execute("SELECT * FROM patients")
            sql = "INSERT INTO patients (First_Name, Last_Name,Password,Phone) VALUES (?,?,?,?)"
            val = (self.FirstEdit.text(), self.LastEdit.text(),self.PassEdit.text(),self.PhoneEdit.text())
        elif self.id == 2:
            print('Im a doctor')
            self.conn = sqlite3.connect("doctor.db")
            self.c = self.conn.cursor()
            self.c.execute("SELECT * FROM doctors")
            sql = "INSERT INTO doctors (Name, Family,Password,Phone) VALUES (?,?,?,?)"
            val = (self.FirstEdit.text(), self.LastEdit.text(),self.PassEdit.text(),self.PhoneEdit.text())
        elif self.id == 3:
            print('Im a radiology')
            self.conn = sqlite3.connect("patient.db")
            self.c = self.conn.cursor()
            self.c.execute("SELECT * FROM patients")
            sql = "INSERT INTO patients (First_Name, Last_Name,Password,Phone) VALUES (?,?,?,?)"
            val = (self.FirstEdit.text(), self.LastEdit.text(),self.PassEdit.text(),self.PhoneEdit.text())
        self.c.execute(sql, val)
        self.conn.commit()
        self.conn.close()
        self.StackWidget.setCurrentIndex(1)
    # async def secondwindow():
        

    def sign_in(self):
        if self.id == 1:
            self.conn = sqlite3.connect("patient.db")
            self.c = self.conn.cursor()
            self.c.execute("SELECT * FROM patients")
        elif self.id == 2:
            self.conn = sqlite3.connect("doctor.db")
            self.c = self.conn.cursor()
            self.c.execute("SELECT * FROM doctors")
        elif self.id == 3:
            self.conn = sqlite3.connect("patient.db")
            self.c = self.conn.cursor()
            self.c.execute("SELECT * FROM patients")
        self.LoadingLabel.setText('Loading ... ')
        flag = False
        check = self.c.fetchall()
        for i in check:
            print('-----------------------------')
            if i[3]==self.PhoneEdit_2.text() and i[2]==self.PassEdit_2.text():
                print(i[0])
                print(i[1])
                self.Name_User = i[0] + ' ' + i[1]
                self.Phone_User = i[3]
                print(self.Name_User)
                print(self.Phone_User)
                self.tup = i
                flag = True
        if flag :
            self.signInOk = True
            self.hide()
            self.showSecondWindow()
            # loop=asyncio.new_event_loop()
            # loop.run_until_complete(secondwindow())

            
            
        else:
            self.signInNotOk = False
            self.LoadingLabel.setText('nOk')
                 
        self.conn.close()

    def showSecondWindow(self):
        self.w=PatPort(self.tup)
        self.w.show()
        

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



# class SqlConversionModel(QSqlTableModel):
#     def __init__(self,parent=None):
#         super(SqlConversionModel,self).__init__(parent)


# def testQuery():
#     query = QSqlQuery("")












async def runSignUp():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    w = IntroWindow()
    w.show()
    
    app.exec_()
    return w.Name_User,w.Phone_User
    

def getUserAppointments(Phone_User):
    conn = sqlite3.connect("appoinment.db")
    c = conn.cursor()
    c.execute("SELECT * FROM appoinments WHERE Pat_phone = '{}' ORDER BY date(Date) DESC,CAST(Time AS INTEGER) DESC".format(Phone_User))
    reserve = c.fetchall()
    return reserve


def createTable():
    if table_name in QSqlDatabase.database().tables():
        return

    query = QSqlQuery()
    if not query.exec_(
        """
        CREATE TABLE IF NOT EXISTS 'Conversations' (
            'author' TEXT NOT NULL,
            'recipient' TEXT NOT NULL,
            'timestamp' TEXT NOT NULL,
            'message' TEXT NOT NULL,
        FOREIGN KEY('author') REFERENCES Contacts ( name ),
        FOREIGN KEY('recipient') REFERENCES Contacts ( name )
        )
        """
    ):
        logging.error("Failed to query database")

    # This adds the first message from the Bot
    # and further development is required to make it interactive.
    query.exec_(
        """
        INSERT INTO Conversations VALUES(
            'machine', 'Me', '2019-01-07T14:36:06', 'Hello!'
        )
        """
    )
    logging.info(query)



class appointmentModel(QAbstractTableModel):
    def __init__(self,data):
        super(appointmentModel,self).__init__()
        self._data=data
        
        
        
    def data(self, index, role):
        # See below for the nested-list data structure.
        # .row() indexes into the outer list,
        # .column() indexes into the sub-list
        return self._data[index.row()][index.column()]


    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])    
        
        

async def runPortal(Name_User,Phone_User):
    app = QApplication(sys.argv)     
    engine = QQmlApplicationEngine()


    print(getUserAppointments(Phone_User))
    


    #Get context
    main = addAppointmentWindow(Name_User,Phone_User)
    engine.rootContext().setContextProperty("backend",main)
    appointment=appointmentModel(getUserAppointments(Phone_User))
    engine.rootContext().setContextProperty("appointmentModel",appointment)
    dataList = ({"doc_name":"دکتر جهانشاهی"},{"doc_name":"دکتر اساسی"},{"doc_name":"دکتر هاشمی"})

    # view = QQuickView()
    # view.setResizeMode(QQuickView.SizeRootObjectToView)
    # view.setInitialProperties( "SetAppointmentListModel", QVariant.fromValue(dataList) )
    engine.load(os.path.join(os.path.dirname(__file__), "FINAL/qml/main.qml"))
    main.setName.emit(Name_User)
    if not engine.rootObjects():
        sys.exit(-1)

    
    app.exec_()

loop = asyncio.get_event_loop()
Name_User,Phone_User=(loop.run_until_complete(runSignUp()))
# Name_User="امــــــیدرزاقی"
# Phone_User="09156549973"
# print(loop.run_until_complete(runPortal(Name_User,Phone_User)))




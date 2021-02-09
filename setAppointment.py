import sys
import os
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QVBoxLayout, QGridLayout
import random
import matplotlib
import numpy as np
from time import sleep
import datetime
import calendar
import sqlite3
matplotlib.use("Qt5Agg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from PySide2.QtCore import Signal,Slot,QObject

form = uic.loadUiType(os.path.join(os.getcwd(),"setAppointment.ui"))[0]
class setAppointmentWindow(QMainWindow,form):
    
    def __init__(self,Name,Phone,updateSignal,appo_context):
        super(setAppointmentWindow,self).__init__()
        
        
        self.setupUi(self)
        self.name=Name
        self.phone=Phone
        self.updateSignal=updateSignal
        self.appo_context=appo_context
        self.calendarWidget.selectionChanged.connect(self.Doctor)
        self.Doc_Box.currentTextChanged.connect(self.date1)
        self.Time_Box.currentTextChanged.connect(self.Set_Time)
        self.appo_Button.clicked.connect(self.Set_appo)
        self.flag1 = False
        self.Doc_Name = []
        if self.flag1==False:
            
            self.conn = sqlite3.connect("doctor.db")
            self.c = self.conn.cursor()
            self.c.execute("SELECT * FROM doctors")
            Docs = self.c.fetchall()
            print(Docs)
            self.Doc_Box.clear()
            self.Doc_Box.addItem('Choose A Doctor')
            for i in Docs:
                self.Doc_Box.addItem(i[0]+' '+i[1])
                self.Doc_Name.append(i[0]+' '+i[1])
            
            self.conn.close()
            self.flag1=True

    def sign_up(self):
        self.conn = sqlite3.connect("patient.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM patients")
        print(self.c.fetchall())
        sql = "INSERT INTO patients (First_Name, Last_Name,Password,Phone) VALUES (?,?,?,?)"
        val = (self.FirstEdit.text(), self.LastEdit.text(),self.PassEdit.text(),self.PhoneEdit.text())
        print(val)
        try:
            self.c.execute(sql, val)
            
        except sqlite3.Error:
            self.ErrorLabel.setText('This Phone Number is already exist')
        self.c.execute("SELECT * FROM patients")
        print(self.c.fetchall())
        self.conn.commit()
        self.conn.close()

    def date1(self):
        self.date = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")
        self.Check_Label.setText('')
        self.doctor = self.Doc_Box.currentText()
        self.Time_Box.clear()
        if self.doctor in self.Doc_Name:
            print('-------------------')
            self.conn = sqlite3.connect("doctor.db")
            self.c = self.conn.cursor()
            x = self.doctor.split()
            print(x)
            print(self.doctor)
            print(x[0],x[1])
            self.c.execute('SELECT * FROM doctors WHERE Name = "{}" and Family = "{}";'.format(x[0],x[1]))
            info = self.c.fetchall()
            print(info)
            information = "Name: Doctor " + info[0][0]+' '+info[0][1] + '\n' + 'Resume: ' + info[0][4]
            self.textEdit.setPlaceholderText(information)
            print(self.doctor)
            self.Time_Box.clear()
            self.conn.close()
            self.Time_Box.clear()
            time = ['9','10','11','12','13','15','16','17','18']
            t = datetime.datetime.now().strftime('%H')
            d = datetime.datetime.now().strftime('%Y-%m-%d')
            newtime = []
            if d == self.date:
                for i in time:
                    if int(i)>int(t):
                        newtime.append(i)
                time = newtime  
            self.conn = sqlite3.connect("appoinment.db")
            self.c = self.conn.cursor()
            self.c.execute("SELECT * FROM appoinments")
            Times = self.c.fetchall()
            for i in Times:
                if i[0] == self.date   and i[2] == self.doctor:
                    time.remove(i[1])
            if len(time) == 0:
                self.Check_Label.setText('This Doctor has No Time On This Day')
            for i in time:
                self.Time_Box.addItem(i)
            self.conn.close()
        else:
            self.textEdit.setPlaceholderText('Choose the doctor')
            self.conn.close()

    def Doctor(self):
        self.Check_Label.setText('')
        self.date = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")
        print('YES')
        print(self.doctor)
        if self.doctor in self.Doc_Name:
            self.Time_Box.clear()
            time = ['9','10','11','12','13','15','16','17','18']
            t = datetime.datetime.now().strftime('%H')
            d = datetime.datetime.now().strftime('%Y-%m-%d')
            newtime = []
            if d == self.date:
                for i in time:
                    if int(i)>int(t):
                        newtime.append(i)
                time = newtime   
            self.conn = sqlite3.connect("appoinment.db")
            self.c = self.conn.cursor()
            self.c.execute("SELECT * FROM appoinments")
            Times = self.c.fetchall()
            for i in Times:
                if i[0] == self.date   and i[2] == self.doctor:
                    time.remove(i[1])
            if len(time) == 0:
                self.Check_Label.setText('This Doctor has No Time On This Day')
            for i in time:
                self.Time_Box.addItem(i)
            self.conn.close()

    def Set_Time(self):
        self.appo_Button.setEnabled(True)
        
    
    
    
    def  Set_appo(self):
        self.time = self.Time_Box.currentText()
        self.conn = sqlite3.connect("appoinment.db")
        self.c = self.conn.cursor()
        sql = "INSERT INTO appoinments (Date, Time,Doc_Name,Pat_Name,Pat_phone) VALUES (?,?,?,?,?)"
        val = (self.date, self.time,self.doctor,self.name,self.phone)
        print(val)
        self.c.execute(sql, val)
        self.conn.commit()
        self.conn.close()
        
        
        self.appo_context.updateData()
        
        self.Time_Box.clear()
        self.Doc_Box.setCurrentText('Choose A Doctor')

       

        


        
        


        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    w = setAppointmentWindow()
    w.show()
    sys.exit(app.exec_())
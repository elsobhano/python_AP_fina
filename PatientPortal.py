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
form1=uic.loadUiType(os.path.join(os.getcwd(),"PatPortal.ui"))[0]


class PatPort(QMainWindow,form1):
    def __init__(self,input ,parent=None):
        super(PatPort, self).__init__(parent)
        print(input)
        self.setupUi(self)
        self.firstlabel.setText(input[0])
        self.lastlabel.setText(input[1])
        self.phonelabel.setText(input[3])
        self.name = input[0] + ' ' + input[1]
        self.phone = input[3]
        self.imagepath = './images/pat_images/' + input[5]
        print(self.imagepath)
        self.pixmap = QPixmap(self.imagepath)
        self.piclabel.setScaledContents(True)
        self.piclabel.setPixmap(self.pixmap)
        self.updateButton.clicked.connect(self.update)
        self.resumelabel.setText(input[4])
        # tabel of appointments
        
        t = datetime.datetime.now()
        self.conn = sqlite3.connect("appoinment.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM appoinments WHERE Pat_phone = '{}' ORDER BY date(Date) DESC,CAST(Time AS INTEGER) DESC".format(self.phone))
        reserve = self.c.fetchall()
        self.tableWidget.setRowCount(len(reserve))
        i = 0
        k = 0
        for m in reserve:
            self.tableWidget.setItem(i,0, QTableWidgetItem(m[0]))
            self.tableWidget.setItem(i,1, QTableWidgetItem(m[1]))
            self.tableWidget.setItem(i,2, QTableWidgetItem(m[2]))
            date_str = m[0]+' '+m[1]
            date_reserve = datetime.datetime.strptime(date_str,'%Y-%m-%d %H')
            if date_reserve<t:
                self.tableWidget.setItem(i,3, QTableWidgetItem('Finished'))
                k = k + 1
            i = i + 1
        self.numlabel.setText(str(k))
        self.conn.close()
        #نوبت گیری
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
        #سوابق
        self.conn = sqlite3.connect("savabegh.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM savabeghs WHERE Phone = '{}' ORDER BY date(Date) DESC,CAST(Time AS INTEGER) DESC".format(self.phone))
        record = self.c.fetchall()
        self.conn.close()
        num = 0
        for i in record:
            self.grid.addWidget(self.createExampleGroup(i[0],i[1],i[2],i[5],i[6]), num, 0)
            num = num + 1
        #پیام ها
        self.conn = sqlite3.connect("message.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM messages WHERE PatPhone = '{}' ORDER BY date(Date) DESC,CAST(Time AS INTEGER) DESC".format(self.phone))
        record = self.c.fetchall()
        self.conn.close()
        num = 0
        for i in record:
            self.grid2.addWidget(self.createExampleGroup1(i[0],i[1],i[2],i[5]), num, 0)
            num = num + 1
    def update(self):
        t = datetime.datetime.now()
        self.conn = sqlite3.connect("appoinment.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM appoinments WHERE Pat_phone = '{}' ORDER BY date(Date) DESC,CAST(Time AS INTEGER) DESC".format(self.phone))
        reserve = self.c.fetchall()
        self.tableWidget.setRowCount(len(reserve))
        i = 0
        k = 0
        for m in reserve:
            self.tableWidget.setItem(i,0, QTableWidgetItem(m[0]))
            self.tableWidget.setItem(i,1, QTableWidgetItem(m[1]))
            self.tableWidget.setItem(i,2, QTableWidgetItem(m[2]))
            date_str = m[0]+' '+m[1]
            date_reserve = datetime.datetime.strptime(date_str,'%Y-%m-%d %H')
            if date_reserve<t:
                print(t)
                print(date_reserve)
                self.tableWidget.setItem(i,3, QTableWidgetItem('Finished'))
                k = k + 1
            else:
                self.tableWidget.setItem(i,3, QTableWidgetItem(''))
                k = k + 1
            i = i + 1
        self.numlabel.setText(str(k))
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
            if len(time) != 0:
                self.conn = sqlite3.connect("appoinment.db")
                self.c = self.conn.cursor()
                self.c.execute("SELECT * FROM appoinments")
                Times = self.c.fetchall()
                for i in Times:
                    if i[0] == self.date  and i[2] == self.doctor:
                        print(i[1])
                        if i[1] in time:
                            time.remove(i[1])
                if len(time) == 0:
                    self.Check_Label.setText('This Doctor has No Time On This Day')
                for i in time:
                    self.Time_Box.addItem(i)
                self.conn.close()
            else:
                self.Check_Label.setText('Clinic is Closed')
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
            if len(time) != 0:   
                self.conn = sqlite3.connect("appoinment.db")
                self.c = self.conn.cursor()
                self.c.execute("SELECT * FROM appoinments")
                Times = self.c.fetchall()
                for i in Times:
                    if i[0] == self.date   and i[2] == self.doctor:
                        if i[1] in time:
                            time.remove(i[1])
                if len(time) == 0:
                    self.Check_Label.setText('This Doctor has No Time On This Day')
                for i in time:
                    self.Time_Box.addItem(i)
            else:
                self.Check_Label.setText('Clinic is Closed')
            self.conn.close()

    def Set_Time(self):
        #self.appo_Button.setEnabled(True)
        pass
       

    def  Set_appo(self):
        if self.doctor!= 'Choose A Doctor':
            self.time = self.Time_Box.currentText()
            self.conn = sqlite3.connect("appoinment.db")
            self.c = self.conn.cursor()
            sql = "INSERT INTO appoinments (Date, Time,Doc_Name,Pat_Name,Pat_phone) VALUES (?,?,?,?,?)"
            val = (self.date, self.time,self.doctor,self.name,self.phone)
            print(val)
            self.c.execute(sql, val)
            self.conn.commit()
            self.conn.close()
            self.Time_Box.clear()
            self.Doc_Box.setCurrentText('Choose A Doctor')
        else:
            self.Check_Label.setText('First Choose A Doctor!')


    def createExampleGroup1(self,date,time,doc,dis):
        
        groupBox = QGroupBox('Date: '+date + '   Time : '+time)
        label1 = QLabel("Doctor: " + doc)
        label2 = QLabel("Discription: " + dis)
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)    
        vbox.addStretch(1)
        groupBox.setLayout(vbox)
        return groupBox
    def createExampleGroup(self,date,time,doc,dis,file):
        
        groupBox = QGroupBox('Date: '+date + '   Time : '+time)
        label1 = QLabel("Doctor: " + doc)
        label2 = QLabel("Discription: " + dis)

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        if file != '':
            self.pic1 = QLabel(self)
            self.pixmap1 = QPixmap('./img/'+file)
            self.pic1.setPixmap(self.pixmap1)
            self.pic1.resize(self.pixmap1.width(), self.pixmap1.height())
            vbox.addWidget(self.pic1)
            vbox.addStretch(1)
        groupBox.setLayout(vbox)
        return groupBox
    

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    w = PatPort(("Sobhan","Asasi"," ","09156549973"))
    w.show()
    sys.exit(app.exec_())
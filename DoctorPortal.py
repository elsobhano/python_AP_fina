from os.path import supports_unicode_filenames
import sys
import os
from PyQt5 import uic, QtCore,Qt
from PyQt5.QtWidgets import QApplication,QGroupBox,QRadioButton,QVBoxLayout ,QLineEdit,QLabel ,QWidget,QPushButton, QMainWindow, QVBoxLayout ,QStackedWidget,QTableWidgetItem
from PyQt5.QtGui import QPixmap
<<<<<<< HEAD
from PyQt5.QtCore import QDate
=======
from PyQt5.QtCore import QTime,QDate
>>>>>>> d241dd6e52a1cfd4b63423deff092add220273f6
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
        self.setupUi(self)
        self.updateButton.clicked.connect(self.update)
        self.doc_completeName=input[0]+' '+input[1]
        self.setupConnectionsOfChatTab()
        #TODO:DateEdit default today date
        print(input)
        self.firstlabel.setText(input[0])
        self.lastlabel.setText(input[1])
        self.phonelabel.setText(input[3])
        self.name = input[0] + ' ' + input[1]
        self.phone = input[3]
        self.imagepath = './images/doc_images/' + input[5]
        print(self.imagepath)
        self.pixmap = QPixmap(self.imagepath)
        self.piclabel.setScaledContents(True)
        self.piclabel.setPixmap(self.pixmap)
        self.resumelabel.setText(input[4])
        d = QDate.currentDate()
        self.dateEdit.setDate(d)
    def update(self):
        print('Here')
        self.tableWidget.setRowCount(0)
        self.tabdate = self.dateEdit.date().toString("yyyy-MM-dd")
        self.conn = sqlite3.connect("appoinment.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM appoinments WHERE Doc_Name = '{}' AND Date = '{}' ORDER BY date(Date) DESC,CAST(Time AS INTEGER) DESC".format(self.name,self.tabdate))
        reserve = self.c.fetchall()
        self.conn.close()
        self.tableWidget.setRowCount(len(reserve))
        i = 0
        k = 0
        t = datetime.datetime.now()
        for m in reserve:
            self.tableWidget.setItem(i,0, QTableWidgetItem(m[0]))
            self.tableWidget.setItem(i,1, QTableWidgetItem(m[1]))
            self.tableWidget.setItem(i,2, QTableWidgetItem(m[3]))
            date_str = m[0]+' '+m[1]
            date_reserve = datetime.datetime.strptime(date_str,'%Y-%m-%d %H')
            if date_reserve<t:
                self.tableWidget.setItem(i,3, QTableWidgetItem('Finished'))
                k = k + 1
            i = i + 1

    def setupConnectionsOfChatTab(self):
        patNamesList=[]
        self.patInfoList=self.getPatients(self.doc_completeName)
        for i in self.patInfoList:
            patNamesList.append(i[0])
        self.pat_comboBox.addItems(patNamesList)
        self.sendBtn.clicked.connect(self.sendMessage)
        
    
    def getPatients(self,doc_name_familyname):
        conn = sqlite3.connect("appoinment.db")
        c = conn.cursor()
        c.execute("SELECT * FROM appoinments WHERE Doc_Name = '{}' ORDER BY date(Date) DESC,CAST(Time AS INTEGER) DESC".format(doc_name_familyname))
        output = c.fetchall()
        patientList=[]
        for i in output:
            if (i[3],i[4]) not in patientList:
                patientList.append((i[3],i[4]))
        c.close()
        return patientList

    def sendMessage(self):
        if(self.msg_lineEdit.text != '' and self.pat_comboBox.currentText() != ''):
            self.addToMessageDatabase()
            self.msg_lineEdit.clear()
            
    def addToMessageDatabase(self):
        conn = sqlite3.connect("message.db")
        c = conn.cursor()
        t = QTime()
        d = QDate()
        sql = "INSERT INTO messages (Date, Time,Doc,Pat,PatPhone,Payam) VALUES (?,?,?,?,?,?)"
        val = (d.currentDate().toString("yyyy-MM-dd"), (t.currentTime().toString()),self.doc_completeName,self.pat_comboBox.currentText(),self.patInfoList[self.pat_comboBox.currentIndex()][1],self.msg_lineEdit.text())
        print(val)
        c.execute(sql,val)
        conn.commit()
        c.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    w = DocPort(("Amir","Jahanshahi","123","09153109973","Jarah","defaultImage.jpg"))
    w.show()
    sys.exit(app.exec_())
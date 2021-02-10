from os.path import supports_unicode_filenames
import sys
import os
from PyQt5 import uic, QtCore,Qt
from PyQt5.QtWidgets import QApplication,QGroupBox,QRadioButton,QVBoxLayout ,QLineEdit,QLabel ,QWidget,QPushButton, QMainWindow, QVBoxLayout ,QStackedWidget,QTableWidgetItem
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTime,QDate
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
        self.doc_completeName=input[0]+' '+input[1]
        self.setupConnectionsOfChatTab()
        #TODO:DateEdit default today date
        print(input)

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
    w = DocPort(("Majid","Samiei","123","09153109973","resume","defaultImage.jpg"))
    w.show()
    sys.exit(app.exec_())
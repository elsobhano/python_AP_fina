from os.path import supports_unicode_filenames
import sys
import os
from PyQt5 import uic, QtCore,Qt
from PyQt5.QtWidgets import QApplication,QGroupBox,QRadioButton,QVBoxLayout ,QLineEdit,QLabel ,QWidget,QPushButton, QMainWindow, QVBoxLayout ,QStackedWidget,QTableWidgetItem
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QDate
from PyQt5.QtCore import QTime,QDate
import random
import datetime
import matplotlib
from matplotlib.backends.backend_qt5 import MainWindow
import numpy as np
from time import sleep
import sqlite3
form1=uic.loadUiType(os.path.join(os.getcwd(),"DocPortal.ui"))[0]
new = uic.loadUiType(os.path.join(os.getcwd(), "new.ui"))[0]


conn = sqlite3.connect('savabegh.db')
c = conn.cursor()

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
        num = self.num_patient()
        self.firstlabel.setText(str(num))
        print(self.imagepath)
        self.pixmap = QPixmap(self.imagepath)
        self.piclabel.setScaledContents(True)
        self.piclabel.setPixmap(self.pixmap)
        self.resumelabel.setText(input[4])
        d = QDate.currentDate()
        self.dateEdit.setDate(d)
        #savabegh
        self.doc = input[0] + input[1]
        self.username_lineEdit.textChanged.connect(self.search)
        self.date_comboBox.currentTextChanged.connect(self.show_prescription)
        self.pres_textEdit.setReadOnly(True)
        self.doc_lineEdit.setEnabled(False)
        self.new_Button.clicked.connect(self.show_window)

        
        #پیام ها
        self.pat_comboBox.currentTextChanged.connect(self.updateMessagesGrid)
        self.messageConn=sqlite3.connect("message.db")
        self.messageC = self.messageConn.cursor()
        self.messageC.execute("SELECT * FROM messages WHERE Doc = '{}' AND Pat = '{}' ORDER BY date(Date) DESC,Time DESC".format(self.doc_completeName,self.pat_comboBox.currentText()))
        messages = self.messageC.fetchall()
        self.messageConn.close()
        num = 0 
        for i in messages:
            self.grid2.addWidget(self.createExampleGroup1(i[0],i[1],i[3],i[5]),num,0) 
            num=num+1
    def num_patient(self):
        phones = []
        conn = sqlite3.connect("appoinment.db")
        c = conn.cursor()
        c.execute("SELECT * FROM appoinments")
        total = c.fetchall()
        for i in total:
            if i[4] not in phones:
                phones.append(i[4])
        return(len(phones))
    def updateMessagesGrid(self):
        print(self.grid2.rowCount())
        
        for i in reversed(range(self.grid2.count())): 
            self.grid2.itemAt(i).widget().setParent(None)
        self.messageConn=sqlite3.connect("message.db")
        self.messageC = self.messageConn.cursor()
        self.messageC.execute("SELECT * FROM messages WHERE Doc = '{}' AND Pat = '{}' ORDER BY date(Date) DESC,Time DESC".format(self.doc_completeName,self.pat_comboBox.currentText()))
        messages = self.messageC.fetchall()
        self.messageConn.close()
        num = 0 
        for i in messages:
            self.grid2.addWidget(self.createExampleGroup1(i[0],i[1],i[3],i[5]),num,0) 
            num=num+1


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
#################################################################
    def search(self, val):
        
        c.execute(f'SELECT Date FROM savabeghs WHERE Phone == "{val}";')
        dates = c.fetchall()
        
        d = []
        for date in dates:
            d.append(date[0])
        self.date_comboBox.clear()
        self.date_comboBox.addItems(d)



    def show_prescription(self, val):
        username = self.username_lineEdit.text()
        c.execute(f'SELECT Discript FROM savabeghs WHERE Phone == "{username}" AND Date == "{val}";')
        pres = c.fetchall()
        c.execute(f'SELECT Doc FROM savabeghs WHERE Phone == "{username}" AND Date == "{val}";')
        doc_name = c.fetchall()
        c.execute(f'SELECT Pat FROM savabeghs WHERE Phone == "{username}" AND Date == "{val}";')
        name = c.fetchall()
        c.execute(f'SELECT Pic FROM savabeghs WHERE Phone == "{username}" AND Date == "{val}";')
        img = c.fetchall()
        self.doc_lineEdit.clear()
        self.pres_textEdit.clear()
        self.name_lineEdit.clear()
        try:
            self.doc_lineEdit.setText(doc_name[0][0])
            self.pres_textEdit.setText(pres[0][0])
            self.name_lineEdit.setText(name[0][0])
            img_path = f'img/{img[0][0]}.jpg'
            if os.path.isfile(img_path):
                pixmap = QPixmap(img_path)
                self.img_lable.setScaledContents(True)
                self.img_lable.setPixmap(pixmap)
        except:
            pass

    def show_window(self):
        self.w = NewWindow()
        self.w.show()
        self.w.user_name = self.username_lineEdit.text()
        self.w.n_lineEdit.setText(self.name_lineEdit.text())
        self.w.doctor_lineEdit.setText(self.doc)
        self.w.n_lineEdit.setEnabled(False)




###############################################################################################        
    def update(self):
        print('Here')
        self.tableWidget.setRowCount(0)
        self.tabdate = self.dateEdit.date().toString("yyyy-MM-dd")
        self.conn = sqlite3.connect("appoinment.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM appoinments WHERE Doc_Name = '{}' AND Date = '{}' ORDER BY date(Date) DESC,Time DESC".format(self.name,self.tabdate))
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
        c.execute("SELECT * FROM appoinments WHERE Doc_Name = '{}' ORDER BY date(Date) DESC,Time DESC".format(doc_name_familyname))
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
            self.updateMessagesGrid()
            
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

class NewWindow(QMainWindow,new):
    def __init__(self):
        super(NewWindow, self).__init__()
        self.setupUi(self)
        self.img_path = ''
        self.user_name = ''

        now = datetime.datetime.now()
        self.date = now.strftime("%Y-%m-%d")
        self.time = now.strftime("%H:%M")
        print(self.date)
        print(self.time)
        self.p_textEdit.setPlaceholderText("لطفا نسخه ی خود را تایپ کنید")
        self.d_lineEdit.setText(self.date)
        self.load_Button.clicked.connect(self.show_img)
        self.save_Button.clicked.connect(self.save)

    def show_img(self):
        self.img_path, _ = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Image files (*.jpg *.gif)")
        pixmap = QPixmap(self.img_path)
        self.image_View.setScaledContents(True)
        self.image_View.setPixmap(pixmap)
        
    def save(self):
        name = self.n_lineEdit.text()
        doc_name = self.doctor_lineEdit.text()
        pres = self.p_textEdit.toPlainText()
        img_str = ''
        if self.img_path != '':
            img_str = name + '_' + self.date
            img = Image.open(self.img_path)
            img.save('img/' + img_str + '.jpg')
        
        c.execute(f'INSERT INTO savabeghs(Date, Time, Doc, Pat, Phone, Discript, Pic) VALUES ("{self.date}", "{self.time}", "{doc_name}", "{name}", "{self.user_name}", "{pres}", "{img_str}")')
        c.fetchall()
        conn.commit()
        self.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    w = DocPort(("Amir","Jahanshahi","123","09153109973","Jarah","defaultImage.jpg"))
    w.show()
    sys.exit(app.exec_())
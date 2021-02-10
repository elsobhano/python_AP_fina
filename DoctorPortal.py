import sys
import os
import sqlite3
import random
import datetime
import matplotlib
import numpy as np
from PIL import Image
from time import sleep
from os.path import supports_unicode_filenames
from PyQt5 import uic, QtCore,Qt
from PyQt5.QtWidgets import QApplication, QGroupBox, QRadioButton, QVBoxLayout, QLineEdit,QLabel, QWidget,QPushButton, QMainWindow, QVBoxLayout, QStackedWidget, QTableWidgetItem, QFileDialog
from PyQt5.QtGui import QPixmap
from matplotlib.backends.backend_qt5 import MainWindow

form1=uic.loadUiType(os.path.join(os.getcwd(),"DocPortal.ui"))[0]
new = uic.loadUiType(os.path.join(os.getcwd(), "new.ui"))[0]

conn = sqlite3.connect('savabegh.db')
c = conn.cursor()

class DocPort(QMainWindow,form1):
    def __init__(self,input ,parent=None):
        super(DocPort, self).__init__(parent)
        self.setupUi(self)

        #TODO:DateEdit default today date
        print(input[0])

        #سوابق
        self.doc = input[0] + input[1]
        self.username_lineEdit.textChanged.connect(self.search)
        self.date_comboBox.currentTextChanged.connect(self.show_prescription)
        self.pres_textEdit.setReadOnly(True)
        self.doc_lineEdit.setEnabled(False)
        self.new_Button.clicked.connect(self.show_window)

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


class NewWindow(QMainWindow, new):
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
    w = DocPort(("Majid","Samiei","123","09153109973","resume","defaultImage.jpg"))
    w.show()
    sys.exit(app.exec_())
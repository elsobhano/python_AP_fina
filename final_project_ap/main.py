import sys
import os
import sqlite3
from PIL import Image
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsPixmapItem, QWidget, QFileDialog

res = uic.loadUiType(os.path.join(os.getcwd(), "resume.ui"))[0]
new = uic.loadUiType(os.path.join(os.getcwd(), "new.ui"))[0]

conn = sqlite3.connect('resume.db')
c = conn.cursor()


class ResumeWindow(QMainWindow, res):
    def __init__(self):
        super(ResumeWindow, self).__init__()
        self.setupUi(self)

        self.name_lineEdit.textChanged.connect(self.search)
        self.date_comboBox.currentTextChanged.connect(self.show_prescription)
        self.pres_textEdit.setReadOnly(True)
        self.doc_lineEdit.setEnabled(False)
        self.new_Button.clicked.connect(self.show_window)

    def search(self, val):
        c.execute(f'SELECT Date FROM Resume WHERE Name == "{val}";')
        dates = c.fetchall()
        d = []
        for date in dates:
            d.append(date[0])
        self.date_comboBox.clear()
        self.date_comboBox.addItems(d)
    
    def show_prescription(self, val):
        name = self.name_lineEdit.text()
        c.execute(f'SELECT prescription FROM Resume WHERE Name == "{name}" AND Date == "{val}";')
        pres = c.fetchall()
        c.execute(f'SELECT Doc_name FROM Resume WHERE Name == "{name}" AND Date == "{val}";')
        doc_name = c.fetchall()
        c.execute(f'SELECT img FROM Resume WHERE Name == "{name}" AND Date == "{val}";')
        img = c.fetchall()
        self.doc_lineEdit.clear()
        self.pres_textEdit.clear()
        try:
            self.doc_lineEdit.setText(doc_name[0][0])
            self.pres_textEdit.setText(pres[0][0])
            img_path = f'C:/Users/s.ali hahsemi/Desktop/final_project_ap/img/{img[0][0]}.jpg'
            if os.path.isfile(img_path):
                scene = QGraphicsScene(self)
                pixmap = QtGui.QPixmap(img_path)
                item = QGraphicsPixmapItem(pixmap)
                scene.addItem(item)
                self.img_graphicsView.setScene(scene)
        except:
            pass

    def show_window(self):
        self.w = NewWindow()
        self.w.show()
        self.w.n_lineEdit.setText(self.name_lineEdit.text())
        self.w.doctor_lineEdit.setText(self.doc_lineEdit.text())
        self.w.n_lineEdit.setEnabled(False)

class NewWindow(QMainWindow, new):
    def __init__(self):
        super(NewWindow, self).__init__()
        self.setupUi(self)
        self.img_path = ''

        self.load_Button.clicked.connect(self.show_img)
        self.save_Button.clicked.connect(self.save)

    def show_img(self):
        self.img_path, _ = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Image files (*.jpg *.gif)")
        scene = QGraphicsScene(self)
        pixmap = QtGui.QPixmap(self.img_path)
        item = QGraphicsPixmapItem(pixmap)
        scene.addItem(item)
        self.image_View.setScene(scene)
        
    def save(self):
        name = self.n_lineEdit.text()
        doc_name = self.doctor_lineEdit.text()
        date = self.d_lineEdit.text()
        pres = self.p_textEdit.toPlainText()
        d = date.replace('/', '')
        img_str = ''
        if self.img_path != '':
            img_str = name + '_' + d
            img = Image.open(self.img_path)
            img.save('img/' + img_str + '.jpg')
        
        c.execute(f'INSERT INTO resume(Name, Doc_name, Date, Prescription, img) VALUES ("{name}", "{doc_name}", "{date}", "{pres}", "{img_str}")')
        c.fetchall()
        conn.commit()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    w = ResumeWindow()
    w.show()
    sys.exit(app.exec_())
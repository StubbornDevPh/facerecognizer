import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5 import QtWidgets,QtCore, QtGui
from PyQt5 import Qt
import os
import faces
import capture
import train

class App(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.title="GUI KOTO"
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(300,300,500,500)
        self.setWindowIcon(QIcon('pythonicon.ico'))
        self.setFixedSize(self.size())
        self.center()
    
        #button = QPushButton('Click me',self)
        #button.setToolTip('you hovered')
        #button.move(100,200)
        #button.clicked.connect(self.clicked)
        
        # self.labelfortb=QLabel(self)
        # self.labelfortb1=QLabel(self)
        # self.labelfortb.setText("Username:")
        # self.labelfortb.move(20,5)
        # self.textbox = QLineEdit(self)
        # self.textbox.move(20,30)
        # self.textbox.resize(250,30)
        # self.labelfortb1.setText("Password:")
        # self.labelfortb1.move(20,65)
        # self.textbox1 = QLineEdit(self)
        # self.textbox1.setEchoMode(QLineEdit.Password)
        # self.textbox1.move(20,90)
        # self.textbox1.resize(250,30)
        # self.label.setStyleSheet("background-color:red; text-align:center")
        # self.label.move(100,160)
        self.setStyleSheet("background-color: rgb(51, 66, 75);")

        self.font = QtGui.QFont()
        self.label = QLabel(self)
        self.btn_login = QtWidgets.QPushButton("Login",self)
        self.btn_register = QtWidgets.QPushButton("Register", self)
        
        self.font.setFamily("Berlin Sans FB")
        self.font.setPointSize(10)
        self.font.setBold(True)
        self.font.setWeight(75)

        self.background = QtWidgets.QLabel(self)
        self.background.setGeometry(QtCore.QRect(160, 20, 101, 91))
        self.background.setPixmap(QtGui.QPixmap("./pics/unnamed.png"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.background.move(200,10)


        self.btn_login.resize(150,30)
        self.btn_register.resize(150,30)
        self.btn_login.move(175,300)
        self.btn_register.move(175,350)
        self.btn_login.setStyleSheet("background-color: rgb(37, 172, 116); font: 13pt Agency FB;")
        self.btn_register.setStyleSheet("background-color: rgb(37, 172, 116); font: 13pt Agency FB;")

        self.label.setText("Welcome to FaceLogin")
        self.label.move(140,180)
        self.label.setStyleSheet("font: 20pt Agency FB;")
        self.label.resize(self.width(),50)

        self.btn_register.clicked.connect(self.reg_clicked)
        self.btn_login.clicked.connect(self.log_clicked)

        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.show()




    
    def reg_clicked(self):
        self.hide()
        self.jump_reg()

    def log_clicked(self):
        self.hide()
        self.jump_log()

    def jump_log(self):
        self.logcode=logcode()
        self.logcode.show()
    
    def jump_reg(self):
        self.regcode=regcode()
        self.regcode.show()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        
class regcode(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.title="Register"
        self.setWindowTitle(self.title)
        self.setGeometry(400,400,400,400)
        self.setWindowIcon(QIcon('pythonicon.ico'))
        self.regtitlelabel = QLabel(self)
        self.regtitlelabel.setText("Register")
        self.regtitlelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.regtitlelabel.resize(self.width(),60)
        self.regtitlelabel.setStyleSheet("font-size:30px")
        self.labelforusername = QLabel(self)
        self.labelforusername.setText('Username:')
        self.labelforusername.move(10,120)
        self.labelforusername.resize(self.width(),30)
        self.labelforusername.setStyleSheet("font-size:20px")
        self.labelforusername.setAlignment(QtCore.Qt.AlignLeft)
        self.txtboxforusername = QLineEdit(self)
        self.txtboxforusername.resize(self.width()-130,30)
        self.txtboxforusername.move(110,120)
        self.txtboxforusername.setStyleSheet("font-size:20px")
        self.labelforpic = QLabel(self)
        self.labelforpic.setText('Click to capture:')
        self.labelforpic.move(0,210)
        self.labelforpic.resize(self.width(),30)
        self.labelforpic.setStyleSheet("font-size:20px")
        self.labelforpic.setAlignment(QtCore.Qt.AlignCenter)
        self.btn_capture = QtWidgets.QPushButton("Capture", self)
        self.btn_capture.move(0,250)
        self.btn_capture.resize(self.width(),40)
        self.btn_capture.clicked.connect(self.check)

        self.btn_save = QtWidgets.QPushButton("Save", self)
        self.btn_save.move(0,290)
        self.btn_save.resize(self.width(),40)
        self.btn_save.clicked.connect(self.insert)

        if os.path.exists(f'images/{self.txtboxforusername.text()}'):
            self.btn_save.setEnabled(False)
        else:
            self.btn_save.setEnabled(True)

        self.center()


    def insert(self):
        train.train()

    def check(self):
        if os.path.exists(f'images/{self.txtboxforusername.text()}'):
            self.btn_save.setEnabled(False)
            self.hide()
        else:
            self.btn_save.setEnabled(True)
        QMessageBox.warning(self, 'Please wait', "Please wait for the capture to finish", QMessageBox.Ok, QMessageBox.Ok)
        print(self.txtboxforusername.text())
        if self.txtboxforusername.text()=='':
            self.labelforusername.setStyleSheet("font-size:20px;color:red")
        else:
            capture.capture(self.txtboxforusername.text())

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class logcode(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.title="Login"
        self.setWindowTitle(self.title)
        self.setGeometry(100,100,300,80)
        self.setWindowIcon(QIcon('pythonicon.ico'))
        self.center()
        self.login_label = QLabel(self)
        self.login_label.setText("Username:")
        self.login_label.move(10,5)
        self.login_textbox = QLineEdit(self)
        self.login_textbox.move(85,5)
        self.login_textbox.resize(200,30)
        self.loginbtnko = QtWidgets.QPushButton("Login",self)
        self.loginbtnko.move(185,40)
        self.loginbtnko.clicked.connect(self.verify)
        

        
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def verify(self):
        users= subfolders = [ f.name for f in os.scandir("images") if f.is_dir() ]
        if self.login_textbox.text() in users:
            QMessageBox.question(self, 'FaceLogin', "User detected! Please wait for the camera ", QMessageBox.Ok, QMessageBox.Ok)
            self.hide()
            faces.detect(self.login_textbox.text())
        else:
            QMessageBox.critical(self, 'Failed', "User not detected please try again", QMessageBox.Ok, QMessageBox.Ok)



  
if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = App()
    sys.exit(app.exec_())
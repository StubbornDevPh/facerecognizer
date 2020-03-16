
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5 import QtWidgets,QtCore, QtGui
from PyQt5 import Qt
import json
class MainWindow(QMainWindow):
        pass

q_app = QtWidgets.QApplication(sys.argv)
win1 = MainWindow()

def openko():

    with open('logs.json', 'r') as f:
        laman = json.load(f)

    nameko=laman['name']
    print(f'welcome {nameko}')

    def remove_trace(win1):
        print('fired')
        cur_person={'name':'','fresh':'no'}
        with open('logs.json','w') as f:
            json.dump(cur_person,f)

    
    win1.setWindowTitle('Welcome')
    win1.setGeometry(300,300,500,140)
    win1.setWindowIcon(QIcon('pythonicon.ico'))
    win1.setFixedSize(win1.size())
    win1.setStyleSheet("background-color: rgb(51, 66, 75);")
    win1.font = QtGui.QFont()
    win1.label = QLabel(win1)
    win1.label.move(0,50)
    win1.label.setAlignment(QtCore.Qt.AlignCenter)
    #win1.label.setText(f'Welcome {nameko}')#+login.username)
    win1.label.setStyleSheet("font: 20pt Agency FB;text-align:center;")
    win1.label.resize(win1.width(),50)
    win1.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
    q_app.aboutToQuit.connect(remove_trace)
    win1.label.setText(f'Welcome {nameko}')
    win1.show()
    #remove_trace()





    #sys.exit(q_app.exec_())

        # def initUI(self):
        #     self.setWindowTitle(self.title)
        #     self.setGeometry(300,300,500,140)
        #     self.setWindowIcon(QIcon('pythonicon.ico'))
        #     self.setFixedSize(self.size())
        #     self.center()
        #     self.setStyleSheet("background-color: rgb(51, 66, 75);")

        #     self.font = QtGui.QFont()
        #     self.label = QLabel(self)
        #     self.label.move(0,50)
        #     self.label.setAlignment(QtCore.Qt.AlignCenter)
        #     self.label.setText(f'Welcome {nameko}')#+login.username)
        #     self.label.setStyleSheet("font: 20pt Agency FB;text-align:center;")
        #     self.label.resize(self.width(),50)
        #     self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        #     self.show()




        
        # 
            
            
  
# if __name__ == '__main__':
#     main()
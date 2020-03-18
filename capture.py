import numpy as np
import cv2
import os
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5 import QtWidgets,QtCore, QtGui
from PyQt5 import Qt
import main

name=''
def capture(name):
    face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)


    def capko():
        num =0
        while(True):
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

            for (x,y,w,h) in faces:
                #print(x,y,w,h)
                roi_gray = gray[y:y+h, x:x+w]
                #roi_color = frame[y:y+h, x:x+w]
                img_item = (f'.\images\{name}\{num}.png')
                cv2.imwrite(img_item, roi_gray)

                color = (255, 0,0)
                stroke = 2
                end_cord_x = x+w
                end_cord_y = y+h
                cv2.rectangle(frame, (x,y), (end_cord_x, end_cord_y),color,stroke)
                num = num+1
                #print(num)

            cv2.imshow('frame',frame)
            if num==500*.10:
                print('10% training completed!')
            elif num==500*.20:
                print('20% training completed!')
            elif num==500*.30:
                print('30% training completed!')
            elif num==500*.40:
                print('40% training completed!')
            elif num==500*.50:
                print('50% training completed!')
            elif num==500*.60:
                print('60% training completed!')
            elif num==500*.70:
                print('70% training completed!')
            elif num==500*.80:
                print('80% training completed!')
            elif num==500*.90:
                print('90% training completed!')
            elif num==500*.100:
                print('Training completed!')
            if cv2.waitKey(20) & 0xFF == ord('q') or num>=500:
                break

        cap.release()
        cv2.destroyAllWindows()

    if not os.path.exists(f'images/{name}'):
        os.makedirs(f'images/{name}')
        capko()
    elif os.path.exists(f'images/{name}'):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("User exists!")
        msgBox.setWindowTitle("Warning!")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()
        os.system("python main.py")

import numpy as np
import cv2
import pickle
import main as al
import sys
import subprocess
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5 import QtWidgets,QtCore, QtGui
from PyQt5 import Qt
import os
import dashboard
import json

target_name=''
frequency_name=[]

def detect(target_name):
    isAthenticated = 0
    print(f'detecting:{target_name}')
    face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')
    #eye_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_eye.xml')

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("trainer.yml")

    labels = {"person_name": 0}
    with open("labels.pickle", 'rb') as file:
        og_labels = pickle.load(file)
        labels = {v:k for k,v in og_labels.items()}

    cap = cv2.VideoCapture(0)

    while(True):
        
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.4, minNeighbors=5)
        
        for (x,y,w,h) in faces:
            #print(x,y,w,h)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            id_, conf = recognizer.predict(roi_gray)
            print(conf)
            if conf>=80 or conf<=95:# and conf<100:
                print(id_)
                print(labels[id_])
                font = cv2.FONT_HERSHEY_SIMPLEX
                name = labels[id_]
                color = (255 ,255, 255)
                stroke = 2
                frequency_name.append(name)
                cv2.putText(frame, name, (x,y-10), font, 0.7, color, stroke, cv2.LINE_AA)
                if name==target_name:
                    isAthenticated=isAthenticated+1
                else:
                    isAthenticated=isAthenticated-1

                if isAthenticated>=10:
                    print("Verification success!")
            else:
                font = cv2.FONT_HERSHEY_SIMPLEX
                name = "unknown"
                color = (254,39,18)
                stroke = 2
                cv2.putText(frame, name, (x,y-10), font, 0.7, color, stroke, cv2.LINE_AA)
            #img_item = "imageko.png"
            #cv2.imwrite(img_item, roi_gray)
            
            color = (255, 0,0)
            stroke = 2
            end_cord_x = x+w
            end_cord_y = y+h
            cv2.rectangle(frame, (x,y), (end_cord_x, end_cord_y),color,stroke)
            
            #eyes = eye_cascade.detectMultiScale(roi_gray)
            #for (ex,ey,ew,eh) in eyes:
                #cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)        
        cv2.imshow('frame',frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
        	break
        	sys.exit()
        if cv2.waitKey(20) & 0xFF == ord('q') or isAthenticated>=10:
        	break
    

    from collections import Counter
    def MostCommon(lst):
    	data=Counter(lst)
    	return max(lst, key=data.get)

    cur_person={'name':MostCommon(frequency_name),'fresh':'yes'}
    print(cur_person)
    with open('logs.json','w') as f:
    	json.dump(cur_person,f)
    	
    cap.release()
    cv2.destroyAllWindows()
    dashboard.openko()




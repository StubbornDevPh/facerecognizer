import os
import cv2
from PIL import Image
import numpy as np
import pickle
def train():
    print('training...')
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    image_dir = os.path.join(BASE_DIR,"images")

    face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_eye.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    current_id = 0
    label_ids = {}
    y_labels = []
    x_train = []


    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith("png") or file.endswith("jpg"):
                path = os.path.join(root, file)
                label = os.path.basename(os.path.dirname(path)).replace(" ", "-").lower()
                #print(label,path)
                
                if not label in label_ids:
                    label_ids[label] = current_id
                    current_id = current_id+1
                id_ = label_ids[label]
                #print(label_ids)
                
                
                pil_image = Image.open(path).convert("L") #conver to gray
                size = (550,550)
                final_image = pil_image.resize(size, Image.ANTIALIAS)
                image_array = np.array(final_image,"uint8")
                #print(image_array)
                faces = face_cascade.detectMultiScale(image_array, minNeighbors=5)
                
                for (x,y,w,h) in faces:
                    roi = image_array[y:y+h, x:x+w]
                    x_train.append(roi)
                    y_labels.append(id_)
                    
                    
    #print(y_labels)
    #print(x_train)
    with open("labels.pickle", 'wb') as file:
        pickle.dump(label_ids, file)
        
    recognizer.train(x_train, np.array(y_labels))
    recognizer.save("trainer.yml")
    print('trained!')
    print('exiting')
    for i in range (0,1000):
        print(i)
        os.system('cls')
        exit()
import os
import cv2
import numpy as np
import faceRecognition as fr
from mainFunctions import *
import uuid
import threading

def trainFaceDectector():
    #This module captures images via webcam and performs face recognition
    faces,faceID=fr.labels_for_training_data('trainingImages')
    face_recognizer=fr.train_classifier(faces,faceID)
    face_recognizer.write('trainingData.yml')


def face_verify():
    bright_thres = 0.5
    dark_thres = 0.4
    #This module captures images via webcam and performs face recognition
    #faces,faceID=fr.labels_for_training_data('trainingImages')
    #face_recognizer=fr.train_classifier(faces,faceID)
    #face_recognizer.write('trainingData.yml')

    #Uncomment below line for subsequent runs
    face_recognizer=cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.read('trainingData.yml')#use this to load training data for subsequent runs

    name = {0 : "Kartik"}
    path ="E:/AI Creation/AI/trainingImages/0"
    
    
    
    try:
        cap=cv2.VideoCapture("http://192.168.1.2:4747/video")
        #cap=cv2.VideoCapture(0)
    except Exception :
        return False
    
    retryCount=0
    while True:

        ret,test_img=cap.read()# captures frame and returns boolean value and captured image

        if  ret == False  or test_img.all()==None:
            return False

        faces_detected,gray_img=fr.faceDetection(test_img)

        if retryCount>=100:
            dark_part = cv2.inRange(gray_img, 0, 30)
            bright_part = cv2.inRange(gray_img, 220, 255)
            # use histogram
            # dark_pixel = np.sum(hist[:30])
            # bright_pixel = np.sum(hist[220:256])
            total_pixel = np.size(gray_img)
            dark_pixel = np.sum(dark_part > 0)
            bright_pixel = np.sum(bright_part > 0)

            if dark_pixel/total_pixel > bright_thres:
                speak("Face is underexposed!")
                return "error"
            elif bright_pixel/total_pixel > dark_thres:
                speak("Face is overexposed!")
                return "error"
            else:
                cap.release()
                cv2.destroyAllWindows()
                return "unknown"  

        for (x,y,w,h) in faces_detected:
          cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=7)

        resized_img = cv2.resize(test_img, (1000, 700))
        cv2.imshow('face detection',resized_img)
        cv2.waitKey(10)


        for face in faces_detected:
            (x,y,w,h)=face
            roi_gray=gray_img[y:y+w, x:x+h]
            label,confidence=face_recognizer.predict(roi_gray)#predicting the label of given image
            print("confidence:",confidence)
            #print("label:",label)
            fr.draw_rect(test_img,face)
            predicted_name=name[label]
            if confidence < 37:#If confidence less than 37 then don't print predicted face text on screen
                fileName = uuid.uuid4().hex+".jpg"
                cv2.imwrite(os.path.join(path , fileName), test_img)
                fr.put_text(test_img,predicted_name,x,y)
                if predicted_name != None:
                    cap.release()
                    cv2.destroyAllWindows()
                    return predicted_name  

        retryCount+=1
        #resized_img = cv2.resize(test_img, (1000, 700))
        #cv2.imshow('face recognition  ',resized_img)
        if cv2.waitKey(10) == ord('q'):#wait until 'q' key is pressed
            break


    cap.release()
    cv2.destroyAllWindows()


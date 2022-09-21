from time import sleep
import cv2
import numpy as np
import face_recognition
import os
import urllib.request
import numpy as np

from ArduinoCom import SerialCommunication 
from Database import database


# global list for Name of images
className = [] 


url='http://192.168.100.61/640x480.jpg' # esp url

# Get images from Imgs folder
def getImages():
    path = 'imgs'
    images = []
 
    myList = os.listdir(path)

    # get images and add to Images Loop
    for currntImg in myList:
        currImg = cv2.imread(f'{path}/{currntImg}')
        images.append(currImg)
        className.append(os.path.splitext(currntImg)[0])
    return images

# find encoding images
def findEncoding():
    encodeList = []
    for img in getImages():
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList    


def rectangleImages(faceLoc, img, name, r,g,b):
    y1,x2,y2,x1 = faceLoc
    y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
    cv2.rectangle(img,(x1,y1),(x2,y2),(b,g,r),2)
    cv2.putText(img,name,(x1,y2+30),cv2.FONT_HERSHEY_COMPLEX,1,(b,g,r),1)

def main() :
    
    database.createTable()    
    
    print("Wait the images to encode....")
    encodedImages = findEncoding()

    print("Images successful encoded...")
    print("Initializing webCam....")
    cap = cv2.VideoCapture(0)
    print("Done Initializing webCam....") 
    
    while True:
        img_resp=urllib.request.urlopen(url)
        imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
        img=cv2.imdecode(imgnp,-1)
        
        # success, img = cap.read()
        frame = cv2.flip(img, 1) # Flip camera vertically
        imgS = cv2.resize(frame,(0,0),None,0.25,0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
         
        cv2.rectangle(frame, (200, 200), (200, 200), (0,255,0), 1)
        
        # encode the capture image in webcamp
        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
        
        # compare the images
        for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
            matches = face_recognition.compare_faces(encodedImages,encodeFace)
            faceDis = face_recognition.face_distance(encodedImages,encodeFace)
            matchIndex = np.argmin(faceDis)        

            print(matches[matchIndex])
            
            if matches[matchIndex]:
                name = className[matchIndex]
                rectangleImages(faceLoc,frame,name,0,255,0)
                database.addRow(name)
                SerialCommunication.SerialWrite(1)
            else:
                rectangleImages(faceLoc,frame,"No found images",255,0,0)
                SerialCommunication.SerialWrite(0)
            SerialCommunication.SerialWrite(0)

 
        
        cv2.imshow('Attendance check',frame)
        
        k = cv2.waitKey(30) & 0xff
        if k == 27: # press 'ESC' to quit
            break
        cv2.waitKey(1)
        
    cap.release()
    cv2.destroyAllWindows
    
main()
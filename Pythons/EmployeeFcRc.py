import customtkinter
import tkinter 
import urllib.request
from PIL import Image, ImageTk
import cv2
import numpy as np
import face_recognition
import os
import Database.database as DB # database
import ArduinoCom.SerialCommunication as SC # Serial Communication
import threading
from tkinter import messagebox
import time

face_detector=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

url='http://192.168.43.154/640x480.jpg' # url ng hotspot mo rey
 # url='http://192.168.100.61/800x600.jpg' # url ng wifi ko

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

cap = cv2.VideoCapture(0)

class TimeIn(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        
        self.errors = 0
        
        self.title("Employee Face Recognition")
        self.resizable(False, False)
        # =================== Center Form =================== #
        window_height = 600
        window_width = 1050

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # kapag sa screen ko
        # x_cordinate = int((screen_width/2) - (window_width/2))
        # y_cordinate = int((screen_height/3) - (window_height/3))

        # kapag sa screen ni rey
        x_cordinate = int((screen_width/4) - (window_width/4))
        y_cordinate = int((screen_height/8) - (window_height/8))
        
        self.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        
                 
        # =================== Mainframe =================== #
        self.mainFrame = customtkinter.CTkFrame(master=self)
        self.mainFrame.pack(pady=15, padx=15, fill="both", expand=True)

        # =================== set row and column =================== #
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        # =================== Camera Streaming =================== #
        self.cameraFrame = customtkinter.CTkFrame(master=self.mainFrame,height=400 )
        self.cameraFrame.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
     
        # Camera
        self.cameras = customtkinter.CTkLabel(master=self.cameraFrame,corner_radius=20,text="Loading...")
        self.cameras.grid(row=0, column=0)

        self.cameras.place(relx=.5,rely=.5,anchor='center')
        
        # =================== click Button Field =================== #
        self.captureButton = customtkinter.CTkFrame(master=self.mainFrame, width=1000,height=130 )
        self.captureButton.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
        
        # Label
        self.label = customtkinter.CTkLabel(master=self.captureButton,
                                 text="Please click the button to capture")
        self.label.pack(pady=10, padx=10)
        self.label.place(relx=.5,rely=.5,anchor='s')
        
        # capture camera
        self.selfie = customtkinter.CTkButton(master=self.captureButton, 
                                   text="Capture camera",
                                   command=self.captureCam)
        self.selfie.pack(pady=10, padx=10)
        self.selfie.place(relx=.5,rely=.6,anchor='center')
        
        
    def asd(self):
        self.root.destroy()
    # ========================== code for video streaming
    def camera(self):
        
        # create database for today
        DB.createTable()
        
        img_resp=urllib.request.urlopen(url)
        imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
        img=cv2.imdecode(imgnp,-1)
        
        cv2image= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        frame = cv2.flip(cv2image, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Draw a rectangle around the faces
        faces = face_detector.detectMultiScale(gray, 
                                               scaleFactor=1.15,
                                               minNeighbors=5,
                                               minSize=(34, 35), 
                                               flags=cv2.CASCADE_SCALE_IMAGE)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
        img = Image.fromarray(frame)
        
        ImgTks = ImageTk.PhotoImage(image=img)
        
        self.cameras.configure(image = ImgTks)
        self.cameras.image = ImgTks
       
        self.cameras.after(5, self.camera)
    
    # ==========================  code for capture camera
    def captureCam(self):
         
        img_resp=urllib.request.urlopen(url)
        imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
        img=cv2.imdecode(imgnp,-1)
        
        frame = cv2.flip(img, 1)
        
        img_name = "TimeInOut/TimeInOut.png"
        cv2.imwrite(img_name, frame)
        
        # face recognition ===========
        
        # known faces
        encodedImages = self.findEncoding()
        
        # unknown to be known
        facesCurFrame = face_recognition.face_locations(self.getCapture())
        encodesCurFrame = face_recognition.face_encodings(self.getCapture(),facesCurFrame)        
        
        
        if not facesCurFrame:
            SC.SerialWrite(0)
            self.errors +=1
            messagebox.showerror('error', "I can't recognize you, may you please position your face properly on the camera")
            
        # compare images
        for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
            matches = face_recognition.compare_faces(encodedImages,encodeFace)
            faceDis = face_recognition.face_distance(encodedImages,encodeFace)
            matchIndex = np.argmin(faceDis) 
            
            
            if matches[matchIndex]:
                
                # get the name
                name = self.className[matchIndex]

                # Serial write to true
                SC.SerialWrite(1)
                
                # set Text
                # messagebox.showinfo('information', "Hello have a great day! " + name + " :)")
                
                # add to database
                DB.addRow(name) 
                break
            else:
                # Serial write to true
                SC.SerialWrite(0)
                self.errors +=1
                messagebox.showerror('error', "Im sorry but i dont recognize you")
                break


    # ==========================  find encoding images
    
    # global list for Name of images
    className = [] 
    
    def getImages(self):
        
        path = 'imgs'
        images = []
        myList = os.listdir(path)

        #  get images and add to Images Loop
        for currntImg in myList:
            currImg = cv2.imread(f'{path}/{currntImg}')
            images.append(currImg)
            self.className.append(os.path.splitext(currntImg)[0])
        return images 
    
    def findEncoding(self): 
        encodeList = []
        for img in self.getImages():
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList 
    
    # ==========================  get capture images
    def getCapture(self):
        capture = cv2.imread('TimeInOut/TimeInOut.png') # get capture images
        return capture
    
    # ==========================  serial coms
    def serialRead(self):
        a = SC.SerialRead()
        # print(a)
        if a:
            # print(a)
            b = DB.selectTable(a)
            SC.SerialWrite(b)
            print(b)
            messagebox.showinfo('information', 'Please come back asap takecare!') if b == 1 else messagebox.showerror('error', 'please do register!')
        return self.serialRead()
    
    # ========================== errors
    def errorstO(self):
        print(str(self.errors))
        if self.errors == 3:
            messagebox.showwarning('warning', 'Please try again after 10 sec')
            self.label.configure(text="Unable to capture camera please wait 10 seconds")
            self.selfie.configure(state="disabled")
            time.sleep(10)
            self.label.configure(text="Please click the button to Time In")
            self.selfie.configure(state="enable")
            self.errors = 0
        else:
            self.label.configure(text="Please click the button to Time In")
            self.selfie.configure(state="enable")
            
        return self.errorstO()   

if __name__ == "__main__":
    app = TimeIn()
    
    threading.Thread(target=app.serialRead, args=()).start()
    threading.Thread(target=app.camera, args=()).start()
    threading.Thread(target=app.errorstO, args=()).start()
    app.mainloop()

    



import customtkinter
import tkinter 
from PIL import Image, ImageTk
import cv2
import numpy as np
import face_recognition
import os
import Database.database as DB # database
import ArduinoCom.SerialCommunication as SC # Serial Communication


face_detector=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

cap = cv2.VideoCapture(0)

class TimeIn(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        
        self.title("Time In")
        self.resizable(False, False)
        # =================== Center Form =================== #
        window_height = 750
        window_width = 1050

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/3) - (window_height/3))
        
        self.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        
         
        
        # =================== Mainframe =================== #
        self.mainFrame = customtkinter.CTkFrame(master=self)
        self.mainFrame.pack(pady=15, padx=15, fill="both", expand=True)

        
        # =================== set row and column =================== #
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        # =================== Camera Streaming =================== #
        self.cameraFrame = customtkinter.CTkFrame(master=self.mainFrame,height=500 )
        self.cameraFrame.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
     
        # Camera
        self.cameras = customtkinter.CTkLabel(master=self.cameraFrame,corner_radius=20)
        self.cameras.grid(row=0, column=0)

        self.cameras.place(relx=.5,rely=.5,anchor='center')
        
        # =================== click Button Field =================== #
        self.captureButton = customtkinter.CTkFrame(master=self.mainFrame, width=1000,height=180 )
        self.captureButton.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
        
        # Label
        self.label = customtkinter.CTkLabel(master=self.captureButton,
                                 text="Please click the button to Time In")
        self.label.pack(pady=10, padx=10)
        self.label.place(relx=.5,rely=.5,anchor='s')
        
        # capture camera
        self.selfie = customtkinter.CTkButton(master=self.captureButton, 
                                   text="Capture camera",
                                   command=self.captureCam)
        self.selfie.pack(pady=10, padx=10)
        self.selfie.place(relx=.5,rely=.6,anchor='center')
        
                # capture camera
        self.goback  = customtkinter.CTkButton(master=self.captureButton, 
                                   text="back to mainmenu",
                                   command=self.quit)
        self.goback.pack(pady=10, padx=10)
        self.goback.place(relx=.5,rely=.8,anchor='center')

        # self.camera.configure(image=)
    def asd(self):
        self.root.destroy()
    # ========================== code for video streaming
    def camera(self):
        
        # create database for today
        DB.createTable()
        
        ret, img = cap.read()
        cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
        
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
         
        ret, img = cap.read()
        frame = cv2.flip(img, 1)
        
        img_name = "TimeInOut/TimeIn.png"
        cv2.imwrite(img_name, frame)
        
        # face recognition ===========
        
        # known faces
        encodedImages = self.findEncoding()
        
        # unknown to be known
        facesCurFrame = face_recognition.face_locations(self.getCapture())
        encodesCurFrame = face_recognition.face_encodings(self.getCapture(),facesCurFrame)        
        
        
        if not facesCurFrame:
            self.label.configure(text="I can't recognize yoy, may you please position ypur face properly on the camera")
            print(facesCurFrame)
            SC.SerialWrite(0)
        # compare images
        for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
            matches = face_recognition.compare_faces(encodedImages,encodeFace)
            faceDis = face_recognition.face_distance(encodedImages,encodeFace)
            matchIndex = np.argmin(faceDis) 
            
            
            
            if matches[matchIndex]:
                
                # get the name
                name = self.className[matchIndex]
                
                # set Text
                self.label.configure(text="Hello have a great day! " + name + " :)")
                
                # Serial write to true
                SC.SerialWrite(1)
                
                # add to database
                DB.addRow(name) 
                
                
                print()
                break
            else:
                self.label.configure(text="Im sorry but i dont recognize you")
                
                # Serial write to true
                SC.SerialWrite(0)
                
                break
 
        # cv2.waitKey()
        # cv2.destroyAllWindows()

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
        capture = cv2.imread('TimeInOut/TimeIn.png') # get capture images
        return capture
    

if __name__ == "__main__":
    app = TimeIn()
    app.camera()
    app.mainloop()

# TimeIn().camera()
    



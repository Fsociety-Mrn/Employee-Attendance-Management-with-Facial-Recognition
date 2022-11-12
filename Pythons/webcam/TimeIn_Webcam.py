import customtkinter
import tkinter 
from PIL import Image, ImageTk
import cv2
import sys



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
        window_height = 700
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
        self.captureButton = customtkinter.CTkFrame(master=self.mainFrame, width=1000,height=130 )
        self.captureButton.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
        
        # Label
        self.label = customtkinter.CTkLabel(master=self.captureButton,
                                 text="Attendance Face Recognition")
        self.label.pack(pady=10, padx=10)
        self.label.place(relx=.5,rely=.5,anchor='s')
        
        # capture camera
        self.selfie = customtkinter.CTkButton(master=self.captureButton, 
                                   text="Capture camera",
                                   command=self.captureCam)
        self.selfie.pack(pady=10, padx=10)
        self.selfie.place(relx=.5,rely=.6,anchor='center')

        # self.camera.configure(image=)
    
    # code for video streaming
    def camera(self):
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
        
    def captureCam(self):
        
        ret, img = cap.read()
        
        frame = cv2.flip(img, 1)
        
        # SPACE pressed
        img_name = "imgs/TimeIn.png"
        cv2.imwrite(img_name, frame)
        
        print("{} written!".format(img_name))
        cv2.waitKey()
        cv2.destroyAllWindows()

        
    
if __name__ == "__main__":
    app = TimeIn()
    app.camera()
    app.mainloop()
    



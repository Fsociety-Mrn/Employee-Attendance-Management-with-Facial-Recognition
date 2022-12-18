import tkinter 
import customtkinter

from PIL import Image, ImageTk
import cv2

from tkinter import messagebox
from ArduinoCom import SerialCommunication 
from Database import database

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


cap = cv2.VideoCapture(0)
face_detector=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


app = customtkinter.CTk()


app.resizable(False, False)
        # =================== Center Form =================== #
window_height = 580
window_width = 400

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

        # kapag sa screen ko
# x_cordinate = int((screen_width/2) - (window_width/2))
# y_cordinate = int((screen_height/2) - (window_height/2))

        # kapag sa screen ni rey
x_cordinate = int((screen_width/3) - (window_width/3))
y_cordinate = int((screen_height/8) - (window_height/8))
        
app.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        

# app.geometry("400x580")
app.title("Attendance registration")


# def on_closing(self, event=0):
#     self.destroy()
#     import Mainmenu

def check():
    if not LastName.get() == "" and not firstName.get() == "" and not middleInitial.get() == "":
        return True
    else:
        return False
    

        
def openWebCam():
    if check():
        

        
        
        photo = customtkinter.CTkToplevel()
        photo.title("Capture Camera")

        def capture():
            ret, img = cap.read()
            frame = cv2.flip(img, 1)
            name = str(LastName.get()) + "," + str(firstName.get()) + " " + str(middleInitial.get())
            img_name = "imgs/" + name + ".png"
            cv2.imwrite(img_name, frame)
            photo.destroy()
            messagebox.showinfo('information', 'capture complete')
            
      
    
    #     window_height = 600
    #     window_width = 700

    #     screen_width = app.winfo_screenwidth()
    #     screen_height = app.winfo_screenheight()

    # # kapag sa screen ko
    #     x_cordinate = int((screen_width/2) - (window_width/2))
    #     y_cordinate = int((screen_height/3) - (window_height/3))

    # kapag sa screen ni rey
    # x_cordinate = int((screen_width/4) - (window_width/4))
    # y_cordinate = int((screen_height/8) - (window_height/8))
        
        photo.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        photo.geometry("700x600")
       
 
        label = customtkinter.CTkLabel(photo, text="Loading....")
        label.pack(side="top", fill="both", expand=True, padx=10, pady=10)
    
        button = customtkinter.CTkButton(master=photo, text="Capture", command=capture )
        button.pack(side="top", padx=30, pady=30)
    
    
        def camera():
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
        
            label.configure(image = ImgTks)
            label.image = ImgTks
       
            label.after(5, camera)
        
        camera()
    
    
        # name = str(LastName.get()) + "," + str(firstName.get()) + " " + str(middleInitial.get())
        # captureWebCam.cam(name.upper())
    else:
        messagebox.showerror("Attendance Face Recognition","Please input the empty field")


def backToMainMene():  
    RDI_text = ""
    while not RDI_text:
        RDI_text = SerialCommunication.SerialRead()
        print(RDI_text)
        
    RFIDLABEL.config(text=RDI_text)
    
def registerNow():
    
    if check() and RFIDLABEL.text != "Click the button to scan your RFID":
        name = str(LastName.get()) + "," + str(firstName.get()) + " " + str(middleInitial.get())
        database.insert(RFIDLABEL.text,name)
        print("goods") 
    



frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=20, fill="both", expand=True)

# Capture camera
# goback = customtkinter.CTkButton(master=frame_1, 
#                                    text="go to mainmenu",
#                                    command=backToMainMene
#                                    )
# goback.pack(pady=12, padx=10)

title = customtkinter.CTkLabel(master=frame_1,
                                 text="Please enter all necessary information.", 
                                 justify=tkinter.LEFT)
title.pack(pady=12, padx=10)


# fillUp information
LastName = customtkinter.CTkEntry(master=frame_1,
                                  width=500, 
                                  height=50,
                                  placeholder_text="Last Name",
                                  )
LastName.pack(pady=20, padx=20)


firstName = customtkinter.CTkEntry(master=frame_1,
                                  width=500, 
                                  height=50,
                                  placeholder_text="First Name",
                                  )
firstName.pack(pady=20, padx=20)

middleInitial = customtkinter.CTkEntry(master=frame_1,
                                  width=500, 
                                  height=50,
                                  placeholder_text="Middle Name",
                                  )
middleInitial.pack(pady=20, padx=20)

# Capture camera
captureCamera = customtkinter.CTkButton(master=frame_1, 
                                   text="Take a Photo",
                                   command=openWebCam
                                   )
captureCamera.pack(pady=12, padx=10)


RFIDLABEL = customtkinter.CTkLabel(master=frame_1,
                                 text="Click the button to scan your RFID", 
                                 justify=tkinter.LEFT)
RFIDLABEL.pack(pady=12, padx=10)



    
buts = customtkinter.CTkButton(master=frame_1, 
                                   text="scan",
                                   command=backToMainMene
                                   )
buts.pack(pady=12, padx=10)

RegisterButton = customtkinter.CTkButton(master=frame_1, 
                                   text="Register",
                                   command=registerNow
                                   ).pack(pady=12, padx=10)


app.mainloop()
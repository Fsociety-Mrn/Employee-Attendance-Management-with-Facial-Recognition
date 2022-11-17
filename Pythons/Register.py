import tkinter 
import customtkinter
import captureEspCam
import captureWebCam


from tkinter import messagebox
from ArduinoCom import SerialCommunication 
from Database import database

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"




app = customtkinter.CTk()
app.geometry("400x580")
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
        name = str(LastName.get()) + "," + str(firstName.get()) + " " + str(middleInitial.get())
        captureWebCam.cam(name.upper())
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
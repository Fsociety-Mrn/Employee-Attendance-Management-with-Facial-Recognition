import tkinter
import customtkinter
from tkinter import messagebox
from Database import database

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x250")
app.title("")


def button_callback():

    print("Button click", database.login(username.get(),password.get()))
    
    if database.login(username.get(),password.get()):
        messagebox.showinfo("Attendance Face Recognition","login was successful")
        app.destroy()
        import Mainmenu
    else:
        messagebox.showerror("Attendance Face Recognition","We apologize for the inconvenience; please enter the correct username and password.")


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=20, fill="both", expand=True)

title = customtkinter.CTkLabel(master=frame_1,
                                 text="Attendance Face Recognition", 
                                 justify=tkinter.CENTER)
title.pack(pady=12, padx=10)


username = customtkinter.CTkEntry(master=frame_1,
                                  width=500, 
                                  height=40,
                                  placeholder_text="Input your username",
                                  )
username.pack(pady=5, padx=10)

password = customtkinter.CTkEntry(master=frame_1,
                                  width=500, 
                                  height=40,
                                  placeholder_text="Input your password",
                                  show="*"
                                  )
password.pack(pady=5, padx=10)


button_1 = customtkinter.CTkButton(master=frame_1, 
                                   text="Login",
                                   command=button_callback)
button_1.pack(pady=12, padx=10)




app.mainloop()

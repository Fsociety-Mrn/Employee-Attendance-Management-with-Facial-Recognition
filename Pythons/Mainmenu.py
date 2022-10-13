import tkinter
import customtkinter
import espCam


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x250")
app.title("Attendance Face Recognition")

def openCamera():
    app.destroy()
    espCam.main()
    
def register():
    app.destroy()
    import Register

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=15, padx=15, fill="both", expand=True)

title = customtkinter.CTkLabel(master=frame_1,
                                 text="Please select the following from the main menu", 
                                 justify=tkinter.CENTER)
title.pack(pady=12, padx=0)

checkAttendance = customtkinter.CTkButton(master=frame_1, 
                                   text="Check Attendance",
                                   width=5000,
                                   height=50,
                                   command=openCamera
                                    )
checkAttendance.pack(pady=12, padx=10)


register = customtkinter.CTkButton(master=frame_1, 
                                   text="Register",
                                   width=5000,
                                    height=50,
                                    command=register
                                    )
register.pack(pady=12, padx=10)



app.mainloop()
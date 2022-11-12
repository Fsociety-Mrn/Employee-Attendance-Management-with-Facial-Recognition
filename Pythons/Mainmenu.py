import tkinter
import customtkinter
import Test
# import espCam


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class asd(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("400x250")
        self.title("Attendance Face Recognition")

        self.frame_1 = customtkinter.CTkFrame(master=self)
        self.frame_1.pack(pady=15, padx=15, fill="both", expand=True)

        self.title = customtkinter.CTkLabel(master=self.frame_1,
                                 text="Please select the following from the main menu", 
                                 justify=tkinter.CENTER)
        self.title.pack(pady=12, padx=0)

        self.checkAttendance = customtkinter.CTkButton(master=self.frame_1, 
                                   text="Check Attendance",
                                   width=5000,
                                   height=50,
                                   command=self.openCamera
                                    )
        self.checkAttendance.pack(pady=12, padx=10)


        self.register = customtkinter.CTkButton(master=self.frame_1, 
                                   text="Register",
                                   width=5000,
                                    height=50,
                                    command=self.register
                                    )
        self.register.pack(pady=12, padx=10)



    def openCamera(self):
        self.destroy()
        # import App
        # espCam.main()
    
    def register(self):
        self.destroy()
        # import Register








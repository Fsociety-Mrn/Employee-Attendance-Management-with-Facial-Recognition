import tkinter
import customtkinter
import Database.database as DB # Database
import ArduinoCom.SerialCommunication as SC # Serial Communication
# import espCam


customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class asd(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # =================== Center Form =================== #
        window_height = 400
        window_width = 400

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/3) - (window_height/3))
        
        self.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        
        self.title("Attendance Face Recognition")

        self.frame_1 = customtkinter.CTkFrame(master=self)
        self.frame_1.pack(pady=15, padx=15, fill="both", expand=True)

        self.title = customtkinter.CTkLabel(master=self.frame_1,
                                 text="Please tap the card to exit.", 
                                 justify=tkinter.CENTER)
        self.title.pack(pady=12, padx=0)
        

        self.TimeIn = customtkinter.CTkButton(master=self.frame_1, 
                                   text="Time In",
                                   width=5000,
                                   height=50,
                                   command=self.openCamera
                                    )
        self.TimeIn.pack(pady=12, padx=10)


        self.TimeOut = customtkinter.CTkButton(master=self.frame_1, 
                                   text="Time Out",
                                   width=5000,
                                    height=50,
                                    command=self.openCamera
                                    )
        self.TimeOut.pack(pady=12, padx=10)
        
        self.reguster = customtkinter.CTkButton(master=self.frame_1, 
                                   text="Register",
                                   width=5000,
                                    height=50,
                                    command=self.openCamera
                                    )
        self.reguster.pack(pady=12, padx=10)
        
        


    def openCamera(self):
        self.quit()
        # espCam.main()
    
    def register(self):
        self.quit()
        # import Register
        
    def serialRead(self):
        a = SC.SerialRead()
        if a:
            print(SC.SerialWrite(DB.selectTable(a)))
            
            
        self.title.configure(text="Please tap the card to exit.")
        self.title.after(1000, self.serialRead)

if __name__ == "__main__":
    app = asd()
    app.serialRead()
    app.mainloop()
    







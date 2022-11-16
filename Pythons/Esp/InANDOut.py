import tkinter
import customtkinter
import Database.database as DB # Database
import ArduinoCom.SerialCommunication as SC # Serial Communication
from tkinter import messagebox


customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class asd(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # =================== Center Form =================== #
        window_height = 200
        window_width = 400

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        
        self.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        
        self.title("Attendance Face Recognition")

        self.frame_1 = customtkinter.CTkFrame(master=self)
        self.frame_1.pack(pady=15, padx=15, fill="both", expand=True)

        self.title = customtkinter.CTkLabel(master=self.frame_1,
                                 text="Hi, Please tap the card to exit. :)", 
                                 justify=tkinter.CENTER)
        self.title.pack(pady=12, padx=0)
        self.title.place(in_=self.frame_1, anchor="c", relx=.5, rely=.5)

       
        

        
        # ================== serial communication for exit ================== #
        self.serialRead()

    def timeIn(self):
        window = customtkinter.CTkToplevel(self)
        window.geometry("400x200")

        # create label on CTkToplevel window
        label = customtkinter.CTkLabel(window, text="CTkToplevel window")
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)
        
    def register(self):
        self.quit()
        # import Register
        
    def serialRead(self):
        a = SC.SerialRead()
        if a:
            b = DB.selectTable(a)
            SC.SerialWrite(b)
            print(DB.selectTable(a))
            messagebox.showinfo('information', 'Please come back asap takecare!') if b == 1 else messagebox.showerror('error', 'please do register!')
            
        # self.title.configure(text="Please tap the card to exit.")
        self.title.after(1000, self.serialRead)



app = asd()
app.mainloop()







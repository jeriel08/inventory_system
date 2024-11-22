from customtkinter import *
from tkcalendar import Calendar

import config

class SignUpPage(CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("SmartStock Tracker - Sign-up Page")
        self.resizable(False, False)

        # Birthday
        birthday_label = CTkLabel(master=self,
                                  height=16,
                                  width=52,
                                  text="Birthday",
                                  font=("Roboto", 14))
        birthday_label.place(x=130, y=394)

        choose_date = CTkButton(master=self,
                                height=14,
                                width=69,
                                hover_color=config.background,
                                fg_color="transparent",
                                text_color=config.text,
                                text="Choose Date",
                                font=("Roboto", 12))
        choose_date.place(x=276, y=394)

        self.birthday = CTkEntry(master=self,
                                 height=50,
                                 width=270,
                                 corner_radius=35,
                                 border_color=config.secondary,
                                 placeholder_text_color=config.text,
                                 placeholder_text="mm/dd/yy",
                                 font=("Roboto", 18))
        self.birthday.place(x=118, y=416)
        self.birthday.bind("<1>", self.choose_date)

    def choose_date(self):
        global cal, date_window
        date_window = CTkToplevel()
        date_window.grab_set()
        date_window.title("Choose Date of Birth")

        # Center the window on the screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        position_x = (screen_width // 2) - (250 // 2)
        position_y = (screen_height // 2) - (220 // 2)
        date_window.geometry(f"250x220+{position_x}+{position_y}")

        cal = Calendar(master=date_window,
                       selectmode="Day",
                       date_pattern="mm/dd/yy")
        cal.place(x=0, y=0)

        submit = CTkButton(master=date_window,
                           text="Submit",
                           height=14,
                           width=40,
                           hover_color=config.background,
                           fg_color="transparent",
                           text_color=config.text,
                           font=("Roboto", 12),
                           command=self.grab_date)
        submit.place(x=80, y=190)

    def grab_date(self):
        self.birthday.delete(0, END)
        self.birthday.insert(0, cal.get_date())
        date_window.destroy()


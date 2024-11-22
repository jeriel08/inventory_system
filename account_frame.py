from customtkinter import *
import config
from tkcalendar import Calendar

class Account(CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, width=963, height=480, bg_color="transparent")

        # Username Settings
        self.date_window = None
        self.cal = None
        username_label = CTkLabel(master=self,
                                  height=16,
                                  width=64,
                                  text="Username",
                                  font=("Roboto", 14))
        username_label.place(x=219, y=39)

        self.username = CTkEntry(master=self,
                                 height=55,
                                 width=275,
                                 corner_radius=35,
                                 border_color=config.secondary,
                                 placeholder_text_color=config.text,
                                 font=("Roboto", 18))
        self.username.place(x=198, y=64)

        # Password Settings
        password_label = CTkLabel(master=self,
                                  height=17,
                                  width=69,
                                  text="Password",
                                  font=("Roboto", 14))
        password_label.place(x=516, y=39)

        self.password = CTkEntry(master=self,
                                 height=55,
                                 width=275,
                                 corner_radius=35,
                                 border_color=config.secondary,
                                 placeholder_text_color=config.text,
                                 show="*",
                                 font=("Roboto", 18))
        self.password.place(x=492, y=63)

        self.show_password_status = BooleanVar(value=False)

        self.show_password = CTkCheckBox(master=self,
                                         text="Show Password",
                                         width=86,
                                         height=14,
                                         checkbox_width=14,
                                         checkbox_height=14,
                                         corner_radius=5,
                                         border_width=2,
                                         border_color=config.secondary,
                                         hover_color=config.clicked_secondary,
                                         offvalue=False,
                                         onvalue=True,
                                         variable=self.show_password_status,
                                         command=self.show_password)
        self.show_password.place(x=528, y=125)

        # Contact Number
        contact_number_label = CTkLabel(master=self,
                                        height=17,
                                        width=114,
                                        text="Contact Number",
                                        font=("Roboto", 14))
        contact_number_label.place(x=219, y=154)

        self.contact_number = CTkEntry(master=self,
                                       height=55,
                                       width=275,
                                       corner_radius=35,
                                       border_color=config.secondary,
                                       placeholder_text_color=config.text,
                                       font=("Roboto", 18))
        self.contact_number.place(x=198, y=179)

        # Email Address
        email_address_label = CTkLabel(master=self,
                                       height=17,
                                       width=99,
                                       text="Email Address",
                                       font=("Roboto", 14))
        email_address_label.place(x=516, y=154)

        self.email_address = CTkEntry(master=self,
                                      height=55,
                                      width=275,
                                      corner_radius=35,
                                      border_color=config.secondary,
                                      placeholder_text_color=config.text,
                                      font=("Roboto", 18))
        self.email_address.place(x=492, y=179)

        # Birthday
        birthday_label = CTkLabel(master=self,
                                  height=16,
                                  width=52,
                                  text="Birthday",
                                  font=("Roboto", 14))
        birthday_label.place(x=219, y=271)

        choose_date = CTkButton(master=self,
                                height=14,
                                width=69,
                                hover_color=config.background,
                                fg_color="transparent",
                                text_color=config.text,
                                text="Choose Date",
                                font=("Roboto", 14),
                                command=self.choose_date)
        choose_date.place(x=368, y=269)

        self.birthday = CTkEntry(master=self,
                                 height=55,
                                 width=275,
                                 corner_radius=35,
                                 border_color=config.secondary,
                                 placeholder_text_color=config.text,
                                 placeholder_text="mm/dd/yy",
                                 font=("Roboto", 18))
        self.birthday.place(x=198, y=296)

        # Gender
        gender_label = CTkLabel(master=self,
                                height=17,
                                width=50,
                                text="Gender",
                                font=("Roboto", 14))
        gender_label.place(x=516, y=271)

        self.gender = CTkComboBox(master=self,
                                  height=55,
                                  width=275,
                                  corner_radius=35,
                                  border_color=config.secondary,
                                  button_color=config.secondary,
                                  button_hover_color=config.secondary,
                                  font=("Roboto", 18),
                                  values=["Male", "Female", "Others"])
        self.gender.place(x=492, y=296)

        # Save Button
        self.save_button = CTkButton(master=self,
                                        width=178,
                                        height=51,
                                        text="SAVE",
                                        corner_radius=35,
                                        border_color=config.accent,
                                        fg_color=config.secondary,
                                        hover_color=config.clicked_secondary,
                                        font=("Roboto", 18),
                                        command=self.save_func)
        self.save_button.place(x=394, y=390)

    def show_password(self):
        if self.show_password_status.get():
            self.password.configure(show="")
        else:
            self.password.configure(show="*")

    def choose_date(self):
        self.date_window = CTkToplevel()
        self.date_window.grab_set()
        self.date_window.resizable(False, False)
        self.date_window.title("Choose Date of Birth")

        config.window_size(master=self.date_window, window_width=400, window_height=400)

        # Calendar Widget
        self.cal = Calendar(master=self.date_window,
                            selectmode="day",
                            date_pattern="mm/dd/yy",
                            font=("Roboto", 14))
        self.cal.place(x=73, y=63)

        # Submit Button
        submit = CTkButton(master=self.date_window,
                           height=51,
                           width=109,
                           corner_radius=35,
                           border_color=config.secondary,
                           hover_color=config.clicked_secondary,
                           fg_color=config.secondary,
                           text="Submit",
                           font=("Roboto", 18),
                           command=self.grab_date)
        submit.place(x=152, y=288)

    def grab_date(self):
        # Get the selected date and update the birthday entry
        selected_date = self.cal.get_date()
        self.birthday.delete(0, END)
        self.birthday.insert(0, selected_date)

        # Close the calendar window
        self.date_window.destroy()

    def save_func(self):
        self.username.delete(0, END)
        self.password.delete(0, END)
        self.contact_number.delete(0, END)
        self.email_address.delete(0, END)
        self.birthday.delete(0, END)
        self.gender.set("Male")
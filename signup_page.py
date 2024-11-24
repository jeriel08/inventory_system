from customtkinter import *
import customtkinter
from tkcalendar import Calendar
import config
from database import insert_user, check_user
from tkinter import messagebox

customtkinter.set_appearance_mode("light")

class SignUpPage(CTkToplevel):
    def __init__(self, controller):
        super().__init__()
        self.date_window = None
        self.cal = None
        self.controller = controller
        self.title("SmartStock Tracker - Sign-up Page")
        self.configure(bg=config.background)
        self.protocol("WM_DELETE_WINDOW", self.controller.show_login_page)
        self.resizable(False, False)

        config.window_size(master=self, window_width=config.width, window_height=config.height)

        # Posting Logo
        ctk_logo = CTkImage(light_image=config.app_logo, dark_image=config.app_logo, size=(271, 136))
        label = CTkLabel(master=self, image=ctk_logo, text="")
        label.place(x=118, y=27)

        # Sign-up Page Title
        sign_up = CTkLabel(master=self,
                           text="SIGN-UP PAGE",
                           font=("Roboto", 40, "bold"),
                           height=47,
                           width=272)
        sign_up.place(x=410, y=70)

        # Username Settings
        self.username = CTkEntry(master=self,
                            height=50,
                            width=270,
                            corner_radius=35,
                            border_color=config.secondary,
                            placeholder_text_color=config.text,
                            font=("Roboto", 18))
        self.username.place(x=118, y=200)

        username_label = CTkLabel(master=self,
                                  height=16,
                                  width=64,
                                  text="Username",
                                  font=("Roboto", 14))
        username_label.place(x=137, y=178)

        # Password Settings
        self.password = CTkEntry(master=self,
                            height=50,
                            width=270,
                            corner_radius=35,
                            border_color=config.secondary,
                            placeholder_text_color=config.text,
                            show="*",
                            font=("Roboto", 18))
        self.password.place(x=410, y=200)

        password_label = CTkLabel(master=self,
                                  height=16,
                                  width=64,
                                  text="Password",
                                  font=("Roboto", 14))
        password_label.place(x=434, y=180)

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
        self.show_password.place(x=434, y=260)

        # Contact Number
        contact_number_label = CTkLabel(master=self,
                                        height=16,
                                        width=103,
                                        text="Contact Number",
                                        font=("Roboto", 14))
        contact_number_label.place(x=133, y=287)

        self.contact_number = CTkEntry(master=self,
                                       height=50,
                                       width=270,
                                       corner_radius=35,
                                       border_color=config.secondary,
                                       placeholder_text_color=config.text,
                                       font=("Roboto", 18))
        self.contact_number.place(x=118, y=310)

        # Email Address
        email_address_label = CTkLabel(master=self,
                                        height=16,
                                        width=103,
                                        text="Email Address",
                                        font=("Roboto", 14))
        email_address_label.place(x=428, y=287)

        self.email_address = CTkEntry(master=self,
                                       height=50,
                                       width=270,
                                       corner_radius=35,
                                       border_color=config.secondary,
                                       placeholder_text_color=config.text,
                                       font=("Roboto", 18))
        self.email_address.place(x=410, y=310)

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
                                font=("Roboto", 12),
                                command=self.choose_date)
        choose_date.place(x=276, y=392)

        self.birthday = CTkEntry(master=self,
                                       height=50,
                                       width=270,
                                       corner_radius=35,
                                       border_color=config.secondary,
                                       placeholder_text_color=config.text,
                                       placeholder_text="mm/dd/yy",
                                       font=("Roboto", 18))
        self.birthday.place(x=118, y=416)

        # Gender
        gender_label = CTkLabel(master=self,
                                       height=16,
                                       width=45,
                                       text="Gender",
                                       font=("Roboto", 14))
        gender_label.place(x=428, y=394)

        self.gender = CTkComboBox(master=self,
                                    height=50,
                                    width=270,
                                    corner_radius=35,
                                    border_color=config.secondary,
                                    button_color=config.secondary,
                                    button_hover_color=config.secondary,
                                    font=("Roboto", 18),
                                    values=["Male", "Female", "Others"])
        self.gender.place(x=410, y=416)

        # Sign-up Button
        self.sign_up_button = CTkButton(master=self,
                                   width=109,
                                   height=51,
                                   text="Sign-up",
                                   corner_radius=35,
                                   border_color=config.accent,
                                   fg_color=config.secondary,
                                   hover_color=config.clicked_secondary,
                                   font=("Roboto", 18),
                                    command=self.signup_func)
        self.sign_up_button.place(x=346, y=500)


        # Go Back Button
        go_back = CTkButton(master=self,
                            height=14,
                            width=51,
                            hover_color=config.background,
                            fg_color="transparent",
                            text_color=config.text,
                            text="Go Back",
                            font=("Roboto", 12),
                            command=self.go_to_login)
        go_back.place(x=372, y=559)

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

    def signup_func(self):
        # Retrieve entered values
        entered_username = self.username.get()
        entered_password = self.password.get()
        entered_contact_number = self.contact_number.get()
        entered_email_address = self.email_address.get()
        entered_birthday = self.birthday.get()
        entered_gender = self.gender.get()

        # Clear entry widgets after registration
        self.username.delete(0, END)
        self.password.delete(0, END)
        self.contact_number.delete(0, END)
        self.email_address.delete(0, END)
        self.birthday.delete(0, END)
        self.gender.set("Male")

        if not entered_username or not entered_password or not entered_contact_number or not entered_email_address or not entered_birthday:
            messagebox.showerror("Input Error", "All fields are required.")
            return

        user = check_user(entered_username)

        if user:
            messagebox.showerror("Signup Failed", "Username already exists.")
            return

        insert_user(entered_username, entered_password, entered_contact_number, entered_email_address, entered_birthday,
                    entered_gender)

        messagebox.showinfo("Signup Successful", "Account created successfully!")

    def go_to_login(self):
        self.controller.show_login_page()



from tkinter import messagebox
from datetime import datetime
from customtkinter import *
import config
from tkcalendar import Calendar

from session import ActiveUser


class Account(CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, width=865, height=674, fg_color="transparent")

        account_title_label = CTkLabel(master=self,
                                   text="ACCOUNT",
                                   font=("Roboto", 40, "bold"))
        account_title_label.place(x=26, y=88)

        # Username Settings
        self.date_window = None
        self.cal = None
        username_label = CTkLabel(master=self,
                                  height=16,
                                  width=64,
                                  text="Username",
                                  font=("Roboto", 14))
        username_label.place(x=170, y=172)

        self.username = CTkEntry(master=self,
                                 height=55,
                                 width=275,
                                 corner_radius=35,
                                 border_color=config.secondary,
                                 placeholder_text_color=config.text,
                                 font=("Roboto", 18))
        self.username.place(x=149, y=197)

        # Password Settings
        password_label = CTkLabel(master=self,
                                  height=17,
                                  width=69,
                                  text="Password",
                                  font=("Roboto", 14))
        password_label.place(x=467, y=172)

        self.password = CTkEntry(master=self,
                                 height=55,
                                 width=275,
                                 corner_radius=35,
                                 border_color=config.secondary,
                                 placeholder_text_color=config.text,
                                 show="*",
                                 font=("Roboto", 18))
        self.password.place(x=443, y=196)

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
        self.show_password.place(x=480, y=259)

        # Contact Number
        contact_number_label = CTkLabel(master=self,
                                        height=17,
                                        width=114,
                                        text="Contact Number",
                                        font=("Roboto", 14))
        contact_number_label.place(x=170, y=287)

        self.contact_number = CTkEntry(master=self,
                                       height=55,
                                       width=275,
                                       corner_radius=35,
                                       border_color=config.secondary,
                                       placeholder_text_color=config.text,
                                       font=("Roboto", 18))
        self.contact_number.place(x=149, y=312)

        # Email Address
        email_address_label = CTkLabel(master=self,
                                       height=17,
                                       width=99,
                                       text="Email Address",
                                       font=("Roboto", 14))
        email_address_label.place(x=467, y=287)

        self.email_address = CTkEntry(master=self,
                                      height=55,
                                      width=275,
                                      corner_radius=35,
                                      border_color=config.secondary,
                                      placeholder_text_color=config.text,
                                      font=("Roboto", 18))
        self.email_address.place(x=443, y=312)

        # Birthday
        birthday_label = CTkLabel(master=self,
                                  height=16,
                                  width=52,
                                  text="Birthday",
                                  font=("Roboto", 14))
        birthday_label.place(x=170, y=404)

        choose_date = CTkButton(master=self,
                                height=14,
                                width=69,
                                hover_color=config.background,
                                fg_color="transparent",
                                text_color=config.text,
                                text="Choose Date",
                                font=("Roboto", 14),
                                command=self.choose_date)
        choose_date.place(x=323, y=404)

        self.birthday = CTkEntry(master=self,
                                 height=55,
                                 width=275,
                                 corner_radius=35,
                                 border_color=config.secondary,
                                 placeholder_text_color=config.text,
                                 placeholder_text="mm/dd/yy",
                                 font=("Roboto", 18))
        self.birthday.place(x=149, y=429)

        # Gender
        gender_label = CTkLabel(master=self,
                                height=17,
                                width=50,
                                text="Gender",
                                font=("Roboto", 14))
        gender_label.place(x=467, y=404)

        self.gender = CTkComboBox(master=self,
                                  height=55,
                                  width=275,
                                  corner_radius=35,
                                  border_color=config.secondary,
                                  button_color=config.secondary,
                                  button_hover_color=config.secondary,
                                  font=("Roboto", 18),
                                  values=["Male", "Female", "Others"])
        self.gender.place(x=443, y=429)

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
        self.save_button.place(x=345, y=523)

        self.load_account_details()

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
        selected_date = self.cal.get_date()

        try:
            formatted_date = datetime.strptime(selected_date, "%m/%d/%y").strftime("%Y-%m-%d")

            self.birthday.delete(0, END)
            self.birthday.insert(0, formatted_date)

            self.date_window.destroy()

        except ValueError:
            messagebox.showerror("Date Error", "An error occurred while processing the selected date.")

    def save_func(self):
        # Get updated user input
        new_username = self.username.get().strip()
        new_password = self.password.get().strip()
        new_contact_number = self.contact_number.get().strip()
        new_email = self.email_address.get().strip()
        new_birthdate = self.birthday.get().strip()
        new_gender = self.gender.get().strip()

        # Validation
        if not new_username or not new_password or not new_contact_number or not new_email or not new_birthdate or not new_gender:
            messagebox.showerror("Input Error", "All fields are required.")
            return

        if len(new_password) < 8:
            messagebox.showerror("Invalid Password", "Password must be at least 8 characters long.")
            return

        if not new_contact_number.isdigit() or not new_contact_number.startswith("09") or len(new_contact_number) != 11:
            messagebox.showerror("Invalid Contact Number",
                                 "Contact Number must be exactly 11 digits long and start with '09'.")
            return

        if '@' not in new_email or '.' not in new_email.split('@')[-1]:
            messagebox.showerror("Invalid Email", "Please enter a valid email address.")
            return

        # Update the database
        from database import update_user
        success = update_user(
            user_id=ActiveUser.user_id,
            username=new_username,
            password=new_password,
            contact_number=new_contact_number,
            email=new_email,
            birthdate=new_birthdate,
            gender=new_gender
        )

        # Feedback to the user
        if success:
            messagebox.showinfo("Success", "Account details updated successfully.")
            # Update the ActiveUser session
            ActiveUser.set_user(
                user_id=ActiveUser.user_id,
                username=new_username,
                password=new_password,
                contact_number=new_contact_number,
                email=new_email,
                birthdate=new_birthdate,
                gender=new_gender
            )
        else:
            messagebox.showerror("Update Failed", "Unable to update account details. Please try again later.")

    def load_account_details(self):
        self.username.insert(0, ActiveUser.username)
        self.password.insert(0, ActiveUser.password)
        self.contact_number.insert(0, ActiveUser.contact_number)
        self.email_address.insert(0, ActiveUser.email)
        self.birthday.insert(0, ActiveUser.birthdate)
        self.gender.set(ActiveUser.gender)
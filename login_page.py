from customtkinter import *
import customtkinter
from tkinter import messagebox
from database import check_user
import config
from session import ActiveUser

customtkinter.set_appearance_mode("light")

class LoginPage(CTk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("SmartStock Tracker - Login Page")
        self.configure(bg=config.background)
        self.protocol("WM_DELETE_WINDOW", self.controller.exit_app)
        # self.iconbitmap(config.app_icon)
        self.resizable(False, False)

        config.window_size(master=self, window_width=config.width, window_height=config.height)

        ctk_logo = CTkImage(light_image=config.app_logo, dark_image=config.app_logo, size=(564, 282))
        self.app_logo_label = CTkLabel(master=self, image=ctk_logo, text="")
        self.app_logo_label.place(x=118, y=34)

        self.username = CTkEntry(master=self,
                            height=50,
                            width=250,
                            corner_radius=35,
                            border_color=config.secondary,
                            placeholder_text="Username",
                            placeholder_text_color=config.text,
                            font=("Roboto", 18))
        self.username.place(x=293, y=316)

        ctk_logo_username = CTkImage(light_image=config.username_logo, dark_image=config.username_logo, size=(40, 40))
        username_logo_label = customtkinter.CTkLabel(master=self, image=ctk_logo_username, text="")
        username_logo_label.place(x=234, y=322)

        self.password = CTkEntry(master=self,
                            height=50,
                            width=250,
                            corner_radius=35,
                            border_color=config.secondary,
                            placeholder_text="Password",
                            placeholder_text_color=config.text,
                            show="*",
                            font=("Roboto", 18))
        self.password.place(x=293, y=387)

        ctk_logo_password = CTkImage(light_image=config.password_logo, dark_image=config.password_logo, size=(40, 40))
        password_logo_label = customtkinter.CTkLabel(master=self, image=ctk_logo_password, text="")
        password_logo_label.place(x=235, y=393)

        self.show_password_status = BooleanVar(value=False)

        show_password = CTkCheckBox(master=self,
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
        show_password.place(x=315, y=446)

        sign_in = CTkButton(master=self,
                            height=51,
                            width=109,
                            corner_radius=35,
                            border_color=config.secondary,
                            hover_color=config.clicked_secondary,
                            fg_color=config.secondary,
                            text="Sign-in",
                            font=("Roboto", 18),
                            command=self.login_button)
        sign_in.place(x=352, y=486)

        sign_up_label = CTkLabel(master=self,
                                 text="Don't have an account yet?",
                                 height=14,
                                 width=143,
                                 font=("Roboto", 12))
        sign_up_label.place(x=301, y=551)

        sign_up = CTkButton(master=self,
                            height=14,
                            width=40,
                            hover_color=config.background,
                            fg_color="transparent",
                            text_color=config.text,
                            text="Sign-up",
                            font=("Roboto", 12),
                            command=self.go_to_signup)
        sign_up.place(x=458, y=548)


    def go_to_signup(self):
        self.controller.show_signup_page()


    def show_password(self):
        if self.show_password_status.get():
            self.password.configure(show="")
        else:
            self.password.configure(show="*")

    def login_button(self):
        entered_username = self.username.get()
        entered_password = self.password.get()

        self.username.delete(0, END)
        self.password.delete(0, END)
        self.username.configure(placeholder_text="Username")
        self.password.configure(placeholder_text="Password")

        if entered_username == "" or entered_password == "":
            messagebox.showerror("Input Error", "Please enter both username and password.")
            return

        user = check_user(entered_username)

        if user:
            stored_password = user['password']

            if entered_password == stored_password:
                ActiveUser.set_user(user['user_id'],
                                    user['username'],
                                    user['password'],
                                    user['contact_number'],
                                    user['email'],
                                    user['birthdate'],
                                    user['gender'])
                self.controller.show_dashboard()
            else:
                messagebox.showerror("Login Failed", "Incorrect password.")
        else:
            messagebox.showerror("Login Failed", "User not found.")
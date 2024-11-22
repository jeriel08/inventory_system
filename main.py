from login_page import LoginPage
from signup_page import SignUpPage
from dashboard import Dashboard

class MainApp:
    def __init__(self):
        self.login_page = LoginPage(controller=self)
        self.signup_page = SignUpPage(controller=self)
        self.dashboard = Dashboard(controller=self)

    def show_login_page(self):
        self.dashboard.withdraw()
        self.signup_page.withdraw()
        self.login_page.deiconify()

    def show_signup_page(self):
        self.login_page.withdraw()
        self.signup_page.deiconify()

    def show_dashboard(self):
        self.login_page.withdraw()
        self.dashboard.deiconify()

    def run(self):
        self.show_login_page()
        self.login_page.mainloop()

    def exit_app(self):
        self.login_page.destroy()


if __name__ == "__main__":
    app = MainApp()
    app.run()

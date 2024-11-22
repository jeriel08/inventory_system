from customtkinter import *
import customtkinter
import config
import account_frame, hub_frame

customtkinter.set_appearance_mode("light")

class Dashboard(CTkToplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("SmartStock Tracker - Main App")
        self.configure(bg=config.background)
        self.protocol("WM_DELETE_WINDOW", self.controller.show_login_page)
        self.resizable(False, False)
        self.frames = {}

        config.window_size(master=self, window_width=config.d_width, window_height=config.d_height)

        # Posting Logo
        ctk_logo = CTkImage(light_image=config.app_logo, dark_image=config.app_logo, size=(255, 128))
        label = CTkLabel(master=self, image=ctk_logo, text="")
        label.place(x=60, y=37)

        self.title_label = CTkLabel(master=self,
                               text="",
                               font=("Roboto", 40, "bold"))
        self.title_label.place(x=355, y=70)

        # Inventory Button
        inventory_ctk = CTkImage(light_image=config.inventory_icon, dark_image=config.inventory_icon, size=(30, 30))

        inventory = CTkButton(master=self,
                           text="Inventory",
                           font=("Roboto", 24),
                           fg_color="transparent",
                           text_color=config.text,
                           image=inventory_ctk,
                           hover_color=config.secondary,
                           corner_radius=35,
                           command=self.show_inventory)
        inventory.place(x=63, y=222)

        # Timeline Button
        timeline_ctk = CTkImage(light_image=config.timeline_icon, dark_image=config.timeline_icon, size=(30, 30))

        timeline = CTkButton(master=self,
                           text="Timeline",
                           font=("Roboto", 24),
                           fg_color="transparent",
                           text_color=config.text,
                           image=timeline_ctk,
                           hover_color=config.secondary,
                           corner_radius=35,
                           command=self.show_timeline)
        timeline.place(x=63, y=297)

        # Hub Button
        hub_ctk = CTkImage(light_image=config.hub_icon, dark_image=config.hub_icon, size=(30, 30))

        hub = CTkButton(master=self,
                           text="Hub         ",
                           font=("Roboto", 24),
                           fg_color="transparent",
                           text_color=config.text,
                           image=hub_ctk,
                           hover_color=config.secondary,
                           corner_radius=35,
                           command=self.show_hub)
        hub.place(x=63, y=372)

        # Account Button
        account_ctk = CTkImage(light_image=config.account_icon, dark_image=config.account_icon, size=(30, 30))

        account = CTkButton(master=self,
                           text="Account",
                           font=("Roboto", 24),
                           fg_color="transparent",
                           text_color=config.text,
                           image=account_ctk,
                           hover_color=config.secondary,
                           corner_radius=35,
                           command=self.show_account)
        account.place(x=63, y=447)

        # Logout Button
        logout_ctk = CTkImage(light_image=config.logout_icon, dark_image=config.logout_icon, size=(30, 30))

        logout = CTkButton(master=self,
                           text="Logout",
                           font=("Roboto", 24),
                           fg_color="transparent",
                           text_color=config.text,
                           image=logout_ctk,
                           hover_color=config.secondary,
                           corner_radius=35,
                           command=self.logout_button)
        logout.place(x=63, y=522)

        self.withdraw()

        # Separator
        separator_line = CTkFrame(master=self,
                                  height=391,
                                  width=1,
                                  bg_color=config.secondary)
        separator_line.place(x=237, y=200)

    def show_inventory(self):
        self.title_label.configure(text="INVENTORY")
        self.hide_all_frames()

    def show_timeline(self):
        self.title_label.configure(text="TIMELINE")
        self.hide_all_frames()

    def show_hub(self):
        self.title_label.configure(text="HUB")
        self.hide_all_frames()
        if 'hub_panel' not in self.frames:
            hub_panel = hub_frame.OuterFrame(self)
            self.frames['hub_panel'] = hub_panel
        self.frames['hub_panel'].place(x=257,y=162)

    def show_account(self):
        self.title_label.configure(text="ACCOUNT")
        self.hide_all_frames()  # Hide all frames first
        if 'account_panel' not in self.frames:
            account_panel = account_frame.Account(self)
            self.frames['account_panel'] = account_panel
        self.frames['account_panel'].place(x=257, y=169)

    def hide_all_frames(self):
        for frame in self.frames.values():
            frame.place_forget()

    def logout_button(self):
        self.withdraw()
        self.controller.show_login_page()
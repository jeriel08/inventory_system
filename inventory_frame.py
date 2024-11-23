from customtkinter import *

class InventoryFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, width=865, height=674, bg_color="transparent")

        inventory_title_label = CTkLabel(master=self,
                               text="INVENTORY",
                               font=("Roboto", 40, "bold"))
        inventory_title_label.place(x=26, y=88)
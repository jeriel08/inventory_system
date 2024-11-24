from customtkinter import *

class TimelineFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, width=865, height=674, fg_color="transparent")

        timeline_title_label = CTkLabel(master=self,
                                         text="TIMELINE",
                                         font=("Roboto", 40, "bold"))
        timeline_title_label.place(x=26, y=88)


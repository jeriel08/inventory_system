from customtkinter import *
import config


class OuterFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, width=963, height=480, bg_color=config.background)
        self.frames = {}

        # Add Button
        add_ctk = CTkImage(light_image=config.add_icon,
                                 dark_image=config.add_icon,
                                 size=(22, 22))

        add_btn = CTkButton(master=self,
                            width=175,
                            height=50,
                            text="ADD",
                            text_color=config.text,
                            font=("Roboto", 18),
                            border_color=config.secondary,
                            corner_radius=35,
                            fg_color="transparent",
                            hover_color=config.secondary,
                            image=add_ctk,
                            command=self.show_add)
        add_btn.place(x=0, y=83)

        # Delete Button
        delete_ctk = CTkImage(light_image=config.delete_icon,
                           dark_image=config.delete_icon,
                           size=(22, 22))

        delete_btn = CTkButton(master=self,
                            width=175,
                            height=50,
                            text="DELETE",
                            text_color=config.text,
                            font=("Roboto", 18),
                            border_color=config.secondary,
                            corner_radius=35,
                            fg_color="transparent",
                            hover_color=config.secondary,
                            image=delete_ctk,
                            command=self.show_delete)
        delete_btn.place(x=0, y=174)

        # Update Button
        update_ctk = CTkImage(light_image=config.update_icon,
                           dark_image=config.update_icon,
                           size=(22, 22))

        update_btn = CTkButton(master=self,
                            width=175,
                            height=50,
                            text="UPDATE",
                            text_color=config.text,
                            font=('Roboto', 18),
                            border_color=config.secondary,
                            corner_radius=35,
                            fg_color="transparent",
                            hover_color=config.secondary,
                               image=update_ctk,
                               command=self.show_update)
        update_btn.place(x=0, y=265)

        # Clear Button
        clear_ctk = CTkImage(light_image=config.clear_icon,
                           dark_image=config.clear_icon,
                           size=(22, 22))

        clear_btn = CTkButton(master=self,
                               width=175,
                               height=50,
                               text="CLEAR",
                               text_color=config.text,
                               font=('Roboto', 18),
                               border_color=config.secondary,
                               corner_radius=35,
                               fg_color="transparent",
                               hover_color=config.secondary,
                               image=clear_ctk,
                               command=self.show_clear)
        clear_btn.place(x=0, y=356)

        separator = CTkFrame(master=self,
                             height=391,
                             width=1,
                             bg_color=config.secondary)
        separator.place(x=190, y=42)

    def show_add(self):
        self.hide_all_frames()
        if 'add_frame' not in self.frames:
            add_frame = AddFrame(self)
            self.frames['add_frame'] = add_frame
        self.frames['add_frame'].place(x=247, y=40)

    def show_delete(self):
        self.hide_all_frames()
        if 'delete_frame' not in self.frames:
            delete_frame = DeleteFrame(self)
            self.frames['delete_frame'] = delete_frame
        self.frames['delete_frame'].place(x=247, y=40)

    def show_update(self):
        self.hide_all_frames()
        if 'update_frame' not in self.frames:
            update_frame = UpdateFrame(self)
            self.frames['update_frame'] = update_frame
        self.frames['update_frame'].place(x=247, y=40)

    def show_clear(self):
        self.hide_all_frames()
        if 'clear_frame' not in self.frames:
            clear_frame = ClearFrame(self)
            self.frames['clear_frame'] = clear_frame
        self.frames['clear_frame'].place(x=247, y=40)

    def hide_all_frames(self):
        for frame in self.frames.values():
            frame.place_forget()

class AddFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, width=668, height=415, bg_color="transparent")

        title_label = CTkLabel(master=self,
                               text="ADD",
                               font=("Roboto", 20, "bold"))
        title_label.place(x=48, y=16)

class DeleteFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, width=668, height=415, bg_color="transparent")

        title_label = CTkLabel(master=self,
                               text="DELETE",
                               font=("Roboto", 20, "bold"))
        title_label.place(x=48, y=16)

class UpdateFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, width=668, height=415, bg_color="transparent")

        title_label = CTkLabel(master=self,
                               text="UPDATE",
                               font=("Roboto", 20, "bold"))
        title_label.place(x=48, y=16)

class ClearFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, width=668, height=415, bg_color="transparent")

        title_label = CTkLabel(master=self,
                               text="CLEAR",
                               font=("Roboto", 20, "bold"))
        title_label.place(x=48, y=16)
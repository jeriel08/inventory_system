from customtkinter import *
from datetime import datetime
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
                               text="ADD PRODUCTS",
                               font=("Roboto", 20, "bold"))
        title_label.place(x=67, y=16)

        # Product ID
        product_id_label = CTkLabel(master=self,
                                    width=72,
                                    height=16,
                                    text="Product ID:",
                                    font=("Roboto", 14))
        product_id_label.place(x=67, y=59)

        product_id_entry = CTkEntry(master=self,
                                    width=274,
                                    height=51,
                                    corner_radius=35,
                                    border_color=config.secondary,
                                    text_color=config.text,
                                    font=("Roboto", 18))
        product_id_entry.place(x=48, y=80)

        # Product Name
        product_name_label = CTkLabel(master=self,
                                    width=99,
                                    height=16,
                                    text="Product Name:",
                                    font=("Roboto", 14))
        product_name_label.place(x=362, y=59)

        product_name_entry = CTkEntry(master=self,
                                    width=274,
                                    height=51,
                                    corner_radius=35,
                                    border_color=config.secondary,
                                    text_color=config.text,
                                    font=("Roboto", 18))
        product_name_entry.place(x=343, y=80)

        # Price
        price_label = CTkLabel(master=self,
                                      width=38,
                                      height=16,
                                      text="Price:",
                                      font=("Roboto", 14))
        price_label.place(x=67, y=151)

        price_entry = CTkEntry(master=self,
                                      width=274,
                                      height=51,
                                      corner_radius=35,
                                      border_color=config.secondary,
                                      text_color=config.text,
                                      font=("Roboto", 18))
        price_entry.place(x=48, y=172)

        # Quantity
        quantity_label = CTkLabel(master=self,
                               width=59,
                               height=16,
                               text="Quantity:",
                               font=("Roboto", 14))
        quantity_label.place(x=362, y=151)

        quantity_entry = CTkEntry(master=self,
                               width=274,
                               height=51,
                               corner_radius=35,
                               border_color=config.secondary,
                               text_color=config.text,
                               font=("Roboto", 18))
        quantity_entry.place(x=343, y=172)

        # Category
        category_label = CTkLabel(master=self,
                                  width=62,
                                  height=16,
                                  text="Category:",
                                  font=("Roboto", 14))
        category_label.place(x=67, y=243)

        categories = ["Electronics", "Apparel", "Home Appliances", "Furniture", "Groceries", "Health & Beauty", "Books",
                      "Toy & Games", "Sports Equipment", "Office Supplies", "Pet Supplies"]

        category_entry = CTkComboBox(master=self,
                                  width=274,
                                  height=51,
                                  corner_radius=35,
                                  border_color=config.secondary,
                                  button_color=config.secondary,
                                  button_hover_color=config.clicked_secondary,
                                  text_color=config.text,
                                  values=categories,
                                  font=("Roboto", 18))
        category_entry.place(x=48, y=264)

        # Date
        date_label = CTkLabel(master=self,
                                  width=34,
                                  height=16,
                                  text="Date:",
                                  font=("Roboto", 14))
        date_label.place(x=362, y=243)

        current_date = datetime.now().date()
        formatted_date = current_date.strftime("%d/%m/%Y")

        date_entry = CTkEntry(master=self,
                                  width=274,
                                  height=51,
                                  corner_radius=35,
                                  border_color=config.secondary,
                                  text_color=config.text,
                                  placeholder_text="dd/mm/yy",
                                  font=("Roboto", 18))
        date_entry.place(x=343, y=264)
        date_entry.insert(0, formatted_date)

        # Sign-up Button
        self.add_button = CTkButton(master=self,
                                        width=177,
                                        height=51,
                                        text="ADD",
                                        corner_radius=35,
                                        border_color=config.accent,
                                        fg_color=config.secondary,
                                        hover_color=config.clicked_secondary,
                                        font=("Roboto", 18))
        self.add_button.place(x=244, y=348)

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
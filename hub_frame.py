from tkinter import messagebox

from customtkinter import *
import config
import database
from session import ActiveUser


class OuterFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, width=865, height=674, fg_color="transparent")
        self.frames = {}

        hub_title_label = CTkLabel(master=self,
                 text="HUB",
                 font=("Roboto", 40, "bold"))
        hub_title_label.place(x=26, y=88)

        self.sub_frame_title = CTkLabel(master=self,
                               text="",
                               font=("Roboto", 20, "bold"))
        self.sub_frame_title.place(x=26, y=144)

        # Add Button
        add_ctk = CTkImage(light_image=config.add_icon,
                                 dark_image=config.add_icon,
                                 size=(30, 30))

        add_btn = CTkButton(master=self,
                            width=175,
                            height=50,
                            text="ADD",
                            text_color=config.text,
                            font=("Roboto", 21),
                            border_color=config.secondary,
                            corner_radius=35,
                            fg_color="transparent",
                            hover_color=config.secondary,
                            image=add_ctk,
                            command=self.show_add)
        add_btn.place(x=3, y=230)

        # Delete Button
        delete_ctk = CTkImage(light_image=config.delete_icon,
                           dark_image=config.delete_icon,
                           size=(30, 30))

        delete_btn = CTkButton(master=self,
                            width=175,
                            height=50,
                            text="DELETE",
                            text_color=config.text,
                            font=("Roboto", 21),
                            border_color=config.secondary,
                            corner_radius=35,
                            fg_color="transparent",
                            hover_color=config.secondary,
                            image=delete_ctk,
                            command=self.show_delete)
        delete_btn.place(x=3, y=412)

        # Update Button
        update_ctk = CTkImage(light_image=config.update_icon,
                           dark_image=config.update_icon,
                           size=(30, 30))

        update_btn = CTkButton(master=self,
                            width=175,
                            height=50,
                            text="UPDATE",
                            text_color=config.text,
                            font=('Roboto', 21),
                            border_color=config.secondary,
                            corner_radius=35,
                            fg_color="transparent",
                            hover_color=config.secondary,
                               image=update_ctk,
                               command=self.show_update)
        update_btn.place(x=3, y=321)

        # Clear Button
        clear_ctk = CTkImage(light_image=config.clear_icon,
                           dark_image=config.clear_icon,
                           size=(30, 30))

        clear_btn = CTkButton(master=self,
                               width=175,
                               height=50,
                               text="CLEAR",
                               text_color=config.text,
                               font=('Roboto', 21),
                               border_color=config.secondary,
                               corner_radius=35,
                               fg_color="transparent",
                               hover_color=config.secondary,
                               image=clear_ctk,
                               command=self.show_clear)
        clear_btn.place(x=3, y=503)

        separator = CTkFrame(master=self,
                             height=388,
                             width=1,
                             bg_color=config.secondary)
        separator.place(x=222, y=190)

    def show_add(self):
        self.hide_all_frames()
        self.sub_frame_title.configure(text="-ADD-")
        if 'add_frame' not in self.frames:
            add_frame = AddFrame(self)
            self.frames['add_frame'] = add_frame
        self.frames['add_frame'].place(x=247, y=0)

    def show_delete(self):
        self.hide_all_frames()
        self.sub_frame_title.configure(text="-DELETE-")
        if 'delete_frame' not in self.frames:
            delete_frame = DeleteFrame(self)
            self.frames['delete_frame'] = delete_frame
        self.frames['delete_frame'].place(x=247, y=0)

    def show_update(self):
        self.hide_all_frames()
        self.sub_frame_title.configure(text="-UPDATE-")
        if 'update_frame' not in self.frames:
            update_frame = UpdateFrame(self)
            self.frames['update_frame'] = update_frame
        self.frames['update_frame'].place(x=247, y=0)

    def show_clear(self):
        self.hide_all_frames()
        self.sub_frame_title.configure(text="-CLEAR-")
        if 'clear_frame' not in self.frames:
            clear_frame = ClearFrame(self)
            self.frames['clear_frame'] = clear_frame
        self.frames['clear_frame'].place(x=247, y=0)

    def hide_all_frames(self):
        for frame in self.frames.values():
            frame.place_forget()

class AddFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, width=618, height=674, fg_color="transparent")

        # Product Section
        product_title_label = CTkLabel(master=self,
                               text="PRODUCT DETAILS",
                               font=("Roboto", 20, "bold"))
        product_title_label.place(x=43, y=97)

        # Product Name
        product_name_label = CTkLabel(master=self,
                                    width=99,
                                    height=16,
                                    text="Product Name:",
                                    font=("Roboto", 14))
        product_name_label.place(x=43, y=130)

        self.product_name_entry = CTkEntry(master=self,
                                    width=274,
                                    height=51,
                                    corner_radius=35,
                                    border_color=config.secondary,
                                    text_color=config.text,
                                    font=("Roboto", 18))
        self.product_name_entry.place(x=24, y=161)

        # Price
        price_label = CTkLabel(master=self,
                                      width=38,
                                      height=16,
                                      text="Price:",
                                      font=("Roboto", 14))
        price_label.place(x=43, y=232)

        self.price_entry = CTkEntry(master=self,
                                      width=274,
                                      height=51,
                                      corner_radius=35,
                                      border_color=config.secondary,
                                      text_color=config.text,
                                      font=("Roboto", 18))
        self.price_entry.place(x=24, y=253)

        # Quantity
        quantity_label = CTkLabel(master=self,
                               width=59,
                               height=16,
                               text="Quantity:",
                               font=("Roboto", 14))
        quantity_label.place(x=338, y=232)

        self.quantity_entry = CTkEntry(master=self,
                               width=274,
                               height=51,
                               corner_radius=35,
                               border_color=config.secondary,
                               text_color=config.text,
                               font=("Roboto", 18))
        self.quantity_entry.place(x=319, y=253)

        # Category
        category_label = CTkLabel(master=self,
                                  width=62,
                                  height=16,
                                  text="Category:",
                                  font=("Roboto", 14))
        category_label.place(x=338, y=140)

        categories = ["Electronics", "Apparel", "Home Appliances", "Furniture", "Groceries", "Health & Beauty", "Books",
                      "Toy & Games", "Sports Equipment", "Office Supplies", "Pet Supplies"]

        self.category_entry = CTkComboBox(master=self,
                                  width=274,
                                  height=51,
                                  corner_radius=35,
                                  border_color=config.secondary,
                                  button_color=config.secondary,
                                  button_hover_color=config.clicked_secondary,
                                  text_color=config.text,
                                  values=categories,
                                  font=("Roboto", 18))
        self.category_entry.place(x=319, y=161)

        # Supplier Section
        supplier_title_label = CTkLabel(master=self,
                                       text="SUPPLIER DETAILS",
                                       font=("Roboto", 20, "bold"))
        supplier_title_label.place(x=43, y=346)

        # Supplier Name
        supplier_name_label = CTkLabel(master=self,
                                      width=99,
                                      height=16,
                                      text="Supplier Name:",
                                      font=("Roboto", 14))
        supplier_name_label.place(x=43, y=389)

        self.supplier_name_entry = CTkEntry(master=self,
                                      width=274,
                                      height=51,
                                      corner_radius=35,
                                      border_color=config.secondary,
                                      text_color=config.text,
                                      font=("Roboto", 18))
        self.supplier_name_entry.place(x=24, y=410)

        # Contact Number
        contact_label = CTkLabel(master=self,
                               width=111,
                               height=16,
                               text="Contact Number:",
                               font=("Roboto", 14))
        contact_label.place(x=338, y=389)

        self.contact_entry = CTkEntry(master=self,
                               width=274,
                               height=51,
                               corner_radius=35,
                               border_color=config.secondary,
                               text_color=config.text,
                               font=("Roboto", 18))
        self.contact_entry.place(x=319, y=410)

        # Sign-up Button
        self.add_button = CTkButton(master=self,
                                        width=177,
                                        height=51,
                                        text="ADD",
                                        corner_radius=35,
                                        border_color=config.accent,
                                        fg_color=config.secondary,
                                        hover_color=config.clicked_secondary,
                                        font=("Roboto", 18),
                                    command=self.add_product)
        self.add_button.place(x=220, y=525)

    def add_product(self):
        product_name = self.product_name_entry.get().strip()
        quantity = self.quantity_entry.get().strip()
        price = self.price_entry.get().strip()
        category = self.category_entry.get().strip()
        supplier_name = self.supplier_name_entry.get().strip()
        supplier_contact = self.contact_entry.get().strip()

        price_float = float(price)

        if not all([product_name, quantity, price, category, supplier_name, supplier_contact]):
            messagebox.showerror("Input Error", "All fields must be filled.")
            return

        if not quantity.isdigit() or int(quantity) <= 0:
            messagebox.showerror("Input Error", "Quantity must be a positive integer.")
            return

        if not price.isdigit():
            messagebox.showerror("Input Error", "Price must be a positive integer.")
            return

        if not (0 <= price_float <= 99999999.99):
            messagebox.showerror("Input Error", "Price must be between 0 and 99,999,999.99.")
            return

        if not supplier_contact.isdigit() or len(supplier_contact) > 11:
            messagebox.showerror("Input Error", "Supplier contact must contain numbers only.")
            return

        existing_product = database.get_product_by_name(product_name)

        if existing_product:
            messagebox.showerror("Product Already Exist", "Product is already recorded. Update it instead.")
            return

        existing_supplier = database.get_supplier_by_name_and_contact(supplier_name, supplier_contact)

        if existing_supplier:
            supplier_id = existing_supplier['supplier_id']
        else:
            supplier_id = database.add_supplier(supplier_name, supplier_contact)
            if not supplier_id:
                messagebox.showerror("Error", "Failed to add supplier. Product not saved.")
                return

        if supplier_id:
            user_id = ActiveUser.user_id

            database.add_product(product_name=product_name, category=category, price=int(price), quantity=int(quantity), supplier_id=supplier_id, user_id=user_id)
            messagebox.showinfo("Success", "Product added successfully.")
        else:
            messagebox.showerror("Error", "Failed to add supplier. Product not saved.")

class DeleteFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, width=618, height=674, fg_color="transparent")

        # Initialize Variables
        self.product_name_var = StringVar()
        self.category_var = StringVar()
        self.quantity_var = StringVar()
        self.price_var = StringVar()
        self.supplier_name_var = StringVar()
        self.contact_number_var = StringVar()

        # Product Section
        product_title_label = CTkLabel(master=self,
                                       text="PRODUCT DETAILS",
                                       font=("Roboto", 20, "bold"))
        product_title_label.place(x=43, y=97)

        # Product Name
        product_name_label = CTkLabel(master=self,
                                      width=99,
                                      height=16,
                                      text="Product Name:",
                                      font=("Roboto", 14))
        product_name_label.place(x=43, y=130)

        self.product_name_combobox = CTkComboBox(master=self,
                                           width=274,
                                           height=51,
                                           corner_radius=35,
                                           border_color=config.secondary,
                                           button_color=config.secondary,
                                           button_hover_color=config.secondary,
                                           variable=self.product_name_var,
                                                 command=self.load_product_details,
                                           font=("Roboto", 18))
        self.product_name_combobox.place(x=24, y=161)

        # Price
        price_label = CTkLabel(master=self,
                               width=38,
                               height=16,
                               text="Price:",
                               font=("Roboto", 14))
        price_label.place(x=43, y=232)

        self.price_entry = CTkEntry(master=self,
                                    width=274,
                                    height=51,
                                    corner_radius=35,
                                    border_color=config.secondary,
                                    text_color=config.text,
                                    textvariable=self.price_var,
                                    font=("Roboto", 18))
        self.price_entry.place(x=24, y=253)

        # Quantity
        quantity_label = CTkLabel(master=self,
                                  width=59,
                                  height=16,
                                  text="Quantity:",
                                  font=("Roboto", 14))
        quantity_label.place(x=338, y=232)

        self.quantity_entry = CTkEntry(master=self,
                                       width=274,
                                       height=51,
                                       corner_radius=35,
                                       border_color=config.secondary,
                                       text_color=config.text,
                                       textvariable=self.quantity_var,
                                       font=("Roboto", 18))
        self.quantity_entry.place(x=319, y=253)

        # Category
        category_label = CTkLabel(master=self,
                                  width=62,
                                  height=16,
                                  text="Category:",
                                  font=("Roboto", 14))
        category_label.place(x=338, y=140)

        categories = ["Electronics", "Apparel", "Home Appliances", "Furniture", "Groceries", "Health & Beauty", "Books",
                      "Toy & Games", "Sports Equipment", "Office Supplies", "Pet Supplies"]

        self.category_entry = CTkComboBox(master=self,
                                          width=274,
                                          height=51,
                                          corner_radius=35,
                                          border_color=config.secondary,
                                          button_color=config.secondary,
                                          button_hover_color=config.clicked_secondary,
                                          text_color=config.text,
                                          variable=self.category_var,
                                          values=categories,
                                          font=("Roboto", 18))
        self.category_entry.place(x=319, y=161)

        # Supplier Section
        supplier_title_label = CTkLabel(master=self,
                                        text="SUPPLIER DETAILS",
                                        font=("Roboto", 20, "bold"))
        supplier_title_label.place(x=43, y=346)

        # Supplier Name
        supplier_name_label = CTkLabel(master=self,
                                       width=99,
                                       height=16,
                                       text="Supplier Name:",
                                       font=("Roboto", 14))
        supplier_name_label.place(x=43, y=389)

        self.supplier_name_entry = CTkEntry(master=self,
                                            width=274,
                                            height=51,
                                            corner_radius=35,
                                            border_color=config.secondary,
                                            text_color=config.text,
                                            textvariable=self.supplier_name_var,
                                            font=("Roboto", 18))
        self.supplier_name_entry.place(x=24, y=410)

        # Contact Number
        contact_label = CTkLabel(master=self,
                                 width=111,
                                 height=16,
                                 text="Contact Number:",
                                 font=("Roboto", 14))
        contact_label.place(x=338, y=389)

        self.contact_entry = CTkEntry(master=self,
                                      width=274,
                                      height=51,
                                      corner_radius=35,
                                      border_color=config.secondary,
                                      text_color=config.text,
                                      textvariable=self.contact_number_var,
                                      font=("Roboto", 18))
        self.contact_entry.place(x=319, y=410)

        # Delete Button
        self.delete_button = CTkButton(master=self,
                                    width=177,
                                    height=51,
                                    text="DELETE",
                                    corner_radius=35,
                                    border_color=config.accent,
                                    fg_color=config.exit_color,
                                    text_color=config.background,
                                    hover_color=config.exit_color_hover,
                                    command=self.delete_product,
                                    font=("Roboto", 18))
        self.delete_button.place(x=220, y=525)

        self.populate_product_combobox()

    def populate_product_combobox(self):
        products = database.fetch_product_name()
        self.product_name_combobox.configure(values=products)

    def load_product_details(self, product_name):
        product_details = database.fetch_product_detail(product_name)
        if product_details:
            self.category_entry.set(product_details[0])
            self.quantity_entry.insert(0, product_details[1])
            self.price_entry.insert(0, product_details[2])
            self.supplier_name_entry.insert(0, product_details[3])
            self.contact_entry.insert(0, product_details[4])
        else:
            messagebox.showerror("Error", "Product details not found.")

    def delete_product(self):
        product_name = self.product_name_var.get()

        if not product_name:
            messagebox.showerror("Error", "Please select a product to delete.")
            return

        database.delete_product(product_name)
        messagebox.showinfo("Success", f"Product '{product_name}' deleted successfully!")
        self.populate_product_combobox()
        self.clear_fields()

    def clear_fields(self):
        self.product_name_var.set("")
        self.category_var.set("")
        self.quantity_var.set("")
        self.price_var.set("")
        self.supplier_name_var.set("")
        self.contact_number_var.set("")

class UpdateFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, width=618, height=674, fg_color="transparent")

        # Product Section
        product_title_label = CTkLabel(master=self,
                                       text="PRODUCT DETAILS",
                                       font=("Roboto", 20, "bold"))
        product_title_label.place(x=43, y=97)

        # Product Name
        product_name_label = CTkLabel(master=self,
                                      width=99,
                                      height=16,
                                      text="Product Name:",
                                      font=("Roboto", 14))
        product_name_label.place(x=43, y=130)

        self.product_name_combobox = CTkComboBox(master=self,
                                                 width=274,
                                                 height=51,
                                                 corner_radius=35,
                                                 border_color=config.secondary,
                                                 button_color=config.secondary,
                                                 button_hover_color=config.secondary,
                                                 font=("Roboto", 18))
        self.product_name_combobox.place(x=24, y=161)

        # Price
        price_label = CTkLabel(master=self,
                               width=38,
                               height=16,
                               text="Price:",
                               font=("Roboto", 14))
        price_label.place(x=43, y=232)

        self.price_entry = CTkEntry(master=self,
                                    width=274,
                                    height=51,
                                    corner_radius=35,
                                    border_color=config.secondary,
                                    text_color=config.text,
                                    font=("Roboto", 18))
        self.price_entry.place(x=24, y=253)

        # Quantity
        quantity_label = CTkLabel(master=self,
                                  width=59,
                                  height=16,
                                  text="Quantity:",
                                  font=("Roboto", 14))
        quantity_label.place(x=338, y=232)

        self.quantity_entry = CTkEntry(master=self,
                                       width=274,
                                       height=51,
                                       corner_radius=35,
                                       border_color=config.secondary,
                                       text_color=config.text,
                                       font=("Roboto", 18))
        self.quantity_entry.place(x=319, y=253)

        # Category
        category_label = CTkLabel(master=self,
                                  width=62,
                                  height=16,
                                  text="Category:",
                                  font=("Roboto", 14))
        category_label.place(x=338, y=140)

        categories = ["Electronics", "Apparel", "Home Appliances", "Furniture", "Groceries", "Health & Beauty", "Books",
                      "Toy & Games", "Sports Equipment", "Office Supplies", "Pet Supplies"]

        self.category_entry = CTkComboBox(master=self,
                                          width=274,
                                          height=51,
                                          corner_radius=35,
                                          border_color=config.secondary,
                                          button_color=config.secondary,
                                          button_hover_color=config.clicked_secondary,
                                          text_color=config.text,
                                          values=categories,
                                          font=("Roboto", 18))
        self.category_entry.place(x=319, y=161)

        # Supplier Section
        supplier_title_label = CTkLabel(master=self,
                                        text="SUPPLIER DETAILS",
                                        font=("Roboto", 20, "bold"))
        supplier_title_label.place(x=43, y=346)

        # Supplier Name
        supplier_name_label = CTkLabel(master=self,
                                       width=99,
                                       height=16,
                                       text="Supplier Name:",
                                       font=("Roboto", 14))
        supplier_name_label.place(x=43, y=389)

        self.supplier_name_entry = CTkEntry(master=self,
                                            width=274,
                                            height=51,
                                            corner_radius=35,
                                            border_color=config.secondary,
                                            text_color=config.text,
                                            font=("Roboto", 18))
        self.supplier_name_entry.place(x=24, y=410)

        # Contact Number
        contact_label = CTkLabel(master=self,
                                 width=111,
                                 height=16,
                                 text="Contact Number:",
                                 font=("Roboto", 14))
        contact_label.place(x=338, y=389)

        self.contact_entry = CTkEntry(master=self,
                                      width=274,
                                      height=51,
                                      corner_radius=35,
                                      border_color=config.secondary,
                                      text_color=config.text,
                                      font=("Roboto", 18))
        self.contact_entry.place(x=319, y=410)

        # Sign-up Button
        self.update_button = CTkButton(master=self,
                                        width=177,
                                        height=51,
                                        text="UPDATE",
                                        corner_radius=35,
                                        border_color=config.accent,
                                        fg_color=config.secondary,
                                        hover_color=config.clicked_secondary,
                                        font=("Roboto", 18))
        self.update_button.place(x=220, y=525)

class ClearFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, width=618, height=674, fg_color="transparent")

        title_label = CTkLabel(master=self,
                               text="CLEAR INVENTORY",
                               font=("Roboto", 40, "bold"))
        title_label.place(x=133, y=144)

        warning = CTkLabel(master=self,
                               text="WARNING!",
                               font=("Roboto", 20, "bold"),
                           text_color="#D90303")
        warning.place(x=260, y=212)

        info_text = CTkLabel(master=self,
                               text="THIS OPERATION WILL CLEAR \nTHE INVENTORY THAT THE SYSTEM \nCURRENTLY HAVE.",
                               font=("Roboto", 20, "bold"))
        info_text.place(x=142, y=256)

        info_text1 = CTkLabel(master=self,
                             text="DO YOU WISH TO CONTINUE?",
                             font=("Roboto", 20, "bold"))
        info_text1.place(x=174, y=390)

        self.delete_button = CTkButton(master=self,
                                       width=177,
                                       height=51,
                                       text="CLEAR",
                                       corner_radius=35,
                                       border_color=config.accent,
                                       fg_color=config.exit_color,
                                       text_color=config.background,
                                       hover_color=config.exit_color_hover,
                                       font=("Roboto", 18))
        self.delete_button.place(x=220, y=479)
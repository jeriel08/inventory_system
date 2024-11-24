from customtkinter import *
from tkinter import ttk
import config


class InventoryFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, width=865, height=674, fg_color="transparent")

        inventory_title_label = CTkLabel(master=self,
                                         text="INVENTORY",
                                         font=("Roboto", 40, "bold"))
        inventory_title_label.place(x=26, y=88)

        # Configure Treeview style
        style = ttk.Style()
        style.configure(
            "Treeview",
            font=("Roboto", 14),  # Set font and size
            rowheight=30,  # Adjust row height
            borderwidth=1,  # Border width
            relief="solid",  # Border style
            background="white",  # Background color of rows
            fieldbackground="white",  # Background color of cells
            highlightthickness=0
        )
        style.configure(
            "Treeview.Heading",
            font=("Roboto", 14, "bold"),  # Header font
            background="#47B3A4",  # Header background
            foreground=config.text,  # Header text color
        )
        style.map(
            "Treeview",
            background=[("selected", "#47B3A4")],  # Row highlight color when selected
            foreground=[("selected", "white")]
        )

        columns = ("Product ID", "Product Name", "Price", "Quantity", "Category", "Date", "Supplier ID", "Supplier Name", "Contact Number")
        product_table = ttk.Treeview(master=self, columns=columns, show="headings")
        product_table.place(x=0, y=200, width=1060, height=623)

        # Treeview Scrollbar Config
        horizontal_scrollbar = ttk.Scrollbar(master=self, orient="horizontal", command=product_table.xview)
        horizontal_scrollbar.place(x=0, y=823, width=1080)

        vertical_scrollbar = ttk.Scrollbar(master=self, orient="vertical", command=product_table.yview)
        vertical_scrollbar.place(x=1060, y=200, height=623)

        # Link Treeview with Scrollbars
        product_table.configure(xscrollcommand=horizontal_scrollbar.set, yscrollcommand=vertical_scrollbar.set)

        # Format Columns
        product_table.column("Product ID", anchor=CENTER, width=120)
        product_table.column("Product Name", anchor=W, width=185)
        product_table.column("Price", anchor=CENTER, width=150)
        product_table.column("Quantity", anchor=CENTER, width=120)
        product_table.column("Category", anchor=W, width=185)
        product_table.column("Date", anchor=W, width=185)
        product_table.column("Supplier ID", anchor=W, width=120)
        product_table.column("Supplier Name", anchor=W, width=185)
        product_table.column("Contact Number", anchor=W, width=185)

        # Define the Headings
        for column in columns:
            product_table.heading(column, text=column)


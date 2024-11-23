from PIL import Image

def window_size(master, window_width, window_height):
    screen_width = master.winfo_screenwidth()
    screen_height = master.winfo_screenheight()
    position_x = (screen_width // 2) - (window_width // 2)
    position_y = (screen_height // 2) - (window_height // 2)
    master.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

# Dimensions for Login and Signup
width = 800
height = 600

d_width = 1280
d_height = 720

# Color Used
primary = "#0A2E53"
accent = "#3FA7D6"
secondary = "#47B3A4"
clicked_secondary = "#3C9C8E"
background = "#F5F7FA"
text = "#333333"
exit_color = "#B23B3B"
exit_color_hover = "#D9534F"

# Username Icon
username_logo = Image.open("images/username icon.png")

# Password Icon
password_logo = Image.open("images/password icon.png")

# Logo Import
app_logo = Image.open("images/Smart Stock Logo.png")

# App Icon
app_icon = Image.open("images/app logo.ico")

# Dashboard Icons
inventory_icon = Image.open("images/inventory icon.png")
timeline_icon = Image.open("images/timeline icon.png")
hub_icon = Image.open("images/hub icon.png")
account_icon = Image.open("images/username icon.png")
logout_icon = Image.open("images/logout icon.png")

# Hub Icons
add_icon = Image.open("images/add icon.png")
delete_icon = Image.open("images/delete icon.png")
update_icon = Image.open("images/update icon.png")
clear_icon = Image.open("images/clear icon.png")

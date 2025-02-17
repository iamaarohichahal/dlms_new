import tkinter as tk
import time
from ui.common import show_frame
from tkinter import ttk






def setUp_admin_wishlist_frame(admin_wishlist_frame):
    # Load the background image
    bg_image = tk.PhotoImage(file=r"C:\Users\iamaa\software\CSIA\dlms\images\bg.png")

    # Add the background image to the frame
    bg_label = tk.Label(admin_wishlist_frame, image=bg_image)
    bg_label.image = bg_image  
    bg_label.place(relwidth=1, relheight=1)  # Make it cover the entire frame

    # Title label
    title = tk.Label(admin_wishlist_frame, text="Book Wishlist", font=("times new roman", 40, "bold"), bg="#69359c", fg="white")
    title.place(x=0, y=0, relwidth=1, height=70)
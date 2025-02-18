import tkinter as tk
import time
from ui.common import show_frame
from tkinter import ttk, END



def populate_wishlist(wishlist_tree, shared_data):
    wishlist_queue = shared_data.get_wishlist_queue()
    book = wishlist_queue.get()
    user_id = shared_data.get_user_id()
    wishlist_tree.delete(*wishlist_tree.get_children())
    wishlist_tree.insert("", "end", values=(book.get_title(), book.get_author(),user_id))
    
    




def setUp_admin_wishlist_frame(admin_wishlist_frame,shared_data,admin_dashboard_frame):
    bg_image = tk.PhotoImage(file=r"C:\Users\iamaa\software\CSIA\dlms\images\bg.png")

    bg_label = tk.Label(admin_wishlist_frame, image=bg_image)
    bg_label.image = bg_image  
    bg_label.place(relwidth=1, relheight=1) 


    title = tk.Label(admin_wishlist_frame, text="Book Wishlist", font=("times new roman", 40, "bold"), bg="#69359c", fg="white")
    title.place(x=0, y=0, relwidth=1, height=70)


    style = ttk.Style(admin_wishlist_frame)
    style.theme_use('clam')
    style.configure('Treeview', font=("Arial", 14))
    style.map('Treeview', background=[('selected', '#1A8F2D')])


    wishlist_tree = ttk.Treeview(admin_wishlist_frame, height=20, columns=( 'Book Title', 'Book Author'))


    wishlist_tree.column('#0', width=0, stretch=tk.NO)
    wishlist_tree.column('Book Title', anchor=tk.CENTER, width=400)
    wishlist_tree.column('Book Author', anchor=tk.CENTER, width=400)

    

  
    wishlist_tree.heading('Book Title', text='Book Title')
    wishlist_tree.heading('Book Author', text='Book Author')
  



   
    wishlist_tree.place(x=250, y=250)

    back_button= tk.Button(admin_wishlist_frame, text="Back", font=("Arial", 16, "bold"), bg="#4CAF50", fg="white", width=20, height=2, relief="solid", command=lambda: show_frame(admin_dashboard_frame))
    back_button.place(x=200, y=700)

    view_button = tk.Button(admin_wishlist_frame, text="View", font=("Arial", 16, "bold"), bg="#4CAF50", fg="white", width=20, height=2, relief="solid", command=lambda: populate_wishlist(wishlist_tree, shared_data))
    view_button.place(x=550, y=700)

    clear_button = tk.Button(admin_wishlist_frame, text="Clear", font=("Arial", 16, "bold"), bg="#4CAF50", fg="white", width=20, height=2, relief="solid")
    clear_button.place(x=850, y=700)

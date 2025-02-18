import tkinter as tk
from tkinter import PhotoImage
from ui.common import show_frame




def setUp_admin_dash(admin_dashboard_frame, user_management_frame, book_management_frame, loan_management_frame, login_frame, admin_wishlist_frame):

    bg_image = tk.PhotoImage(file=r"C:\Users\iamaa\software\CSIA\dlms\images\bg.png")


    bg_label = tk.Label(admin_dashboard_frame, image=bg_image)
    bg_label.image = bg_image  
    bg_label.place(relwidth=1, relheight=1)  


    title = tk.Label(admin_dashboard_frame, text="Admin Dashboard", font=("times new roman", 40, "bold"), bg="#69359c", fg="white")
    title.place(x=0, y=0, relwidth=1, height=70)


    button_style = {"font": ("Arial", 14),"bg": "#1A8F2D","fg": "white","width": 20,"height": 2}

    user_management_button = tk.Button(admin_dashboard_frame,text="Manage Users",command=lambda: show_frame(user_management_frame), **button_style)
    user_management_button.place(relx=0.5, rely=0.3, anchor='center')


    book_management_button = tk.Button(admin_dashboard_frame,text="Manage Books",command=lambda: show_frame(book_management_frame), **button_style)
    book_management_button.place(relx=0.5, rely=0.4, anchor='center')

    loan_management_button = tk.Button(admin_dashboard_frame,text="Manage Loans",command=lambda: show_frame(loan_management_frame),**button_style)
    loan_management_button.place(relx=0.5, rely=0.5, anchor='center')


    book_wishlist_button = tk.Button(admin_dashboard_frame,text="Book Wishlist",command=lambda: show_frame(admin_wishlist_frame),**button_style)
    book_wishlist_button.place(relx=0.5, rely=0.6, anchor='center')

    btn_logout_admin = tk.Button(admin_dashboard_frame,text="Logout",font=("Arial", 14),bg="#1A8F2D",fg="white",width=20,height=2,command=lambda: show_frame(login_frame))
    btn_logout_admin.place(relx=0.5, rely=0.7, anchor='center')


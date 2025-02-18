
import tkinter as tk
from tkinter import ttk, PhotoImage
from db_utils import Database
from ui.common import show_frame
from ui.login_ui import setUp_Login
from ui.register_ui import setUp_Register
from ui.admin_dashboard_ui import setUp_admin_dash
from ui.user_dashboard_ui import setUp_user_dash
from ui.user_management_ui import setUp_user_management
from ui.book_management_ui import setUp_book_management
from ui.browse_books_ui import setUp_browse_books
from ui.borrow_ui import setUp_borrow_books_frame
from ui.loan_details_ui import setUp_loan_details
from ui.loan_return_ui import setUp_loan_return_frame
from ui.loan_management_ui import setUp_loan_management
from ui.user_wishlist_ui import setUp_user_wishlist_frame
from ui.admin_wishlist_ui import setUp_admin_wishlist_frame
from shared import Shared




# Database Initialization
database = Database()
database.init_db()
database.close()


# Application Initialization
app = tk.Tk()
app.title("Library Management System")
app.geometry("1400x1000")


image_path = PhotoImage(file=r"C:\Users\iamaa\software\CSIA\dlms\images\bg.png")


# Login Frame
login_frame = tk.Frame(app, bg='white')
login_frame.place(relheight=1, relwidth=1)


bg_image = tk.Label(login_frame, image=image_path)
bg_image.place(relheight=1, relwidth=1)

# Frame Definitions
register_frame = tk.Frame(app, bg='white')
user_dashboard_frame = tk.Frame(app, bg='white')
admin_dashboard_frame = tk.Frame(app, bg='white')
add_book_frame = tk.Frame(app, bg='white')
browse_books_frame = tk.Frame(app, bg='white')
profile_frame = tk.Frame(app, bg='white')
deposit_book_frame = tk.Frame(app, bg='white')
account_details_frame = tk.Frame(app, bg='white')
wishlist_frame = tk.Frame(app, bg='white')
loan_details_frame = tk.Frame(app, bg='white')
borrowing_history_frame = tk.Frame(app, bg='white')
user_management_frame = tk.Frame(app, bg="white")
book_management_frame = tk.Frame(app, bg="white")
loan_management_frame = tk.Frame(app, bg="white")
reports_frame = tk.Frame(app, bg="white")
settings_frame = tk.Frame(app, bg="white")
borrow_frame = tk.Frame(app, bg="white")
loan_return_frame= tk.Frame(app,bg="white")
user_wishlist_frame= tk.Frame(app,bg="white")
admin_wishlist_frame = tk.Frame(app,bg="white")




for frame in (login_frame, register_frame, user_dashboard_frame, add_book_frame, browse_books_frame, profile_frame, deposit_book_frame, 
              account_details_frame, loan_details_frame, borrowing_history_frame, wishlist_frame, admin_dashboard_frame, user_management_frame, 
              book_management_frame, loan_management_frame, reports_frame, settings_frame, borrow_frame,loan_return_frame,user_wishlist_frame, admin_wishlist_frame):
    frame.place(relwidth=1, relheight=1)

shared_data = Shared()
setUp_Login(login_frame, register_frame, user_dashboard_frame, admin_dashboard_frame, shared_data)

setUp_Register(login_frame, register_frame, user_dashboard_frame, admin_dashboard_frame)

setUp_admin_dash(admin_dashboard_frame, user_management_frame,book_management_frame,loan_management_frame,login_frame,admin_wishlist_frame)

setUp_user_dash(user_dashboard_frame, browse_books_frame,profile_frame,login_frame,shared_data)

setUp_user_management(user_management_frame,admin_dashboard_frame)

setUp_book_management(book_management_frame,admin_dashboard_frame)


setUp_browse_books(browse_books_frame, shared_data, borrow_frame,user_dashboard_frame)

setUp_borrow_books_frame(borrow_frame, shared_data,browse_books_frame)

setUp_loan_details(loan_details_frame,user_dashboard_frame,shared_data,loan_return_frame)

setUp_loan_return_frame(loan_return_frame, show_frame, loan_details_frame, shared_data)



setUp_loan_management(loan_management_frame, admin_dashboard_frame)

setUp_user_wishlist_frame(user_wishlist_frame, profile_frame,shared_data)

setUp_admin_wishlist_frame(admin_wishlist_frame, shared_data,admin_dashboard_frame)






# Profile Frame Setup
 
bg_image = tk.PhotoImage(file=r"C:\Users\iamaa\software\CSIA\dlms\images\bg.png")

bg_label = tk.Label(profile_frame, image=bg_image)
bg_label.image = bg_image  
bg_label.place(relwidth=1, relheight=1) 
title = tk.Label(profile_frame, text="My Profile", font=("times new roman", 40, "bold"), bg="#69359c", fg="white")
title.place(x=0, y=0, relwidth=1, height=70)


loan_details_button = tk.Button(profile_frame, text="Loan Details", font=("Arial", 16, "bold"), bg="#4CAF50", fg="white", width=20, height=2, relief="solid", command=lambda: show_frame(loan_details_frame))
loan_details_button.place(relx=0.5, rely=0.4, anchor='center')

my_wishlist_button = tk.Button(profile_frame, text="My Wishlist", font=("Arial", 16, "bold"), bg="#4CAF50", fg="white", width=20, height=2, relief="solid", command=lambda: show_frame(user_wishlist_frame))
my_wishlist_button.place(relx=0.5, rely=0.5, anchor='center')


back_button = tk.Button(profile_frame, text="Back", font=("Arial", 16, "bold"), bg="#4CAF50", fg="white", width=20, height=2, relief="solid", command=lambda: show_frame(user_dashboard_frame))
back_button.place(relx=0.5, rely=0.6, anchor='center')



def setup_frame(frame, title_text, back_command):
    title = tk.Label(frame, text=title_text, font=("times new roman", 40, "bold"), bg="#69359c", fg="white")
    title.place(x=0, y=0, relwidth=1, height=70)
    back_button = tk.Button(frame, text="Back", font=("Arial", 14), command=back_command)
    back_button.place(relx=0.5, rely=0.9, anchor='center')


# Show Login Frame Initially
show_frame(login_frame)

# Run the Tkinter event loop
app.mainloop()
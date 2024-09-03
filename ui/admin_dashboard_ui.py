import tkinter as tk
from ui.common import show_frame


# -------------------------------------------
# Admin Dashboard Frame Setup
# -------------------------------------------

def setUp_admin_dash(admin_dashboard_frame, user_management_frame,book_management_frame,loan_management_frame,login_frame):
# Title label for Admin Dashboard Frame
    title = tk.Label(admin_dashboard_frame, text="Admin Dashboard", font=("times new roman", 40, "bold"), bg="#69359c", fg="white")
    title.place(x=0, y=0, relwidth=1, height=70)

    # Button to navigate to User Management
    user_management_button = tk.Button(admin_dashboard_frame, text="Manage Users", font=("Arial", 14), command=lambda: show_frame(user_management_frame))
    user_management_button.place(relx=0.5, rely=0.3, anchor='center')

    # Button to navigate to Book Management
    book_management_button = tk.Button(admin_dashboard_frame, text="Manage Books", font=("Arial", 14), command=lambda: show_frame(book_management_frame))
    book_management_button.place(relx=0.5, rely=0.4, anchor='center')

    # Button to navigate to Loan Management
    loan_management_button = tk.Button(admin_dashboard_frame, text="Manage Loans", font=("Arial", 14), command=lambda: show_frame(loan_management_frame))
    loan_management_button.place(relx=0.5, rely=0.5, anchor='center')

    # Logout button for Admin
    btn_logout_admin = tk.Button(admin_dashboard_frame, text="Logout", font=("times new roman", 12, "bold"), bg="white", width=15, command=lambda: show_frame(login_frame))
    btn_logout_admin.place(relx=0.5, rely=0.6, anchor='center')

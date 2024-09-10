import tkinter as tk
import time
from ui.common import show_frame

def update_time(clock_label):
    current_time = time.strftime('%H:%M:%S %p')  # Format: Hour:Minute:Second AM/PM
    current_date = time.strftime('%Y-%m-%d')     # Format: Year-Month-Day
    clock_label.config(text=f"{current_date} {current_time}")
    clock_label.after(1000, update_time, clock_label)  # Update the clock every second


# -------------------------------------------
# User Dashboard Frame Setup
# -------------------------------------------
def setUp_user_dash(user_dashboard_frame, search_book_frame,deposit_book_frame,profile_frame,login_frame):
# Title label for User Dashboard Frame
    title = tk.Label(user_dashboard_frame, text="User Dashboard", font=("times new roman", 40, "bold"), bg="#69359c", fg="white")
    title.place(x=0, y=0, relwidth=1, height=70)

    # Horizontal Menu Frame within User Dashboard
    DashboardMenu = tk.Frame(user_dashboard_frame, bd=2, relief="ridge", bg="white", height=50)
    DashboardMenu.place(relx=0, rely=0.07, relwidth=1, height=50)  # Place under the title and make it horizontal

    # Adding the clock label
    clock_label = tk.Label(DashboardMenu, font=("times new roman", 12, "bold"), bg="white")
    clock_label.pack(side=tk.LEFT, padx=10)  # Align it to the left

    # Start updating the clock
    update_time(clock_label)

    # Buttons for the horizontal menu, aligned to the right
    btn_search_for_book = tk.Button(DashboardMenu, text="Search for Book", font=("times new roman", 12, "bold"), bg="white", width=15, command=lambda: show_frame(search_book_frame))
    btn_search_for_book.pack(side=tk.RIGHT, padx=5, pady=5)

    btn_deposit_book = tk.Button(DashboardMenu, text="Deposit Book", font=("times new roman", 12, "bold"), bg="white", width=15, command=lambda: show_frame(deposit_book_frame))
    btn_deposit_book.pack(side=tk.RIGHT, padx=5, pady=5)

    btn_my_profile = tk.Button(DashboardMenu, text="My Profile", font=("times new roman", 12, "bold"), bg="white", width=15, command=lambda: show_frame(profile_frame))
    btn_my_profile.pack(side=tk.RIGHT, padx=5, pady=5)

    btn_logout = tk.Button(DashboardMenu, text="Logout", font=("times new roman", 12, "bold"), bg="white", width=15, command=lambda: show_frame(login_frame))
    btn_logout.pack(side=tk.RIGHT, padx=5, pady=5)
        
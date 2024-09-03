import tkinter as tk
from tkinter import ttk, messagebox 
from ui.common import show_frame
from db_utils import Database


def add_to_user_treeview(tree):
    database = Database('user.db')
    users = database.fetch_users()
    tree.delete(*tree.get_children())
    for user in users:
        tree.insert('', 'end', values=user)


def insert_user_treeview(id_enter,username_enter, password_enter,tree):
    database = Database('user.db')
    id = id_enter.get()
    username = username_enter.get()
    password = password_enter.get()
    if not (id and username and password):
        messagebox.showerror('Error', 'Please enter all the fields')
    else:
        database.insert_user(id, username, password)
        add_to_user_treeview(tree)
        messagebox.showinfo('Success', "Your data has been inserted")

# -------------------------------------------
# User Management Frame Setup
# -------------------------------------------
def setUp_user_management(user_management_frame,admin_dashboard_frame):
    # Styling for the Treeview widget
    style = ttk.Style(user_management_frame)
    style.theme_use('clam')
    style.configure('Treeview', font=("Arial", 14))
    style.map('Treeview', background=[('selected', '#1A8F2D')])

    # Creating the Treeview widget to display user data
    tree = ttk.Treeview(user_management_frame, height=30)

    # Defining columns for the Treeview
    tree['columns'] = ('ID', 'Username', 'Password')

    # Configuring columns
    tree.column('#0', width=0, stretch=tk.NO)
    tree.column('ID', anchor=tk.CENTER, width=150)
    tree.column('Username', anchor=tk.CENTER, width=350)
    tree.column('Password', anchor=tk.CENTER, width=350)

    # Defining headings
    tree.heading('ID', text='ID')
    tree.heading('Username', text='Username')
    tree.heading('Password', text='Password')

    # Placing the Treeview widget
    tree.place(x=450, y=50)

    add_to_user_treeview(tree)
# Title label for User Management Frame
    user_management_label = tk.Label(user_management_frame, text="User Management", font=("Arial", 20), bg="lightgrey")
    user_management_label.pack(pady=10)

    # Labels and Entry fields for User Details
    id_label = tk.Label(user_management_frame, font=("Arial", 14), text="User ID", bg="#69359c", fg="white")
    id_label.place(x=20, y=50)

    id_enter = tk.Entry(user_management_frame, font=("Arial", 14), bd=2, width=25, bg="#69359c", fg="white")
    id_enter.place(x=150, y=50)

    username_label = tk.Label(user_management_frame, font=("Arial", 14), text="Username", bg="#69359c", fg="white")
    username_label.place(x=20, y=110)

    username_enter = tk.Entry(user_management_frame, font=("Arial", 14), bd=2, width=25, bg="#69359c", fg="white")
    username_enter.place(x=150, y=110)

    password_label = tk.Label(user_management_frame, font=("Arial", 14), text="Password", bg="#69359c", fg="white")
    password_label.place(x=20, y=170)

    password_enter = tk.Entry(user_management_frame, font=("Arial", 14), bd=2, width=25, bg="#69359c", fg="white")
    password_enter.place(x=150, y=170)

    # Buttons for User Management Actions
    add_user_button = tk.Button(user_management_frame, font=("Arial", 14), text="Add User", command=lambda:insert_user_treeview(id_enter,username_enter, password_enter,tree))
    add_user_button.place(x=20, y=300)

    edit_user_button = tk.Button(user_management_frame, font=("Arial", 14), text="Edit User")
    edit_user_button.place(x=20, y=400)

    view_user_button = tk.Button(user_management_frame, font=("Arial", 14), text="View User")
    view_user_button.place(x=20, y=500)

    delete_user_button = tk.Button(user_management_frame, font=("Arial", 14), text="Delete User")
    delete_user_button.place(x=20, y=600)

   
    # Back button to return to Admin Dashboard
    back_button = tk.Button(user_management_frame, text="Back", font=("Arial", 14), command=lambda: show_frame(admin_dashboard_frame))
    back_button.place(relx=0.5, rely=0.9, anchor='center')
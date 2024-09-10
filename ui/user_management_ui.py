import tkinter as tk
from tkinter import ttk, messagebox, END
from ui.common import show_frame
from db_utils import Database


def clear (id_enter, username_enter, password_enter):
    id_enter.delete(0,END)
    username_enter.delete(0,END)
    password_enter.delete(0,END)

def display_user_data(event,tree,id_enter, username_enter, password_enter):
    print("row is selected")
    selected_item = tree.focus()
    if selected_item:
        row = tree.item(selected_item)['values']
        clear(id_enter, username_enter, password_enter)
        id_enter.insert(0,row[0])
        username_enter.insert(0,row[1])
        password_enter.insert(0,row[2])
    else:
        pass


    
def add_users_to_tree(tree):
    database = Database()
    users = database.fetch_users()
    tree.delete(*tree.get_children())
    for user in users:
        tree.insert('', 'end', values=user)


def insert_user_treeview(id_enter,username_enter, password_enter,tree):
    database = Database()
    id = id_enter.get()
    username = username_enter.get()
    password = password_enter.get()
    if not (id and username and password):
        messagebox.showerror('Error', 'Please enter all the fields')
    else:
        database.insert_user(id, username, password)
        add_users_to_tree(tree)
        messagebox.showinfo('Success', "Your data has been inserted")

def delete_user (id_enter,username_enter, password_enter,tree):
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror('Error', 'Chose a user to delete.')
    else:
        id = id_enter.get()
        print("id to be deleted:" + id)
        Database.delete_user(id)
        add_users_to_tree(tree)
        clear(id_enter,username_enter, password_enter)
        messagebox.showinfo('Success', 'Data has been deleted')

def edit_user(tree, id_enter, username_enter, password_enter):
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror('Error', "Choose a user to edit")
    else:
        id = id_enter.get()
        username = username_enter.get()
        password = password_enter.get()
        
        # Correct order of arguments: username, password, id
        Database.update_user(username, password, id)

        # Refresh the treeview
        add_users_to_tree(tree)
        
        # Clear the entry fields
        clear(id_enter, username_enter, password_enter)
        
        messagebox.showinfo('Success', 'Data has been edited')

      



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


    add_users_to_tree(tree)
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

    edit_user_button = tk.Button(user_management_frame, font=("Arial", 14), text="Edit User", command=lambda:edit_user(tree, id_enter, username_enter, password_enter))
    edit_user_button.place(x=20, y=400)

    view_user_button = tk.Button(user_management_frame, font=("Arial", 14), text="View User")
    view_user_button.place(x=20, y=500)

    delete_user_button = tk.Button(user_management_frame, font=("Arial", 14), text="Delete User", command=lambda:delete_user(id_enter,username_enter, password_enter,tree))
    delete_user_button.place(x=20, y=600)

   
    # Back button to return to Admin Dashboard
    back_button = tk.Button(user_management_frame, text="Back", font=("Arial", 14), command=lambda: show_frame(admin_dashboard_frame))
    back_button.place(relx=0.5, rely=0.9, anchor='center')

    # Bind the <<TreeviewSelect>> event to the display_user_data function
    tree.bind('<<TreeviewSelect>>' ,  lambda event: display_user_data(event,tree,id_enter, username_enter, password_enter))

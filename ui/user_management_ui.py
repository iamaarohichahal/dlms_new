import tkinter as tk
from tkinter import ttk, messagebox, END
from ui.common import show_frame
from db_utils import Database
from server.user_managment import User


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
    user_management = User()
    users = user_management.get_users()
    tree.delete(*tree.get_children())
    for user in users:
        tree.insert('', 'end', values=user)


def insert_user_treeview(id_enter,username_enter, password_enter,tree):

    id = id_enter.get()
    username = username_enter.get()
    password = password_enter.get()
    if not (id and username and password):
        messagebox.showerror('Error', 'Please enter all the fields')
    else:

        user_management = User()
        user_management.insert_user(id, username, password)
        add_users_to_tree(tree)
        messagebox.showinfo('Success', "Your data has been inserted")

def delete_user (id_enter,username_enter, password_enter,tree):
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror('Error', 'Chose a user to delete.')
    else:
        id = id_enter.get()
        print("id to be deleted:" + id)
        user_management= User()
        user_management.delete_user(id)
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
        
        user_management = User()
        user_management.edit_user(id,username,password)


        add_users_to_tree(tree)
        

        clear(id_enter, username_enter, password_enter)
        
        messagebox.showinfo('Success', 'Data has been edited')

def refresh_tree(tree):
    add_users_to_tree(tree)

      




def setUp_user_management(user_management_frame,admin_dashboard_frame):


    bg_image = tk.PhotoImage(file=r"C:\Users\iamaa\software\CSIA\dlms\images\bg.png")


    bg_label = tk.Label(user_management_frame, image=bg_image)
    bg_label.image = bg_image  
    bg_label.place(relwidth=1, relheight=1) 
  
    style = ttk.Style(user_management_frame)
    style.theme_use('clam')
    style.configure('Treeview', font=("Arial", 14))
    style.map('Treeview', background=[('selected', '#1A8F2D')])

  
    tree = ttk.Treeview(user_management_frame, height=30)

    tree['columns'] = ('ID', 'Username', 'Password')


    tree.column('#0', width=0, stretch=tk.NO)
    tree.column('ID', anchor=tk.CENTER, width=150)
    tree.column('Username', anchor=tk.CENTER, width=350)
    tree.column('Password', anchor=tk.CENTER, width=350)


    tree.heading('ID', text='ID')
    tree.heading('Username', text='Username')
    tree.heading('Password', text='Password')


    tree.place(x=450, y=100)


    add_users_to_tree(tree)
  
    user_management_label = tk.Label(user_management_frame, text="User Management",  font=("times new roman", 40, "bold"), bg="#69359c", fg="white")
    user_management_label.place(x=0, y=0, relwidth=1, height=70)

    
    id_label = tk.Label(user_management_frame, font=("Arial", 14), text="User ID", bg="white", fg="black")
    id_label.place(x=20, y=100)

    id_enter = tk.Entry(user_management_frame, font=("Arial", 14), bd=2, width=25, bg="white", fg="black")
    id_enter.place(x=150, y=100)

    username_label = tk.Label(user_management_frame, font=("Arial", 14), text="Username", bg="white", fg="black")
    username_label.place(x=20, y=160)

    username_enter = tk.Entry(user_management_frame, font=("Arial", 14), bd=2, width=25, bg="white", fg="black")
    username_enter.place(x=150, y=160)

    password_label = tk.Label(user_management_frame, font=("Arial", 14), text="Password", bg="white", fg="black")
    password_label.place(x=20, y=220)

    password_enter = tk.Entry(user_management_frame, font=("Arial", 14), bd=2, width=25, bg="white", fg="black")
    password_enter.place(x=150, y=220)


    button_style = {"font": ("Arial", 14), "bg": "#1A8F2D","fg": "white","width": 20,"height": 2}


    add_user_button = tk.Button(user_management_frame, text="Add User",command=lambda: insert_user_treeview(id_enter, username_enter, password_enter, tree), **button_style)
    add_user_button.place(x=20, y=350)

    edit_user_button = tk.Button(user_management_frame,text="Edit User",command=lambda: edit_user(tree, id_enter, username_enter, password_enter),**button_style)
    edit_user_button.place(x=20, y=450)

    view_user_button = tk.Button(user_management_frame,text="View User",**button_style)
    view_user_button.place(x=20, y=550)

    delete_user_button = tk.Button(user_management_frame,text="Delete User",command=lambda: delete_user(id_enter, username_enter, password_enter, tree),**button_style)
    delete_user_button.place(x=20, y=650)

    refresh_button = tk.Button(user_management_frame,text="Refresh",command=lambda:refresh_tree(tree),**button_style)
    refresh_button.place(x=20, y=750)

    back_button = tk.Button(user_management_frame,text="Back",command=lambda: show_frame(admin_dashboard_frame),**button_style)
    back_button.place(relx=0.5, rely=0.9, anchor='center')

    tree.bind('<<TreeviewSelect>>' ,  lambda event: display_user_data(event,tree,id_enter, username_enter, password_enter))

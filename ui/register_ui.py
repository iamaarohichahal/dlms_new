import tkinter as tk
from tkinter import messagebox, simpledialog
from ui.common import show_frame
from server.user_managment import User_management




def register_user(type_of_user,username, password,login_frame):
    user_management = User_management()

    status = user_management.register_user(type_of_user, username, password)

    if status == 'true':

        messagebox.showinfo('Registration', 'Registration successful! Please log in.')
        show_frame(login_frame) 
    else:
       
        messagebox.showerror('Error', 'Username already exists')



# -------------------------------------------
# Registration Frame Setup
# -------------------------------------------
def setUp_Register(login_frame, register_frame, user_dashboard_frame, admin_dashboard_frame):
    
     # Load the background image
    bg_image = tk.PhotoImage(file=r"C:\Users\iamaa\software\CSIA\dlms\images\bg.png")

    # Add the background image to the register frame
    bg_label = tk.Label(register_frame, image=bg_image)
    bg_label.image = bg_image  # Keep a reference to avoid garbage collection
    bg_label.place(relwidth=1, relheight=1)  # Make it cover the entire frame

    # Title label for Registration Frame (overlaid on the background)
    title = tk.Label(register_frame, text="Add a New User", font=("times new roman", 40, "bold"), bg="#69359c", fg="white")
    title.place(x=0, y=0, relwidth=1, height=70)


    # Register button for User
    user_register_button = tk.Button(register_frame, text="Register User", font=("Arial", 14), 
                                    command=lambda: register_user('non_admin', 
                                        simpledialog.askstring("Register User", "Enter username:"),
                                        simpledialog.askstring("Register User", "Enter password:", show='*'),
                                        user_dashboard_frame
                                    ))
    user_register_button.place(relx=0.5, rely=0.4, anchor='center')

    # Register button for Admin
    admin_register_button = tk.Button(register_frame, text="Register Admin", font=("Arial", 14), 
                                    command=lambda: register_user('admin', 
                                        simpledialog.askstring("Register Admin", "Enter username:"),
                                        simpledialog.askstring("Register Admin", "Enter password:", show='*'),
                                        admin_dashboard_frame
                                    ))
    admin_register_button.place(relx=0.5, rely=0.5, anchor='center')

    # Back to Login button
    back_button = tk.Button(register_frame, text="Back to Login", font=("Arial", 14), command=lambda: show_frame(login_frame))
    back_button.place(relx=0.5, rely=0.6, anchor='center')

from tkinter import *

class DLMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Digital Library Management System")

        # Title
        title = Label(self.root, text="Browse Books", font=("times new roman", 40, "bold"),bg="#69359c",fg="white")
        title.place(x=0, y=0, relwidth=1, height=70)

        #left menu for browse books 
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE)
        LeftMenu.place(x=0,y=102,width)


root = Tk()
obj = DLMS(root)
root.mainloop()

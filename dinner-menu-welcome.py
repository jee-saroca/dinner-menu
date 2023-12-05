import tkinter as tk
from tkinter import *

dinnerMenu = Tk()
dinnerMenu.geometry("450x550")
dinnerMenu.title("Dinner Menu")

welcome = Label(dinnerMenu,text="Welcome to \nThe Dinner Place",
                bg='#f9f1f1',fg='black',
                font=('BookmanOldStyle',40))
welcome.pack()

dinnerMenu.mainloop()

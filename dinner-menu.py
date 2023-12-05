import tkinter as tk
from tkinter import *

# GUI -------------------------
dinnerMenu = Tk()
dinnerMenu.geometry("450x550")
dinnerMenu.title("Dinner Menu")
dinnerMenu.config(bg='#f9f1f1')

# WELCOME ------------------------------
welcome = Label(dinnerMenu,text="Welcome to \nThe Dinner Place",
                bg='#f9f1f1',fg='black',
                font=('BookmanOldStyle',40))
welcome.pack()

# start_btn
def startOrder():
    startBtn.destroy()
    rad_wing.pack(anchor=CENTER)
    rad_fries.pack(anchor=CENTER)
    rad_oysters.pack(anchor=CENTER)
    afterBtnApp.pack(anchor=S)

startBtn = Button(dinnerMenu,text="Order",command=startOrder,
                     bg="#f9f1f1")
startBtn.pack()

# CHECKBOXES -----------------------------------------

def Button_1():
    label_1.configure(text="Done")

label_1 = tk.Label(dinnerMenu, text="What will you be having?")
label_1.pack()

checkbutton_1 = tk.Checkbutton(dinnerMenu, text="Appetizer", width=12)
checkbutton_1.pack()

checkbutton_2 = tk.Checkbutton(dinnerMenu, text="Drink", width=12)
checkbutton_2.pack()

checkbutton_3 = tk.Checkbutton(dinnerMenu, text="Main Course", width=12)
checkbutton_3.pack()

checkbutton_4 = tk.Checkbutton(dinnerMenu, text="Dessert", width=12)
checkbutton_4.pack()


# --------someone create radio buttons for Appetizers (Wings, Fries, Oysters)

sup 




# someone create radio buttons for Drink (Virgin Sangria, Virgin Mimosa, Virgin Wine, Virgin Margarita)




# someone create radio buttons for Main Course (Bucket of Fried Chicken, Filet Mignon, Salmon)




# someone create radio buttons for Dessert (Double Choclate Cake, Vanilla Ice Cream)



# someone create a dinner layout with a table and each chosen food.


dinnerMenu.mainloop()
# someone create a receipt




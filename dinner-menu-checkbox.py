
import tkinter as tk

dinnerMenu = tk.Tk()
dinnerMenu.geometry("550x550")
dinnerMenu.title("Dinner Menu")



def Button_1():
    label_1.configure(text="Done")

label_1 = tk.Label(dinnerMenu, text="What will you be having?")
label_1.pack()

checkbutton_1 = tk.Checkbutton(dinnerMenu, text="Appetizer", width=12)
checkbutton_1.pack()

checkbutton_2 = tk.Checkbutton(dinnerMenu, text="Dink", width=12)
checkbutton_2.pack()

checkbutton_3 = tk.Checkbutton(dinnerMenu, text="Main Couese", width=12)
checkbutton_3.pack()

checkbutton_4 = tk.Checkbutton(dinnerMenu, text="Dessert", width=12)
checkbutton_4.pack()

B2 = tk.Button(dinnerMenu, text="Next", command=Button_1)
B2.pack()

dinnerMenu.mainloop()

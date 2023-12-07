import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

# GUI -------------------------
dinnerMenu = Tk()
dinnerMenu.geometry("450x650")
dinnerMenu.title("Dinner Menu")
dinnerMenu.config(bg='#f9f1f1')
dinnerMenu.resizable(False,False)

# WELCOME ------------------------------
welcome = Label(dinnerMenu,text="Welcome to \nThe Dinner Place",
                bg='#f9f1f1',fg='black',
                font=('BookmanOldStyle',35))
welcome.pack()

# start_btn
def startOrder(): # displays checkboxes
    startBtn.destroy()
    label_1.pack()
    checkbutton_1.pack()
    checkbutton_2.pack()
    checkbutton_3.pack()
    checkbutton_4.pack()
    submitBTN.pack() # maybe when this button is clicked, the checkbuttons send out their commands?
startBtn = Button(dinnerMenu,text="Order",command=startOrder,
                     bg="#f9f1f1")
startBtn.pack()

# Item costs: Drinks, App, Main, Dessert
vMim = 4.99
vSan = 5.99
vWin = 6.99
VMar = 4.99

hWin = 11.99
fFri = 9.99
rOys = 12.99

fChi = 18.99
bSal = 24.99
fMig = 29.99

dChoc = 21.99
vIce = 4.99

# CHECKBOXES -----------------------------------------
checkDrink = tk.StringVar()
checkApp = tk.StringVar()
checkMain = tk.StringVar()
checkDessert = tk.StringVar()


label_1 = tk.Label(dinnerMenu, text="What will you be having?", bg='#f9f1f1')


checkbutton_1 = tk.Checkbutton(dinnerMenu, text="Drink", bg='#f9f1f1',
                               variable=checkDrink, width=12,
                               onvalue="1", offvalue="0"
                               )
#print(checkApp)

checkbutton_2 = tk.Checkbutton(dinnerMenu, text="Appetizer", bg='#f9f1f1',
                               variable=checkApp, width=12,
                               onvalue="1", offvalue="0"
                               )

checkbutton_3 = tk.Checkbutton(dinnerMenu, text="Main Course", bg='#f9f1f1',
                               variable=checkMain, width=12,
                               onvalue="1", offvalue="0"
                               )

checkbutton_4 = tk.Checkbutton(dinnerMenu, text="Dessert", bg='#f9f1f1',
                               variable=checkDessert, width=12,
                               onvalue="1", offvalue="0"
                               )

# submit checkbox answers btn
def submitCB(): # main purpose is to lock the results so user cannot change
    submitBTN.destroy()
    # config(state="disabled") locks the answer
    checkbutton_1.config(state="disabled") # state arg disables the checkbutton from being clicked again-
    checkbutton_2.config(state="disabled") # this was to make sure that the user doesn't go back and change-
    checkbutton_3.config(state="disabled") # their answer.
    checkbutton_4.config(state="disabled")

    # displaying the radiobuttons
    if checkDrink.get() == "1":
        drinks_title.pack(anchor=CENTER)
        rad_mimosa.pack(anchor=CENTER)
        rad_sangria.pack(anchor=CENTER)
        rad_wine.pack(anchor=CENTER)
        rad_margarita.pack(anchor=CENTER)
    else:
        print("No drinks")

    if checkApp.get() == "1":
        appetizers_title.pack(anchor=CENTER)
        rad_wing.pack(anchor=CENTER)
        rad_fries.pack(anchor=CENTER)
        rad_oysters.pack(anchor=CENTER)
    else:
        print("No apps")

    if checkMain.get() == "1":
        main_title.pack(anchor=CENTER)
        rad_chicken.pack(anchor=CENTER)
        rad_fish.pack(anchor=CENTER)
        rad_beef.pack(anchor=CENTER)
    else:
        print("No mains")

    if checkDessert.get() == "1":
        dessert_title.pack(anchor=CENTER)
        rad_cake.pack(anchor=CENTER)
        rad_cream.pack(anchor=CENTER)
        dessert_title.pack(anchor=CENTER)
    else:
        print("No desserts")
    sendOrder.pack(anchor=CENTER)

submitBTN = Button(dinnerMenu, text="Next", command=submitCB)

# APPETIZERS RADIO BTN ---------------------------
drinks_title = Label(dinnerMenu,text="Drinks",
                bg="#f9f1f1",fg="black",
                font=("BookmanOldStyle",20))

drinkVar = tk.IntVar()
rad_mimosa = Radiobutton(dinnerMenu, text="Virgin Mimosa", variable=drinkVar, value=1)
rad_mimosa.config(bg="#f9f1f1")
rad_sangria = Radiobutton(dinnerMenu, text="Virgin Sangria", variable=drinkVar, value=2)
rad_sangria.config(bg="#f9f1f1")
rad_wine = Radiobutton(dinnerMenu, text="Virgin Wine", variable=drinkVar, value=3)
rad_wine.config(bg="#f9f1f1")
rad_margarita = Radiobutton(dinnerMenu, text="Virgin Margarita", variable=drinkVar, value=4)
rad_margarita.config(bg="#f9f1f1")
print(drinkVar)

# DRINKS RADIO BTN ----------------------------------
appetizers_title = Label(dinnerMenu,text="Appetizers",
                bg="#f9f1f1",fg="black",
                font=("BookmanOldStyle",20)) # this could really be any font tbh, I couldn't find an appealing one

appVar = IntVar()
rad_wing = Radiobutton(dinnerMenu, text="Hot Wings", variable=appVar, value=1)
rad_wing.config(bg="#f9f1f1")
rad_fries = Radiobutton(dinnerMenu, text="French Fries", variable=appVar, value=2)
rad_fries.config(bg="#f9f1f1")
rad_oysters = Radiobutton(dinnerMenu, text="Raw Oysters", variable=appVar, value=3)
rad_oysters.config(bg="#f9f1f1")

# MAIN COURSES RADIO BTN ---------------------------------
main_title = Label(dinnerMenu,text="Main Courses",
                bg="#f9f1f1",fg="black",
                font=("BookmanOldStyle",20)) # this could really be any font tbh, I couldn't find an appealing one


mainVar = IntVar()
rad_chicken = Radiobutton(dinnerMenu, text="Fried Chicken", variable=mainVar, value=1)
rad_chicken.config(bg="#f9f1f1")
rad_fish = Radiobutton(dinnerMenu, text="Baked Salmon", variable=mainVar, value=2)
rad_fish.config(bg="#f9f1f1")
rad_beef = Radiobutton(dinnerMenu, text="Filet Mignon", variable=mainVar, value=3)
rad_beef.config(bg="#f9f1f1")

# DESSERT RADIO BTN -----------------------------------
dessert_title = Label(dinnerMenu,text="Dessert",
                bg="#f9f1f1",fg="black",
                font=("BookmanOldStyle",20)) # this could really be any font tbh, I couldn't find an appealing one

dessertVar = IntVar()
rad_cake = Radiobutton(dinnerMenu, text="Double Chocolate Cake", variable=dessertVar, value=1)
rad_cake.config(bg="#f9f1f1")
rad_cream = Radiobutton(dinnerMenu, text="Vanilla Ice Cream", variable=dessertVar, value=2)
rad_cream.config(bg="#f9f1f1")

#Reciept Code
def recieptCon():
    global recieptFrame
    recieptFrame.tkraise()
    recieptFrame = tk.Frame(bg="#F1F1E3", padx=5, pady=5)
    recieptFrame.place(x=0, y=0, width=450, height=650)
    labelRe = Label(recieptFrame,text="\nThe Dinner Place",bg="#F1F1E3", font=("BookmanOldStyle",24))
    labelRe2 = Label(recieptFrame, text="-------------------",bg="#F1F1E3", font=("Beirut", 18))
    labelRe.pack()
    labelRe2.pack()
    #labels for reciept information
    labelDriRe = "Drinks   --"
    labelAppRe = "Appetizers --"
    labelMainRe = "Main Course --"
    labelDesRe = "Dessert --"
    total = 0
    tax = 0.725
    totalCost = 0
    #Drinks If Statements
    if (drinkVar.get() == 1):
        labelDriRe += "  Virgin Mimosa -- "
        total += vMim
        labelDri = Label(recieptFrame,text= labelDriRe + str(vMim),bg="#F1F1E3", font=("Beirut",16))
        labelDri.pack()
    if (drinkVar.get() == 2):
        labelDriRe += "  Virgin Sangria -- "
        total += vSan
        labelDri = Label(recieptFrame,text= labelDriRe + str(vSan),bg="#F1F1E3", font=("Beirut",16))
        labelDri.pack()
    if (drinkVar.get() == 3):
        labelDriRe += "  Virgin Wine -- "
        total += vWin
        labelDri = Label(recieptFrame,text= labelDriRe + str(vWin),bg="#F1F1E3", font=("Beirut",16))
        labelDri.pack()
    if (drinkVar.get() == 4):
        labelDriRe += "  Virgin Margarita -- "
        total += vMar
        labelDri = Label(recieptFrame,text= labelDriRe + str(vMar),bg="#F1F1E3", font=("Beirut",16))
        labelDri.pack()
    #Appetizer if statements
    if(appVar.get() == 1):
        labelAppRe += " Hot Wings -- "
        total += hWin
        labelApp = Label(recieptFrame,text= labelAppRe + str(hWin),bg="#F1F1E3", font=("Beirut",16))
        labelApp.pack()
    if(appVar.get() == 2):
        labelAppRe += " French Fries -- "
        total += fFri
        labelApp = Label(recieptFrame,text= labelAppRe + str(fFri),bg="#F1F1E3", font=("Beirut",16))
        labelApp.pack()
    if(appVar.get() == 3):
        labelAppRe += " Raw Oysters -- "
        total += rOys
        labelApp = Label(recieptFrame,text= labelAppRe + str(rOys),bg="#F1F1E3", font=("Beirut",16))
        labelApp.pack()
    #Main Course if statements
    if(mainVar.get() == 1):
        labelMainRe += " Fried Chicken -- "
        total += fChi
        labelMain = Label(recieptFrame,text= labelMainRe + str(fChi),bg="#F1F1E3", font=("Beirut",16))
        labelMain.pack()
    if(mainVar.get() == 2):
        labelMainRe += " Baked Salmon -- "
        total += bSal
        labelMain = Label(recieptFrame,text= labelMainRe + str(bSal),bg="#F1F1E3", font=("Beirut",16))
        labelMain.pack()
    if(mainVar.get() == 3):
        labelMainRe += " Filet Mignon"
        total += fMig
        labelMain = Label(recieptFrame,text= labelMainRe + str(fMig),bg="#F1F1E3", font=("Beirut",16))
        labelMain.pack()
    # Dessert
    if(dessertVar.get() == 1):
        labelDesRe += " Double Choclate Cake -- "
        total += dChoc
        labelDes = Label(recieptFrame,text= labelDesRe + str(dChoc),bg="#F1F1E3", font=("Beirut",16))
        labelDes.pack()
    if(dessertVar.get() == 2):
        labelDesRe += " Vanilla Ice Cream -- "
        total += vIce
        labelDes = Label(recieptFrame,text= labelDesRe + str(vIce),bg="#F1F1E3", font=("Beirut",16))
        labelDes.pack()

    labelRe3 = Label(recieptFrame, text="-------------------",bg="#F1F1E3", font=("Beirut", 18))
    labelRe3.pack()
    labelTotal = Label(recieptFrame, text= "Pre-Total  --  " + str(total),bg="#F1F1E3", font=("Beirut", 18))
    labelTotal.pack()
    tax = total * 0.725
    labelTax = Label(recieptFrame, text= "Tax-Total  --  " + str(tax),bg="#F1F1E3", font=("Beirut", 18))
    labelTax.pack()
    
# SUBMIT ORDER BTN ----------------------------------------------
def submitOrder(): # this command will pop up a new window that will be an image of the meal chosen
    print("SUBMITTED")
    dinnerTable = (Toplevel(dinnerMenu))
    dinnerTable.geometry("450x450")
    dinnerTable.title("")
    dinnerTable.config(bg='#f9f1f1')
    dinnerTable.resizable(False, False)
    recieptCon()
    dinnerTable.mainloop()
sendOrder = Button(dinnerMenu, text="Send Order", command=submitOrder)

# DINNER TABLE POP UP ----------------------------------------
# pictures of food superimposed on top of a picture of a dinner table + layout

# button that makes noise + deletes food images

# RECEIPT Frame  -----------------------------------------------------------
recieptFrame = tk.Frame(bg="#F1F1E3", padx=5, pady=5)
recieptFrame.place(x=0, y=0, width=0, height=0)


dinnerMenu.mainloop()


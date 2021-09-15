## CS449 - SOS Game with Gui
## Justin Foster - 09/08/2021

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("Justin's SOS Game!")

#Global variables for decision making
click = False
counter = 0

#Welcome message that allows player to choose who is playing first
def playerChoice(boool):
        result = messagebox.askyesno("Welcome to SOS!", "Welcome to the game!\nWho is playing first?\nYes for red player, no for blue player!")
        if result == True:
            boool = True
            messagebox.showinfo("Red player", "You chose red player to go first!")
        elif result == False:
            boool = False
            messagebox.showinfo("Blue Player", "You chose blue player to go first!")
    

playerChoice(click)

#Function for clicking a button
def button_click(button):
    global click, counter

    if button["text"] == " " and click == True:
              button["text"] = "S"
              click = False
              counter += 1
    elif button["text"] == " " and click == False:
                button["text"] = "O"
                click = True
                counter += 1
    else:
        messagebox.showerror("SOS Game","Box has already been used!")

###Attaching a frame?
#MainFrame = Frame(root, bd=10, width=770, height=700, relief=RIDGE, bg='steel blue')
#MainFrame.grid()

##Game Logic
#Needs to search nearby S or S to see if an SOS has been made
def wonGame():
    global theWinner
    

#Creating Labels
redPlayer = Label(root, text = "Red Player", relief = RAISED)

bluePlayer = Label(root, text = "Blue Player", relief = RAISED)

#Buttons for placing S or O
#column 0
gameButton0 = Button(root, fg = "blue", text = " ", font = ("Helvitica", 20), height = 3, width = 6,
            command=lambda: button_click(gameButton0))
gameButton1 = Button(root, text = " ", font = ("Helvitica", 20), height = 3, width = 6,
            bg = "blue", command=lambda: button_click(gameButton1))
gameButton2 = Button(root, text = " ", font = ("Helvitica", 20), height = 3, width = 6,
            bg = "blue", command=lambda: button_click(gameButton2))
gameButton3 = Button(root, text = " ", font = ("Helvitica", 20), height = 3, width = 6,
            bg = "blue", command=lambda: button_click(gameButton3))
gameButton4 = Button(root, text = " ", font = ("Helvitica", 20), height = 3, width = 6,
            bg = "blue", command=lambda: button_click(gameButton4))
gameButton5 = Button(root, text = " ", font = ("Helvitica", 20), height = 3, width = 6,
            bg = "blue", command=lambda: button_click(gameButton5))
#column 1
gameButton6 = Button(root, text = " ", font = ("Helvitica", 20), height = 3, width = 6,
            bg = "blue", command=lambda: button_click(gameButton6))
gameButton7 = Button(root, text = " ", font = ("Helvitica", 20), height = 3, width = 6,
            bg = "blue", command=lambda: button_click(gameButton7))
gameButton8 = Button(root, text = " ", font = ("Helvitica", 20), height = 3, width = 6,
            bg = "blue", command=lambda: button_click(gameButton8))
gameButton9 = Button(root, text = " ", font = ("Helvitica", 20), height = 3, width = 6,
            bg = "blue", command=lambda: button_click(gameButton9))
gameButton10 = Button(root, text = " ", font = ("Helvitica", 20), height = 3, width = 6,
            bg = "blue", command=lambda: button_click(gameButton10))
gameButton11 = Button(root, text = " ", font = ("Helvitica", 20), height = 3, width = 6,
            bg = "blue", command=lambda: button_click(gameButton11))
#column 2
gameButton12 = Button(root, text = " ", font = ("Helvitica", 20), height = 3, width = 6,
            bg = "blue", command=lambda: button_click(gameButton12))
gameButton13 = Button(root, text = " ", font = ("Helvitica", 20), height = 3, width = 6,
            bg = "blue", command=lambda: button_click(gameButton13))
gameButton14 = Button(root, text = " ", font = ("Helvitica", 20), height = 3, width = 6,
            bg = "blue", command=lambda: button_click(gameButton14))
gameButton15 = Button(root, text = " ", font = ("Helvitica", 20), height = 3, width = 6,
            bg = "blue", command=lambda: button_click(gameButton15))
gameButton16 = Button(root, text = " ", font = ("Helvitica", 20), height = 3, width = 6,
            bg = "blue", command=lambda: button_click(gameButton16))
gameButton17 = Button(root, text = " ", font = ("Helvitica", 20), height = 3, width = 6,
            bg = "red", command=lambda: button_click(gameButton17))
#column 3
gameButton18 = Button(root, text = " ", font = ("Helvitica", 20), height = 3, width = 6,
            bg = "blue", command=lambda: button_click(gameButton18))
gameButton19 = Button(root, text = " ", font = ("Helvitica", 20), height = 3, width = 6,
            bg = "blue", command=lambda: button_click(gameButton19))
gameButton20 = Button(root, text = " ", font = ("Helvitica", 20), height = 3, width = 6,
            bg = "blue", command=lambda: button_click(gameButton20))
gameButton21 = Button(root, text = " ", font = ("Helvitica", 20), height = 3, width = 6,
            bg = "blue", command=lambda: button_click(gameButton21))
gameButton22 = Button(root, text = " ", font = ("Helvitica", 20), height = 3, width = 6,
            bg = "blue", command=lambda: button_click(gameButton22))
gameButton23 = Button(root, text = " ", font = ("Helvitica", 20), height = 3, width = 6,
            bg = "blue", command=lambda: button_click(gameButton23))
#column 4
gameButton24 = Button(root, text = " ", font = ("Helvitica", 20), height = 3, width = 6,
            bg = "blue", command=lambda: button_click(gameButton24))
gameButton25 = Button(root, text = " ", font = ("Helvitica", 20), height = 3, width = 6,
            bg = "blue", command=lambda: button_click(gameButton25))
gameButton26 = Button(root, text = " ", font = ("Helvitica", 20), height = 3, width = 6,
            bg = "blue", command=lambda: button_click(gameButton26))
gameButton27 = Button(root, text = " ", font = ("Helvitica", 20), height = 3, width = 6,
            bg = "blue", command=lambda: button_click(gameButton27))
gameButton28 = Button(root, text = " ", font = ("Helvitica", 20), height = 3, width = 6,
            bg = "blue", command=lambda: button_click(gameButton28))
gameButton29 = Button(root, text = " ", font = ("Helvitica", 20), height = 3, width = 6,
            bg = "blue", command=lambda: button_click(gameButton29))
#column 5
gameButton30 = Button(root, text = " ", font = ("Helvitica", 20), height = 3, width = 6,
            bg = "blue", command=lambda: button_click(gameButton30))
gameButton31 = Button(root, text = " ", font = ("Helvitica", 20), height = 3, width = 6,
            bg = "blue", command=lambda: button_click(gameButton31))
gameButton32 = Button(root, text = " ", font = ("Helvitica", 20), height = 3, width = 6,
            bg = "blue", command=lambda: button_click(gameButton32))
gameButton33 = Button(root, text = " ", font = ("Helvitica", 20), height = 3, width = 6,
            bg = "blue", command=lambda: button_click(gameButton33))
gameButton34 = Button(root, text = " ", font = ("Helvitica", 20), height = 3, width = 6,
            bg = "blue", command=lambda: button_click(gameButton34))
gameButton35 = Button(root, text = " ", font = ("Helvitica", 20), height = 3, width = 6,
            bg = "blue", command=lambda: button_click(gameButton35))


#Assembling the grid for our "S" and "O" tiles
gameButton0.grid(row=0, column=0)
gameButton1.grid(row=1, column=0)
gameButton2.grid(row=2, column=0)
gameButton3.grid(row=3, column=0)
gameButton4.grid(row=4, column=0)
gameButton5.grid(row=5, column=0)

gameButton6.grid(row=0, column=1)
gameButton7.grid(row=1, column=1)
gameButton8.grid(row=2, column=1)
gameButton9.grid(row=3, column=1)
gameButton10.grid(row=4, column=1)
gameButton11.grid(row=5, column=1)

gameButton12.grid(row=0, column=2)
gameButton13.grid(row=1, column=2)
gameButton14.grid(row=2, column=2)
gameButton15.grid(row=3, column=2)
gameButton16.grid(row=4, column=2)
gameButton17.grid(row=5, column=2)

gameButton18.grid(row=0, column=3)
gameButton19.grid(row=1, column=3)
gameButton20.grid(row=2, column=3)
gameButton21.grid(row=3, column=3)
gameButton22.grid(row=4, column=3)
gameButton23.grid(row=5, column=3)

gameButton24.grid(row=0, column=4)
gameButton25.grid(row=1, column=4)
gameButton26.grid(row=2, column=4)
gameButton27.grid(row=3, column=4)
gameButton28.grid(row=4, column=4)
gameButton29.grid(row=5, column=4)

gameButton30.grid(row=0, column=5)
gameButton31.grid(row=1, column=5)
gameButton32.grid(row=2, column=5)
gameButton33.grid(row=3, column=5)
gameButton34.grid(row=4, column=5)
gameButton35.grid(row=5, column=5)

redPlayer.grid(row=6, column = 0)
bluePlayer.grid(row=6, column = 5)
root.mainloop()

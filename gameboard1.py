#Justin Foster
#CS449 - SOS Game

#importing all litileraries required for game
import tkinter
from tkinter import *
import random



def __init__(self, size):
    self.size = size
 
    #need to create a way to make variable board size
    #gameboard = [[" " for x in range(3)] for y in range(3)]

    #Plan to find pathfinding algorithm which supports variable board size
    #and is more versatile than hard code
def pointScored(tile, player):
        


def emptyTile(i, j):
    return gameBoard[i][j] == " "

def fullBoard():
    isEmpty = True
    for i in gameBoard:
        if(i.count(" ") > 0):
            isEmpty = false
    return isEmpty
  
def humanPlay(gameboard, i, j, player1, player2):
    global turn

    if gameBoard[i][j] == " ":
        if turn%2 == 0:
            gameBoard[i][j] = "S"
        else:
            gameBoard[i][j] = "O"

        turn += 1

    if winner(gameBoard, "S"):
        gameboard.destroy()
        winnerDisplay = messagebox.showinfo("Winner! Player 1 Wins!")

    elif winner(gameBoard, "O"):
        gameboard.destroy()
        winnerDisplayer1 = messagebox.showinfo("Winner! Player 2 wins!")


    #def humanGameBoard

mainGame = board(3)


def mainMenu():
    menu = Tk()
    menu.geometry("400x400")
    menu.title("Justin's SOS Game!")

    welcomeScreen = Button(menu, text="Welcome to my SOS Game!",
                           activebackground="red", activeforeground="grey",
                           background="grey", foreground="blue", width = 500, height = 3)

    singlePlayerButton = Button(menu, text="Human Game",
                                activebackground="blue", activeforeground="grey",
                               background="black", foreground="blue", width = 500)

    exitButton = Button(menu, text="Exit Game",
                        activebackground="blue", activeforeground="grey",
                        background="black", foreground="blue", width = 500,
                        command = menu.quit)

    welcomeScreen.pack(side = "top")
    singlePlayerButton.pack(side = "top")
    exitButton.pack(side = "bottom")

    menu.mainloop()

    

    
gameMenu = mainMenu()









    

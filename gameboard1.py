#Justin Foster
#CS449 - SOS Game
#importing all libraries required for game
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.constants import DISABLED, NORMAL
#I learned about partial functions to resolve an issue with positional arguments when launching the game
#https://www.learnpython.org/en/Partial_functions
from functools import partial
from tkinter import messagebox
import unittest

#Initilization of global variables
#Having these global makes scoping much more comprehendable and easier to use
global gameboard
global boardSize
global recurse
playerOneTurn = True
recurse = 0
global p1Score
global p2Score
"""
def getBoardSize():
    global boardSize
    boardSize = 0
    global defaultSize
    defaultSize = 4
    if(boardSize == 0):
        gameboard = [[" " for x in range(defaultSize)] for y in range(defaultSize)]
    else:
        gameboard = [[" " for x in range(boardSize)] for y in range(boardSize)]
"""
boardSize = 3
#Add extra length to board size as easy workaround out of bounds error and doesnt appear in game board
gameboard = [[" " for x in range (boardSize+2)] for y in range(boardSize+2)]

def isBoardFull():
    isEmpty = True
    for i in gameboard:
        if(i.count(" ") > 0):
            isEmpty = False
    return isEmpty

################# ---------------- Simple Game Functions ------------------------ ######################
################# ---------------- Simple Game Functions ------------------------ ######################
################# ---------------- Simple Game Functions ------------------------ ######################

#called by play function to create a new playable board when needed
def newBoardCreate(board, player1, player2):
    global buttonBoard
    buttonBoard = []
    for i in range(boardSize):
        rowCreate = boardSize+i
        buttonBoard.append(i)
        buttonBoard[i] = []
        for j in range(boardSize):
            markButtonPartial = partial(markButton, player1, player2, board, i, j)
            columnCreate = j
            buttonBoard[i].append(j)
            buttonBoard[i][j] = Button(board, height = 5, width = 10, command = markButtonPartial, font=("Arial", "18", "bold"))
            buttonBoard[i][j].grid(row = rowCreate, column = columnCreate)

    board.mainloop()

#Function to check if an SOS has been made by someone
#Make this a pathfinding algorithm - hard coding this is awful
#Recursive flood fill?
def simpleWinner(board, x, y):
    char = "S"
    altChar = "O"

    if ((board[0][0] == char and board[0][1] == altChar and board[0][2] == char) or
            (board[0][2] == char and board[1][2] == altChar and board[2][2] == char) or
            (board[0][0] == char and board[1][1] == altChar and board[2][2] == char) or
            (board[0][2] == char and board[1][1] == altChar and board[2][0] == char) or
            (board[1][0] == char and board[1][1] == altChar and board[1][2] == char) or
            (board[2][0] == char and board[2][1] == altChar and board[2][2] == char) or
            (board[0][0] == char and board[1][0] == altChar and board[2][0] == char) or
            (board[0][1] == char and board[1][1] == altChar and board[2][1] == char)):
        return True

'''
Attempt at recursive board size
    winner = False
    
    topL  = board[ x - 1 ][ y - 1]
    top      = board[ x     ][ y - 1]
    topR = board[ x + 1 ][ y - 1]
    midL  = board[ x - 1 ][ y]
    midR = board[ x + 1 ][ y]
    botL  = board[ x - 1 ][ y + 1 ]
    bot      = board[x][y +1]
    botR = board[ x + 1 ][ y +1]

    if (topL == altChar or top == altChar or topR == altChar or midL == altChar or midR == altChar or botL == altChar
        or bot == altChar or botR == altChar):
        recurse += 1
        winner = True
        if recurse == 2:
            winner = True
            return winner
        simpleWinner(board, char, x, y)
'''      

def createSimpleNewGame(board):
    board.destroy()
    board = Tk()
    board.title("Justin's SOS Game!")
    #exitButton = Button(board, text = "Close Window.", command = board.destroy())
    #Creating buttons to keep track of who's turn it is currently
    player1 = Button(board, text = "Player 1: 'S'", default="active", bg="light grey")
    player2 = Button(board, text = "Player 2: 'O'", default="normal")
    player1.grid(row = 0, column = 0)
    player2.grid(row = 0, column = 2)
    #player1.pack(side = "top")
    #player2.pack(side = "top")
    newBoardCreate(board, player1, player2)

#simple - first sos wins
def markButton(board, player1, player2, i, j):
    global playerOneTurn
    if gameboard[i][j] == ' ':
        if playerOneTurn == True:
            gameboard[i][j] = "S"
            playerOneTurn = False
            #player1.configure(style="white")
        else:
            gameboard[i][j] = "O"
            playerOneTurn = True
        
        #Responsible for marking the board
        buttonBoard[i][j].config(text=gameboard[i][j])

    #Player 1 "S" wins:
    if simpleWinner(gameboard, i, j) == True and (playerOneTurn == False):
        board.destroy()
        winBox = messagebox.showinfo("Player 1 wins!", "Player 1 wins!")
        mainMenu()

    #Player 2 "O" wins:
    elif simpleWinner(gameboard, i , j) == True and (playerOneTurn == True):
        board.destroy()
        winBox = messagebox.showinfo("Player 2 wins!", "Player 2 wins!")
        mainMenu()
    
    #Tie Game
    elif (isBoardFull()):
        winBox = messagebox.showinfo("Draw!", "Draw!")
        mainMenu()

################################## ------ GENERAL GAME FUNCTIONS ----- ##########################################
################################## ------ GENERAL GAME FUNCTIONS ----- ##########################################
################################## ------ GENERAL GAME FUNCTIONS ----- ##########################################
def generalWinner(board, char, x, y):
    char = "S"
    altChar = "O"

    if((board[0][0] == char and board[0][1] == altChar and board[0][2] == char) or
            (board[1][0] == char and board[1][1] == altChar and board[1][2] == char) or
            (board[2][0] == char and board[2][1] == altChar and board[2][2] == char) or
            (board[0][0] == char and board[1][0] == altChar and board[2][0] == char) or
            (board[0][1] == char and board[1][1] == altChar and board[2][1] == char) or
            (board[0][2] == char and board[1][2] == altChar and board[2][2] == char) or
            (board[0][0] == char and board[1][1] == altChar and board[2][2] == char) or
            (board[0][2] == char and board[1][1] == altChar and board[2][0] == char)):
        return True


def newGeneralBoardCreate(board, player1, player2):
    global buttonBoard
    buttonBoard = []
    for i in range(boardSize):
        rowCreate = boardSize+i
        buttonBoard.append(i)
        buttonBoard[i] = []
        for j in range(boardSize):
            #change to general win algorithm
            markButtonPartial = partial(markGeneralButton, player1, player2, board, i, j)
            columnCreate = j
            buttonBoard[i].append(j)
            buttonBoard[i][j] = Button(board, height = 5, width = 10, command = markButtonPartial, font = ("Arial", "18", "bold"))
            buttonBoard[i][j].grid(row = rowCreate, column = columnCreate)
    board.mainloop()
    
def createGeneralNewGame(board):
    board.destroy()
    board = Tk()
    board.title("Justin's SOS Game!")
    #Creating buttons to keep track of who's turn it is currently
    player1 = Button(board, text = "Player 1: 'S'")
    player2 = Button(board, text = "Player 2: 'O'")
    scoreLabel = Label(board, text = "P1 Score: ")
    scoreLabel2 = Label(board, text = "P2 Score: ")
    player1.grid(row = 1, column = 0)
    player2.grid(row = 1, column = 2)
    scoreLabel.grid(row = 0, column = 0)
    scoreLabel2.grid(row = 0, column = 2)
    newGeneralBoardCreate(board, player1, player2)

#General - keep score of every SOS
def markGeneralButton(board, player1, player2, i, j):
    global playerOneTurn
    global p1Score
    global p2Score
    
    if gameboard[i][j] == ' ':
        if playerOneTurn == True:
            gameboard[i][j] = "S"
            playerOneTurn = False
        else:
            gameboard[i][j] = "O"
            playerOneTurn = True

        buttonBoard[i][j].config(text=gameboard[i][j])

   #Player 1 "S" wins:
    if simpleWinner(gameboard, i, j) == True and (playerOneTurn == False):
        p1Score += 1

    #Player 2 "O" wins:
    if simpleWinner(gameboard, i , j) == True and (playerOneTurn == True):
        p2Score += 1
    
    if isBoardFull == True:
        if (p1Score > p2Score):
            winBox = messagebox.showinfo("Winner!", "Player 1 wins!")
        elif (p2Score > p1Score):
            winBox = messagebox.showinfo("Winner!", "Player 2 wins!")
        elif (p1Score == p2Score):
            winBox = messagebox.showinfo("Draw!", "Draw!")
            mainMenu()

def mainMenu():
    menu = Tk()
    menu.geometry("400x400")
    menu.title("Justin's SOS Game!")
    #Partial function is used here to allow the use of createNewGame to be used as a command for
    #single player buttons to take the variables from createNewGame to call newBoardCreate
    #and itiliaze newBoardCreate with those variables, like an __init__ function, sets menu
    #to always be a default parameter in these functions (menu works as "root" in tkinter library)
    playSimpleGame = partial(createSimpleNewGame, menu)
    playGeneralGame = partial(createGeneralNewGame, menu)

    welcomeScreen = Button(menu, text="Welcome to my SOS Game!",
                           activebackground="grey", activeforeground="light grey", bd = 3,
                           background="grey", foreground="blue", width = 500, height = 3, relief = "raised",
                           font = ("Arial", 12))

    singleGeneralButton = Button(menu, text="Human Simple Game", command=playSimpleGame,
                                activebackground="grey", activeforeground="blue", height = 2,
                               background="white", foreground="blue", width = 500, relief = "sunken")

    singleSimpleButton = Button(menu, text="Human General Game", command = playGeneralGame,
                                activebackground="grey", activeforeground="blue", height = 2,
                               background="white", foreground="blue", width = 500, relief = "sunken")

    computerPlayerButton = Button(menu, text="Versus AI Game",
                                activebackground="grey", activeforeground="blue", height = 2,
                               background="white", foreground="blue", width = 500, relief = "sunken")

    exitButton = Button(menu, text="Exit Game",
                        activebackground="grey", activeforeground="white",
                        background="grey", foreground="blue", width = 500,
                        command = menu.destroy)

    welcomeScreen.pack(side = "top")
    singleGeneralButton.pack(side = "top")
    singleSimpleButton.pack(side = "top")
    computerPlayerButton.pack(side = "top")
    exitButton.pack(side = "bottom")

    menu.mainloop()

gameMenu = mainMenu()



####### ---------------------------- TESTING --------------------------------- #######
####### ---------------------------- TESTING --------------------------------- #######
####### ---------------------------- TESTING --------------------------------- #######
# Now in separate file "gameTest.py"







    

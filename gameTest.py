import newGameboard
import unittest

boardSize = 3
gameboard = [[" " for x in range (boardSize)] for y in range(boardSize)]
gameboard1 = [["S" for x in range (boardSize)] for y in range(boardSize)]
gameBoardTrue = [[" " for x in range (boardSize)] for y in range(boardSize)]
gameBoardTrue[0][0] = "S"
gameBoardTrue[0][1] = "O"
gameBoardTrue[0][2] = "S"
gameBoardTrue[1][0] = "O"
gameBoardTrue[2][0] = "S"
player1 = 0
player2 = 0


class testGameboard(unittest.TestCase):

    #Should return false since board is empty
    def testBoardEmpty(self):
        self.assertFalse(newGameboard.isBoardFull())

    #Should return true since board is full
    def testBoardFull(self):
        self.assertFalse(newGameboard.isBoardFull())

    #Testing creating a board
    def testCreateBoard(self):
        self.assertTrue(newGameboard.newBoardCreate(gameboard, player1, player2))

    #Will return false due to there being no winner in this board
    def testWinner(self):
        self.assertFalse(newGameboard.simpleWinner(gameboard, player1, player2))

    #Will return true due to there being a winner
    def testWinnerTrue(self):
        self.assertTrue(newGameboard.simpleWinner(gameBoardTrue, player1, player2))   

    #Will return true if markButton properly creates allows a board to be marked
    def markButtonTrue(self):
        self.assertTrue(newGameboard.markButton(gameboard, player1, player2, x, y))

    def testMenu(self):
        self.assertTrue(newGameboard.mainMenu())
    
    def testNewGame(self):
        self.assertFalse(newGameboard.createSimpleNewGame(gameboard), gameboard)


if __name__ == '__main__':
    unittest.main()

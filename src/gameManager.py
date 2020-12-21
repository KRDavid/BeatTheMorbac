from src import boardManager
from src import playerManager
import random
import os


class Morpion:
    def __init__(self, mode):
        self.Board = boardManager.Board()
        self.first = random.uniform(0,1)
        self.mode = mode

        if self.mode == "pvp":
            self.PlayerX = playerManager.Player("X", self.Board)
            self.PlayerO = playerManager.Player("O", self.Board)  

        if self.mode == "aivai":
            self.PlayerX = playerManager.aiPlayer("X", self.Board)
            self.PlayerO = playerManager.aiPlayer("O", self.Board) 

        if self.mode == "pvai":
            if self.first >= 0.5:
                self.PlayerX = playerManager.Player("X", self.Board)
                self.PlayerO = playerManager.aiPlayer("O", self.Board)
            else:
                self.PlayerX = playerManager.aiPlayer("X", self.Board)
                self.PlayerO = playerManager.Player("O", self.Board)


    def startGame(self):
        os.system('cmd /c "cls"')
        self.printStartingText()

        if self.mode == "pvp":
            self.humanVsHuman()  

        if self.mode == "aivai":
            self.aiVsAi()

        if self.mode == "pvai":
            self.humanVsAi()
        
    


    def humanVsHuman(self):
            self.Board.getBoardState()

            while True:
                self.hudDisplay()
                self.PlayerX.turn()
                if self.Board.isNotOver(self.Board.board):
                    pass
                else:
                    break

                self.hudDisplay()
                self.PlayerO.turn()
                if self.Board.isNotOver(self.Board.board):
                    pass
                else:
                    break

            winner = self.Board.winner(self.Board.board)




    def aiVsAi(self):
        self.Board.getBoardState()

        while True:
            self.hudDisplay()
            self.PlayerX.turn(self.PlayerX.generateAction(self.Board.board, self.PlayerX.player))
            if self.Board.isNotOver(self.Board.board):
                pass
            else:
                break

            self.hudDisplay()
            self.PlayerO.turn(self.PlayerO.generateAction(self.Board.board, self.PlayerO.player))
            if self.Board.isNotOver(self.Board.board):
                pass
            else:
                break

        winner = self.Board.winner(self.Board.board)



        self.Board.getBoardState()

        return winner


    def humanVsAi(self):
        self.Board.getBoardState()

        if self.first >= 0.5:
            while True:
                self.hudDisplay()
                self.PlayerX.turn()
                if self.Board.isNotOver(self.Board.board):
                    pass
                else:
                    break

                self.hudDisplay()
                self.PlayerO.turn(self.PlayerO.generateAction(self.Board.board, self.PlayerO.player))
                if self.Board.isNotOver(self.Board.board):
                    pass
                else:
                    break
        else:
            while True:
                self.hudDisplay()
                self.PlayerX.turn(self.PlayerX.generateAction(self.Board.board, self.PlayerX.player))
                if self.Board.isNotOver(self.Board.board):
                    pass
                else:
                    break

                self.hudDisplay()
                self.PlayerO.turn()
                if self.Board.isNotOver(self.Board.board):
                    pass
                else:
                    break
            

        winner = self.Board.winner(self.Board.board)



        self.Board.getBoardState()

        return winner

    def printStartingText(self):
        print(" ---------------------------------------------")
        print("|                       o                     |")
        print("|     x          x                    x       |")
        print("|                                             |")
        print("|       o      BEAT THE MORBAC           o    |")
        print("|                                             |")
        print("|    o                       x      o         |")
        print("|                 x                           |")
        print(" ---------------------------------------------")

    def hudDisplay(self):
        os.system('cmd /c "cls"')
        self.printStartingText()
        self.Board.getBoardState()
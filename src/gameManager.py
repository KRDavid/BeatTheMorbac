from src import boardManager
from src import playerManager
import random


class Morpion:
    def __init__(self):
        self.Board = boardManager.Board()
        self.first = random.uniform(0,1)
        if self.first >= 0.5:
            self.PlayerX = playerManager.Player("X", self.Board)
            self.PlayerO = playerManager.aiPlayer("O", self.Board)
        else:
            self.PlayerX = playerManager.aiPlayer("X", self.Board)
            self.PlayerO = playerManager.Player("O", self.Board)


    def startGame(self):

        self.Board.getBoardState()

        if self.first >= 0.5:
            while True:
                self.PlayerX.turn()
                if self.Board.isNotOver(self.Board.board):
                    pass
                else:
                    break

                self.PlayerO.turn(self.PlayerO.generateAction(self.Board.board, self.PlayerO.player))
                if self.Board.isNotOver(self.Board.board):
                    pass
                else:
                    break
        else:
            while True:
                self.PlayerX.turn(self.PlayerX.generateAction(self.Board.board, self.PlayerX.player))
                if self.Board.isNotOver(self.Board.board):
                    pass
                else:
                    break

                self.PlayerO.turn()
                if self.Board.isNotOver(self.Board.board):
                    pass
                else:
                    break
            

        winner = self.Board.winner(self.Board.board)



        self.Board.getBoardState()

        return winner



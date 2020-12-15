from src import boardManager
from src import playerManager


class Morpion:
    def __init__(self):
        self.Board = boardManager.Board()
        self.PlayerX = playerManager.aiPlayer("X")
        self.PlayerO = playerManager.aiPlayer("O")


    def startGame(self):
        self.Board.getBoardState()

        while True:
            self.PlayerX.turn(self.Board)
            if self.Board.isNotOver():
                pass
            else:
                break

            self.PlayerO.turn(self.Board)
            if self.Board.isNotOver():
                pass
            else:
                break

        self.Board.winner()
        self.Board.getBoardState()


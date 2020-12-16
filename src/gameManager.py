from src import boardManager
from src import playerManager


class Morpion:
    def __init__(self):
        self.Board = boardManager.Board()
        self.PlayerX = playerManager.aiPlayer("X")
        self.PlayerO = playerManager.aiPlayer("O")


    def startGame(self):
        self.Board.getBoardState()

        rewardX = 0
        rewardO = 0

        while True:
            reward = self.PlayerX.turn(self.Board)
            rewardX += reward
            if self.Board.isNotOver():
                pass
            else:
                break

            reward = self.PlayerO.turn(self.Board)
            rewardO += reward
            if self.Board.isNotOver():
                pass
            else:
                break

        winner = self.Board.winner()
        if winner == "X":
            rewardX += 3
        elif winner == "O":
            rewardO += 3
        elif winner == False:
            rewardX += 1
            rewardO += 1


        self.Board.getBoardState()

        return rewardX, rewardO


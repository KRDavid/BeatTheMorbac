from src import boardManager
from src import playerManager
import pygame


class MorpionMvM:
    def __init__(self):
        self.Board = boardManager.Board()
        self.PlayerX = playerManager.aiPlayer("X")
        self.PlayerO = playerManager.aiPlayer("O")


    def startGame(self):
        # self.Board.getBoardState()

        rewardX = 0
        rewardO = 0

        # self.Board.drawGrid()

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
            pass
        elif winner == "O":
            rewardO += 3
        elif winner == False:
            rewardX += 1
            rewardO += 1


        self.Board.getBoardState()

        return rewardO, rewardX


class MorpionMvH:
    def __init__(self):
        self.Board = boardManager.Board()
        self.PlayerX = playerManager.Player("X")
        self.PlayerO = playerManager.aiPlayer("O")


    def startGame(self):
        self.Board.getBoardState()

        rewardO = 0

        while True:
            reward = self.PlayerX.turn(self.Board)

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
            pass
        elif winner == "O":
            rewardO += 3
        elif winner == False:
            rewardO += 1


        self.Board.getBoardState()

        return rewardO


class MorpionHvH:
    def __init__(self):
        self.Board = boardManager.Board()
        self.PlayerX = playerManager.Player("X")
        self.PlayerO = playerManager.Player("O")


    def startGame(self, fenetre):
        # self.Board.getBoardState()
        self.Board.drawGrid(fenetre)

        while True:
            reward = self.PlayerX.turn(self.Board)

            if self.Board.isNotOver():
                pass
            else:
                break

            reward = self.PlayerO.turn(self.Board)

            if self.Board.isNotOver():
                pass
            else:
                break

        winner = self.Board.winner()


        self.Board.getBoardState()



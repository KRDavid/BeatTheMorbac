"""Fichier principal de l'application
"""

from src import boardManager
from src import turnManager

Board = boardManager.Board()
PlayerX = turnManager.Player("X")
PlayerO = turnManager.Player("O")

Board.getBoardState()

while True:
    PlayerX.turn(Board)
    if Board.isNotOver():
        pass
    else:
        break

    PlayerO.turn(Board)
    if Board.isNotOver():
        pass
    else:
        break

Board.winner()
Board.getBoardState()



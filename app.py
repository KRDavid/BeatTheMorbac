"""Fichier principal de l'application
"""

from src import boardManager
from src import turnManager

Board = boardManager.Board()
Board.getBoardState()

while True:
    turnManager.turn(Board, "X")
    if Board.isNotOver():
        pass
    else:
        break

    turnManager.turn(Board, "O")
    if Board.isNotOver():
        pass
    else:
        break

Board.winner()
Board.getBoardState()
"""Fichier principal de l'application
"""

from src import boardManager
from src import turnManager

Board = boardManager.Board()

while Board.isNotWon:
    turnManager.turn(Board, "X")
    turnManager.turn(Board, "O")

"""Fichier principal de l'application
"""

from src import gameManager
import argparse

parser = argparse.ArgumentParser(description="Venez affronter Morbac ou vos amis !")
parser.add_argument("-m","--mode", help="pvp : Joueur contre joueur, pvai : Joueur contre Morbac, aivai : Morbac contre Morbac")
args = parser.parse_args()

game = gameManager.Morpion(args.mode)

game.startGame()

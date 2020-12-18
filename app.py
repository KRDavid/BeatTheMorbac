"""Fichier principal de l'application
"""

from src import gameManager

choice = 0

choice = input("1. Joueur VS Joueur.\n2. Joueur VS Machine.\n3. Machine VS Machine.\nSélectionnez un mode de jeu :")

if choice == "1": 
    game = gameManager.MorpionHvH()
    game.startGame()
elif choice == "2":
    game = gameManager.MorpionMvH()
    game.startGame()
elif choice == "3" :
    game = gameManager.MorpionMvM()
    game.startGame()
else :
    print("Vous ne savez pas lire, veuillez relancer le jeu.")


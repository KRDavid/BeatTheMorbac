
import os
import pygame

class Board:

    def __init__(self):
        self.board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]


    def checkPlacement(self, x, y):
        return (x in ["1", "2", "3"] and y in ["1","2","3"])
    
    def getMapping(self, x, y):
        x = int(x) - 1
        y = int(y) - 1
        return (x,y)

    def drawGrid(self, fenetre):
        x = 122
        y = 51
        blockSize = 90 #Set the size of the grid block

        for x in range(398):
            for y in range(398):
                rect = pygame.Rect(x*blockSize, y*blockSize,
                                blockSize, blockSize)
                pygame.draw.rect(fenetre, (200, 200, 200), rect, 2)
            
        pygame.display.flip()


    def isNotAlreadyTaken(self, x, y):
        return self.board[y][x] == ' '

    def placeToken(self, x, y, player):
        self.board[y][x] = player
    
    def getBoardState(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('------------------\n')
        print('')
        print("   |   |   ")
        print(" " + self.board[0][0] + " | " + self.board[0][1] + " | " + self.board[0][2] + " ")
        print("   |   |   ")
        print("-----------")
        print("   |   |   ")
        print(" " + self.board[1][0] + " | " + self.board[1][1] + " | " + self.board[1][2] + " ")
        print("   |   |   ")
        print("-----------")
        print("   |   |   ")
        print(" " + self.board[2][0] + " | " + self.board[2][1] + " | " + self.board[2][2] + " ")
        print("   |   |   ")
        print('')
    
    def isNotOver(self):
        notOver = True
        # Verification victoire en ligne
        if self.board[0][0] + self.board[0][1] + self.board[0][2] in ["XXX", "OOO"]:
            notOver = False
        if self.board[1][0] + self.board[1][1] + self.board[1][2] in ["XXX", "OOO"]:
            notOver = False
        if self.board[2][0] + self.board[2][1] + self.board[2][2] in ["XXX", "OOO"]:
            notOver = False

        # Verification victoire en colonne
        if self.board[0][0] + self.board[1][0] + self.board[2][0] in ["XXX", "OOO"]:
            notOver = False
        if self.board[0][1] + self.board[1][1] + self.board[2][1] in ["XXX", "OOO"]:
            notOver = False
        if self.board[0][2] + self.board[1][2] + self.board[2][2] in ["XXX", "OOO"]:
            notOver = False
        # Verification victoire en diagonale
        if self.board[0][0] + self.board[1][1] + self.board[2][2] in ["XXX", "OOO"]:
            notOver = False
        if self.board[0][2] + self.board[1][1] + self.board[2][0] in ["XXX", "OOO"]:
            notOver = False

        # Verification égalité
        if ' ' not in self.board[0] and ' ' not in self.board[1] and ' ' not in self.board[2]:
            notOver = False

        return notOver

    def winner(self):
        gagnant = False
        # Verification victoire en ligne
        if self.board[0][0] + self.board[0][1] + self.board[0][2] in ["XXX", "OOO"]:
            if self.board[0][0] + self.board[0][1] + self.board[0][2] == "XXX":
                gagnant = "X"
            if self.board[0][0] + self.board[0][1] + self.board[0][2] == "OOO":
                gagnant = "O"
            self.board[0][0] = "-"
            self.board[0][1] = "-"
            self.board[0][2] = "-"

        if self.board[1][0] + self.board[1][1] + self.board[1][2] in ["XXX", "OOO"]:
            if self.board[1][0] + self.board[1][1] + self.board[1][2] == "XXX":
                gagnant = "X"
            if self.board[1][0] + self.board[1][1] + self.board[1][2] == "OOO":
                gagnant = "O"
            self.board[1][0] = "-"
            self.board[1][1] = "-"
            self.board[1][2] = "-"

        if self.board[2][0] + self.board[2][1] + self.board[2][2] in ["XXX", "OOO"]:
            if self.board[2][0] + self.board[2][1] + self.board[2][2] == "XXX":
                gagnant = "X"
            if self.board[2][0] + self.board[2][1] + self.board[2][2] == "OOO":
                gagnant = "O"
            self.board[2][0] = "-"
            self.board[2][1] = "-"
            self.board[2][2] = "-"

        # Verification victoire en colonne
        if self.board[0][0] + self.board[1][0] + self.board[2][0] in ["XXX", "OOO"]:
            if self.board[0][0] + self.board[1][0] + self.board[2][0] == "XXX":
                gagnant = "X"
            if self.board[0][0] + self.board[0][1] + self.board[0][2] == "OOO":
                gagnant = "O"
            self.board[0][0] = "|"
            self.board[1][0] = "|"
            self.board[2][0] = "|"

        if self.board[0][1] + self.board[1][1] + self.board[2][1] in ["XXX", "OOO"]:
            if self.board[0][1] + self.board[1][1] + self.board[2][1] == "XXX":
                gagnant = "X"
            if self.board[0][1] + self.board[1][1] + self.board[2][1] == "OOO":
                gagnant = "O"
            self.board[0][1] = "|"
            self.board[1][1] = "|"
            self.board[2][1] = "|"

        if self.board[0][2] + self.board[1][2] + self.board[2][2] in ["XXX", "OOO"]:
            if self.board[0][2] + self.board[1][2] + self.board[2][2] == "XXX":
                gagnant = "X"
            if self.board[0][2] + self.board[1][2] + self.board[2][2] == "OOO":
                gagnant = "O"
            self.board[0][2] = "|"
            self.board[1][2] = "|"
            self.board[2][2] = "|"

        # Verification victoire en diagonale
        if self.board[0][0] + self.board[1][1] + self.board[2][2] in ["XXX", "OOO"]:
            if self.board[0][0] + self.board[1][1] + self.board[2][2] == "XXX":
                gagnant = "X"
            if self.board[0][0] + self.board[1][1] + self.board[2][2] == "OOO":
                gagnant = "O"
            self.board[0][0] = "\\"
            self.board[1][1] = "\\"
            self.board[2][2] = "\\"

        if self.board[0][2] + self.board[1][1] + self.board[2][0] in ["XXX", "OOO"]:
            if self.board[0][2] + self.board[1][1] + self.board[2][0] == "XXX":
                gagnant = "X"
            if self.board[0][2] + self.board[1][1] + self.board[2][0] == "OOO":
                gagnant = "O"
            self.board[0][2] = "/"
            self.board[1][1] = "/"
            self.board[2][0] = "/"
        if gagnant != False :
            print(f"Félicitations ! Le joueur {gagnant} remporte la partie !!")
        else :
            print("Dommage.. C'est une égalité..")

        return gagnant


    

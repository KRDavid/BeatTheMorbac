
class Board:

    def __init__(self):
        self.board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]


    def checkPlacement(self, x, y):
        return (x in ["1", "2", "3"] and y in ["1","2","3"])
    
    def getMapping(self, x, y):
        x = int(x) - 1
        y = int(y) - 1
        return (x,y)

    def isNotAlreadyTaken(self, x, y):
        return self.board[y][x] == ' '

    def placeToken(self, x, y, player):
        self.board[y][x] = player


    def getBoardState(self):
        print('')
        print("                    |   |   ")
        print("                  " + self.board[0][0] + " | " + self.board[0][1] + " | " + self.board[0][2] + " ")
        print("                    |   |   ")
        print("                 -----------")
        print("                    |   |   ")
        print("                  " + self.board[1][0] + " | " + self.board[1][1] + " | " + self.board[1][2] + " ")
        print("                    |   |   ")
        print("                 -----------")
        print("                    |   |   ")
        print("                  " + self.board[2][0] + " | " + self.board[2][1] + " | " + self.board[2][2] + " ")
        print("                    |   |   ")
        print('')
    
    def isNotOver(self, board):
        notOver = True
        # Verification victoire en ligne
        for i in range(3):
            if board[i][0] + board[i][1] + board[i][2] in ["XXX", "OOO"]:
                notOver = False

        # Verification victoire en colonne
        for i in range(3):
            if board[0][i] + board[1][i] + board[2][i] in ["XXX", "OOO"]:
                notOver = False
            
        # Verification victoire en diagonale
        if board[0][0] + board[1][1] + board[2][2] in ["XXX", "OOO"]:
            notOver = False
        if board[0][2] + board[1][1] + board[2][0] in ["XXX", "OOO"]:
            notOver = False

        # Verification égalité
        if ' ' not in board[0] and ' ' not in board[1] and ' ' not in board[2]:
            notOver = False

        return notOver

    def winner(self, board):
        gagnant = False

        for i in range(3):
            # Verification victoire en ligne
            if board[i][0] + board[i][1] + board[i][2] in ["XXX", "OOO"]:
                if board[i][0] + board[i][1] + board[i][2] == "XXX":
                    gagnant = "X"
                if board[i][0] + board[i][1] + board[i][2] == "OOO":
                    gagnant = "O"
                board[i][0] = "-"
                board[i][1] = "-"
                board[i][2] = "-"


        for i in range(3):
            # Verification victoire en colonne
            if board[0][i] + board[1][i] + board[2][i] in ["XXX", "OOO"]:
                if board[0][i] + board[1][i] + board[2][i] == "XXX":
                    gagnant = "X"
                if board[0][i] + board[1][i] + board[2][i] == "OOO":
                    gagnant = "O"
                board[0][i] = "|"
                board[1][i] = "|"
                board[2][i] = "|"

        
        # Verification victoire en diagonale
        if board[0][0] + board[1][1] + board[2][2] in ["XXX", "OOO"]:
            if board[0][0] + board[1][1] + board[2][2] == "XXX":
                gagnant = "X"
            if board[0][0] + board[1][1] + board[2][2] == "OOO":
                gagnant = "O"
            board[0][0] = "\\"
            board[1][1] = "\\"
            board[2][2] = "\\"

        if board[0][2] + board[1][1] + board[2][0] in ["XXX", "OOO"]:
            if board[0][2] + board[1][1] + board[2][0] == "XXX":
                gagnant = "X"
            if board[0][2] + board[1][1] + board[2][0] == "OOO":
                gagnant = "O"
            board[0][2] = "/"
            board[1][1] = "/"
            board[2][0] = "/"
        if gagnant != False :
            print(f"Félicitations ! Le joueur {gagnant} remporte la partie !!")
        else :
            print("Dommage.. C'est une égalité..")

        return gagnant

    


class Board:

    def __init__(self):
        self.board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

    def checkPlacement(self, placement):
        return placement in ["1","2","3","4","5","6","7","8","9"]

    def getMapping(self, placement):
        if placement == "1" :
            y = 0
            x = 0
        if placement == "2" :
            y = 0
            x = 1
        if placement == "3" :
            y = 0
            x = 2
        if placement == "4" :
            y = 1
            x = 0
        if placement == "5" :
            y = 1
            x = 1
        if placement == "6" :
            y = 1
            x = 2
        if placement == "7" :
            y = 2
            x = 0
        if placement == "8" :
            y = 2
            x = 1
        if placement == "9" :
            y = 2
            x = 2
        return (x,y)

    def isNotAlreadyTaken(self, x, y):
        return self.board[y][x] == ' '

    def placeToken(self, x, y, player):
        self.board[y][x] = player
    
    def getBoardState(self):
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
        
    def isNotWon():
        return False

    

from math import inf as infinity

class Player:
    def __init__(self, player, board):
        self.player = player
        self.Board = board

    def turn(self):

        valid_placement = False
        x = str(input(f"Joueur {self.player}, choisissez votre colonne (1 à 3) : "))
        y = str(input(f"Joueur {self.player}, choisissez votre ligne (1 à 3) : "))
        if self.Board.checkPlacement(x, y):
            x, y = self.Board.getMapping(x, y)
            if self.Board.isNotAlreadyTaken(x, y):
                self.Board.placeToken(x, y, self.player)
            else:
                while valid_placement == False:
                    print("Placement invalide")
                    x = str(input(f"Joueur {self.player}, choisissez votre colonne (1 à 3) : "))
                    y = str(input(f"Joueur {self.player}, choisissez votre ligne (1 à 3) : "))
                    if self.Board.checkPlacement(x, y):
                        x, y = self.Board.getMapping(x, y)
                        if self.Board.isNotAlreadyTaken(x, y):
                            self.Board.placeToken(x, y, self.player)
                            valid_placement = True
        else:
            while valid_placement == False:
                print("Placement invalide")
                x = str(input(f"Joueur {self.player}, choisissez votre colonne (1 à 3) : "))
                y = str(input(f"Joueur {self.player}, choisissez votre ligne (1 à 3) : "))
                if self.Board.checkPlacement(x, y):
                    x, y = self.Board.getMapping(x, y)
                    if self.Board.isNotAlreadyTaken(x, y):
                        self.Board.placeToken(x, y, self.player)
                        valid_placement = True
                else:
                    while valid_placement == False:
                        print("Placement invalide")
                        x = str(input(f"Joueur {self.player}, choisissez votre colonne (1 à 3) : "))
                        y = str(input(f"Joueur {self.player}, choisissez votre ligne (1 à 3) : "))
                        if self.Board.checkPlacement(x, y):
                            x, y = self.Board.getMapping(x, y)
                            if self.Board.isNotAlreadyTaken(x, y):
                                self.Board.placeToken(x, y, self.player)
                                valid_placement = True


class aiPlayer:
    def __init__(self, player, board):
        self.player = player
        self.Board = board
        self.actionSpace = {1: (0,0), 2: (0,1), 3: (0,2), 4: (1,0), 5: (1,1), 6: (1,2), 7: (2,0), 8: (2,1), 9: (2,2)}

    def tryMove(self, boardCopy, player, x, y):
        boardCopy[y][x] = player
        return boardCopy

    def getBoardCopy(self, state):
        new_state = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        for i in range(3):
            for j in range(3):
                new_state[i][j] = state[i][j]
        return new_state


    def generateAction(self, state, player):
        winner = self.getWinner(state)
        if self.Board.isNotOver(state):
            pass
        else:
            if winner == self.player:
                return 1
            if winner != False and winner != self.player:
                return -1
            if winner == False:
                return 0


        moves = []
        empty_cells = []
        for i in range(3):
            for j in range(3):
                if state[i][j] == ' ':
                    empty_cells.append(i*3 + (j+1))
        for empty_cell in empty_cells:
            move = {}
            move['index'] = empty_cell
            y, x = self.actionSpace[empty_cell]
            new_state = self.getBoardCopy(state)
            new_state = self.tryMove(new_state, player, x, y)
            
            if player == 'O':
                result = self.generateAction(new_state, 'X')
                move['score'] = result
            else:
                result = self.generateAction(new_state, 'O')
                move['score'] = result

            moves.append(move)
        
        best_move = None
        if player == self.player:   # If AI player
            best = -infinity
            for move in moves:
                if move['score'] > best:
                    best = move['score']
                    best_move = move['index']
        else:
            best = infinity
            for move in moves:
                if move['score'] < best:
                    best = move['score']
                    best_move = move['index']

        return best_move

    def turn(self, action):
        print('Morbac réfléchit ...')
        # Gérérer une action
        y, x = self.actionSpace[action]
    
        self.Board.placeToken(x, y, self.player)

    def getWinner(self, board):
        gagnant = False
        for i in range(3):
            # Verification victoire en ligne
            if board[i][0] + board[i][1] + board[i][2] in ["XXX", "OOO"]:
                if board[i][0] + board[i][1] + board[i][2] == "XXX":
                    gagnant = "X"
                if board[i][0] + board[i][1] + board[i][2] == "OOO":
                    gagnant = "O"


        for i in range(3):
            # Verification victoire en colonne
            if board[0][i] + board[1][i] + board[2][i] in ["XXX", "OOO"]:
                if board[0][i] + board[1][i] + board[2][i] == "XXX":
                    gagnant = "X"
                if board[0][i] + board[1][i] + board[2][i] == "OOO":
                    gagnant = "O"

        
        # Verification victoire en diagonale
        if board[0][0] + board[1][1] + board[2][2] in ["XXX", "OOO"]:
            if board[0][0] + board[1][1] + board[2][2] == "XXX":
                gagnant = "X"
            if board[0][0] + board[1][1] + board[2][2] == "OOO":
                gagnant = "O"

        if board[0][2] + board[1][1] + board[2][0] in ["XXX", "OOO"]:
            if board[0][2] + board[1][1] + board[2][0] == "XXX":
                gagnant = "X"
            if board[0][2] + board[1][1] + board[2][0] == "OOO":
                gagnant = "O"

        return gagnant
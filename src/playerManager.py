import random

class Player:
    def __init__(self, player):
        self.player = player

    def turn(self, Board):

        valid_placement = False
        x = str(input(f"Joueur {self.player}, choisissez votre colonne (1 à 3) : "))
        y = str(input(f"Joueur {self.player}, choisissez votre ligne (1 à 3) : "))
        if Board.checkPlacement(x, y):
            x, y = Board.getMapping(x, y)
            if Board.isNotAlreadyTaken(x, y):
                Board.placeToken(x, y, self.player)
            else:
                while valid_placement == False:
                    print("Placement invalide")
                    x = str(input(f"Joueur {self.player}, choisissez votre colonne (1 à 3) : "))
                    y = str(input(f"Joueur {self.player}, choisissez votre ligne (1 à 3) : "))
                    if Board.checkPlacement(x, y):
                        x, y = Board.getMapping(x, y)
                        if Board.isNotAlreadyTaken(x, y):
                            Board.placeToken(x, y, self.player)
                            valid_placement = True
        else:
            while valid_placement == False:
                print("Placement invalide")
                x = str(input(f"Joueur {self.player}, choisissez votre colonne (1 à 3) : "))
                y = str(input(f"Joueur {self.player}, choisissez votre ligne (1 à 3) : "))
                if Board.checkPlacement(x, y):
                    x, y = Board.getMapping(x, y)
                    if Board.isNotAlreadyTaken(x, y):
                        Board.placeToken(x, y, self.player)
                else:
                    while valid_placement == False:
                        print("Placement invalide")
                        x = str(input(f"Joueur {self.player}, choisissez votre colonne (1 à 3) : "))
                        y = str(input(f"Joueur {self.player}, choisissez votre ligne (1 à 3) : "))
                        if Board.checkPlacement(x, y):
                            x, y = Board.getMapping(x, y)
                            if Board.isNotAlreadyTaken(x, y):
                                Board.placeToken(x, y, self.player)
                                valid_placement = True
        Board.getBoardState()


class aiPlayer:
    def __init__(self, player):
        self.player = player
        self.actionSpace = {1: (0,0), 2: (0,1), 3: (0,2), 4: (1,0), 5: (1,1), 6: (1,2), 7: (2,0), 8: (2,1), 9: (2,2)}
        self.possibleActions = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def generateAction(self):
        choseAction = random.choice(self.possibleActions)
        x, y = self.actionSpace[choseAction]
        return (x,y)

    def turn(self, Board):
        reward = 0

        valid_placement = False
        # Gérérer une action
        x, y = self.generateAction()
        if Board.isNotAlreadyTaken(x, y):
            Board.placeToken(x, y, self.player)
            reward += .25
        else:
            reward -= 1
            while valid_placement == False:
                # Gérérer une action
                x, y = self.generateAction()
                if Board.isNotAlreadyTaken(x, y):
                    Board.placeToken(x, y, self.player)
                    valid_placement = True
                    reward += .25
                else:
                    reward -= 1
        
        Board.getBoardState()
        return reward

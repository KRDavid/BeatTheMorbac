from src import boardManager

def turn(Board, player):

    valid_placement = False
    x = str(input(f"Joueur {player}, choisissez votre colonne (1 à 3) : "))
    y = str(input(f"Joueur {player}, choisissez votre ligne (1 à 3) : "))
    if Board.checkPlacement(x, y):
        x, y = Board.getMapping(x, y)
        if Board.isNotAlreadyTaken(x, y):
            Board.placeToken(x, y, player)
        else:
            while valid_placement == False:
                print("Placement invalide")
                x = str(input(f"Joueur {player}, choisissez votre colonne (1 à 3) : "))
                y = str(input(f"Joueur {player}, choisissez votre ligne (1 à 3) : "))
                if Board.checkPlacement(x, y):
                    x, y = Board.getMapping(x, y)
                    if Board.isNotAlreadyTaken(x, y):
                        Board.placeToken(x, y, player)
                        valid_placement = True
    else:
        while valid_placement == False:
            print("Placement invalide")
            x = str(input(f"Joueur {player}, choisissez votre colonne (1 à 3) : "))
            y = str(input(f"Joueur {player}, choisissez votre ligne (1 à 3) : "))
            if Board.checkPlacement(x, y):
                x, y = Board.getMapping(x, y)
                if Board.isNotAlreadyTaken(x, y):
                    Board.placeToken(x, y, player)
            else:
                while valid_placement == False:
                    print("Placement invalide")
                    x = str(input(f"Joueur {player}, choisissez votre colonne (1 à 3) : "))
                    y = str(input(f"Joueur {player}, choisissez votre ligne (1 à 3) : "))
                    if Board.checkPlacement(x, y):
                        x, y = Board.getMapping(x, y)
                        if Board.isNotAlreadyTaken(x, y):
                            Board.placeToken(x, y, player)
                            valid_placement = True
    Board.getBoardState()




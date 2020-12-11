from src import boardManager

def turn(Board, player):

    valid_placement = False
    Board.getBoardState()
    placement = str(input("Choisissez votre emplacement (entre 1 et 9) : "))
    if Board.checkPlacement(placement):
        x, y = Board.getMapping(placement)
        if Board.isNotAlreadyTaken(x, y):
            Board.placeToken(x, y, player)
        else:
            while valid_placement == False:
                placement = str(input("Placement invalide, veuillez choisir un nouveau placement (entre 1 et 9) : "))
                if Board.checkPlacement(placement):
                    x, y = Board.getMapping(placement)
                    if Board.isNotAlreadyTaken(x, y):
                        Board.placeToken(x, y, player)
                        valid_placement = True
    else:
        while valid_placement == False:
            placement = str(input("Placement invalide, veuillez choisir un nouveau placement (entre 1 et 9) : "))
            if Board.checkPlacement(placement):
                x, y = Board.getMapping(placement)
                if Board.isNotAlreadyTaken(x, y):
                    Board.placeToken(x, y, player)
            else:
                while valid_placement == False:
                    placement = str(input("Placement invalide, veuillez choisir un nouveau placement (entre 1 et 9) : "))
                    if Board.checkPlacement(placement):
                        x, y = Board.getMapping(placement)
                        if Board.isNotAlreadyTaken(x, y):
                            Board.placeToken(x, y, player)
                            valid_placement = True




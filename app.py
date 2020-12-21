import pygame
from pygame.locals import *

from src import gameManager


    
#Initialisation de la bibliothèque Pygame
pygame.init()

#Fenêtre du jeu
fenetre = pygame.display.set_mode((640, 480))

#Fond de l'appli
# fond = pygame.image.load("src/img/fond.png")
# fenetre.blit(fond, (0,0))

#Icone
icone = pygame.image.load("src/img/icon.png")
pygame.display.set_icon(icone)

#Titre
pygame.display.set_caption("Beat The Morbac : le jeu !")

#Music
pygame.mixer.music.load('src/music/wham.mp3')
pygame.mixer.music.play(-1)

#Actualisation de l'écran
pygame.display.flip()

#Boucle de jeu
continuer = 1 #Continue le jeu à 1, le stoppe à 0

while continuer:    
    #Chargement et affichage de l'écran d'accueil
    accueil = pygame.image.load("src/img/accueil.gif").convert()
    fenetre.blit(accueil, (0,0))

    #Rafraichissement
    pygame.display.flip()

    #On remet ces variables à 1 à chaque tour de boucle
    continuer_jeu = 1
    continuer_accueil = 1

    #BOUCLE D'ACCUEIL
    while continuer_accueil:
    
        #Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)
        fenetre.blit(accueil, (0,0))

        #Rafraichissement
        pygame.display.flip()
    
        for event in pygame.event.get():
        
            #Si l'utilisateur quitte, on met les variables 
            #de boucle à 0 pour n'en parcourir aucune et fermer
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer_accueil = 0
                continuer_jeu = 0
                continuer = 0

                #Variable de choix du module
                choix = 'none'
                
            elif event.type == KEYDOWN:                
                #Joueur VS Joueur
                if event.key == K_F1:
                    continuer_accueil = 0    #On quitte l'accueil
                    choix = 'JCJ'
                #Joueur VS Morbac
                elif event.key == K_F2:
                    continuer_accueil = 0
                    choix = 'JCM'
                #Morbac VS Morbac
                elif event.key == K_F3:
                    continuer_accueil = 0
                    choix = 'MCM'

    #on vérifie que le joueur a bien fait un choix de niveau
    if choix != 'none':
        #Chargement du fond
        fond = pygame.image.load('src/img/fond.png').convert()
        fenetre.blit(fond, (0,0))

        #Rafraichissement
        pygame.display.flip()

        if choix == 'JCJ':

            game = gameManager.MorpionHvH()
            game.startGame(fenetre)

        # elif choix == 'JCM':
        #     game = gameManager.MorpionMvH()
        #     game.startGame()

        # elif choix == 'MCM':
        #     game = gameManager.MorpionMvM()
        #     game.startGame()

                
    #BOUCLE DE JEU
    while continuer_jeu:
    
        #Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)
    
        for event in pygame.event.get():
        
            #Si l'utilisateur quitte, on met la variable qui continue le jeu
            #ET la variable générale à 0 pour fermer la fenêtre
            if event.type == QUIT:
                continuer_jeu = 0
                continuer = 0
        
            elif event.type == KEYDOWN:
                #Si l'utilisateur presse Echap ici, on revient seulement au menu
                if event.key == K_ESCAPE:
                    continuer_jeu = 0
                    
            
        #Affichages aux nouvelles positions
        fenetre.blit(fond, (0,0))


        # niveau.afficher(fenetre)
        # fenetre.blit(dk.direction, (dk.x, dk.y)) #dk.direction = l'image dans la bonne direction
        # pygame.display.flip()




#Choix du module de jeu
# choice = 0
# choice = input("1. Joueur VS Joueur.\n2. Joueur VS Machine.\n3. Machine VS Machine.\nSélectionnez un mode de jeu :")

# if choice == "1": 
#     game = gameManager.MorpionHvH()
#     game.startGame()
# elif choice == "2":
#     game = gameManager.MorpionMvH()
#     game.startGame()
# elif choice == "3" :
#     game = gameManager.MorpionMvM()
#     game.startGame()
# else :
#     print("Vous ne savez pas lire, veuillez relancer le jeu.")




#Boucle infinie
while continuer:
    for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
        if event.type == QUIT:     #Si un de ces événements est de type QUIT
            continuer = 0 










# if self.grille[y][x] == 'X':
#                     pygame.draw.line(self.ecran,self.X_color,(x*200, y*200),(200 + (x*200), 200 + (y*200)), 10)
#                     pygame.draw.line(self.ecran,self.X_color,((x*200), 200 + (y*200)),(200 + (x*200), (y*200)), 10)
#                 elif self.grille[y][x] == 'O':
                    
# pygame.draw.circle
# (self.ecran,self.O_color,(100 + (x*200), 100 + (y*200)),180, 10)

# self.lignes = [ ((200,0),(200,200)),
#                         ((400,0),(400,400)),
#                         ((0,200),(600,200)),
#                         ((0,400),(600,400))]

# for ligne in self.lignes :
#     pygame.draw.line(self.ecran,self.grille_color,ligne[0],ligne[1],3)

# position_x, position_y = position[0]//200, position[1]//200
#         case = [position_x,position_y]
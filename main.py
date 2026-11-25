import pygame
from jeu import Jeu
from enquette import Enquette

import pygame

pygame.init()

#variables 
largeur = 1024
hauteur = 704  
#couleur = (110, 40, 40) # couleur je sais pas quoi mettre
police = pygame.font.SysFont(None , 40) #police

# taille de l'écran
ecran = pygame.display.set_mode((largeur, hauteur))  


# l'iamge de font du jeu
image_fond = pygame.image.load("images/menu.png").convert()
image_fond = pygame.transform.scale(image_fond, (largeur, hauteur)) # image prend la taille de l'écran



# les buttons du menu
largeur_button = 250
hauteur_button = 60
x=(largeur - largeur_button) // 2
y=330

button1 = pygame.Rect(x, y, largeur_button, hauteur_button)
button2 = pygame.Rect(x, y + hauteur_button + 20, largeur_button, hauteur_button)




running = True

while running:

    #position du souris
    position_du_souris = pygame.mouse.get_pos() 
    if button1.collidepoint(position_du_souris):
        couleur = (150, 50, 50) # couleur du button quand la souris est dessus
    else:
        couleur = (110, 40, 40) # couleur du button quand la souris est pas dessus
    if button2.collidepoint(position_du_souris):
        couleur2 = (150, 50, 50) # couleur du button quand la souris est dessus
    else:
        couleur2 = (110, 40, 40) # couleur du button quand la souris est pas dessus

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button1.collidepoint(event.pos):
                print("Jouer")
            elif button2.collidepoint(event.pos):
                print("Quitter")
                running = False    
    ecran.blit(image_fond, (0, 0)) #affiche

     # dessiner les buttons
    pygame.draw.rect(ecran,couleur,button1,border_radius = 8)  
    pygame.draw.rect(ecran,couleur2,button2,border_radius = 8)

    # les textes des buttons
    surface_jouer = police.render("Jouer", True, (255, 255, 255))
    rect_jouer = surface_jouer.get_rect(center=button1.center)
    ecran.blit(surface_jouer, rect_jouer)

    surface_quitter = police.render("Quitter", True, (255, 255, 255))
    rect_quitter = surface_quitter.get_rect(center=button2.center)
    ecran.blit(surface_quitter, rect_quitter)

    pygame.display.flip()#rafraichis l'ecran
         

pygame.quit()
      

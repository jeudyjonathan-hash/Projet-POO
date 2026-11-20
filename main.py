import pygame
from jeu import Jeu
from enquette import Enquette

pygame.init()

pygame.display.set_mode((500,300))

running = True

while running:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()

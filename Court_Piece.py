import pygame
from pygame.locals import *

pygame.init()
 
game_display = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Piece Court (حکم)")
def event_handler():
    for event in pygame.event.get():
       if event.type == QUIT or ( 
            event.type == KEYDOWN and (
              event.key == K_ESCAPE or
              event.key == K_q
            )):
            pygame.quit()
            quit()

 
while True:
    event_handler()
 
    pygame.display.update()
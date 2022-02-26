import pygame
import sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((500, 500))

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.draw.rect(screen, (255, 0, 0), (10, 10, 100, 100))
    pygame.display.update()
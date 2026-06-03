import pygame

width, height = 800, 800
rows, cols = 8,8
square_size = width//cols 

red = (255,0,0)
white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
LIGHT_BROWN = (240, 217, 181)
DARK_BROWN  = (181, 136, 99)

CREAM = (255, 248, 220)
DARK = (60, 42, 33)
OUTLINE = (128, 96, 72)
RED = (170, 60, 50)
GOLD = (212, 175, 55)

crown = pygame.transform.scale(pygame.image.load('crown.png'), (44,25))

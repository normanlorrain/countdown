# Put text on a PyGame screen

from enum import auto

import pygame

from countdown import config

font = {}

NORMAL = auto()
HEADING = auto()
GREEN = (46, 176, 80)
RED = (163, 48, 42)
BLUE = (0, 173, 240)

def init():
    pygame.font.init()
    font[NORMAL] = pygame.font.SysFont(config.typeface, config.size)
    
    

def createMessage(msg, style=NORMAL, colour=BLUE):
    textSurface = font[style].render(msg, True, colour)
    return textSurface

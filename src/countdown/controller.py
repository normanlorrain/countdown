# Ye Olde Controller
# The ringmaster

import os
from enum import auto
import pygame
from datetime import datetime


from countdown import screen
from countdown import text
from countdown import config
from countdown import log
from countdown import signal


os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"  # suppresses Pygame message on import

DOOMSDAY = datetime(2025, 4, 28, 0, 0, 0)  # YYYY, MM, DD, HH, MM, SS

CLOCK_EVENT = pygame.event.custom_type()
CLOCK_INTERVAL = None

pauseState = False
showYearState = False

NEXT = auto()
PREVIOUS = auto()


def init():

    screen.init()  # Needs to be before the rest, so Pygame gets initalized.
    text.init()
    signal.init()
    global CLOCK_INTERVAL
    CLOCK_INTERVAL =  1000  # msec
    pygame.key.set_repeat(1000, 100)


def refreshScreen(direction=NEXT):
    # Blank the screen
    screen.displaySurface.fill((0, 0, 0))
  
    td = DOOMSDAY - datetime.now()
    days = td.days
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    pad = 10
    message = text.createMessage(f"{days:02d}:{hours:02d}:{minutes:02d}:{seconds:02d}")
    width = message.get_width()
    height = message.get_height()   
    x = screen.WIDTH // 2 - width // 2
    y = screen.HEIGHT // 2 - height // 2
    screen.displaySurface.blit(message, (x, y))

    pygame.display.flip()





def run() -> bool:
    global pauseState
    global showYearState

    refreshScreen()

    # Creates a periodically repeating event on the event queue
    pygame.time.set_timer(CLOCK_EVENT, CLOCK_INTERVAL)
    while True:
        event = pygame.event.wait()
        if event.type == pygame.NOEVENT:
            continue
        log.debug(f"{event}")  # Noisy, e.g. mouse movements
        if event.type == CLOCK_EVENT:
            refreshScreen()
            pygame.time.set_timer(CLOCK_EVENT, CLOCK_INTERVAL)

        if event.type in [pygame.WINDOWCLOSE, pygame.QUIT]:
            log.debug(f"{event}")
            return False
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_q]:
                log.debug(f"{event}")
                return False

            pygame.event.clear(eventtype=[pygame.KEYDOWN, pygame.KEYUP])




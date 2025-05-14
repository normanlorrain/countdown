# An interface layer for Pygames management of the window/screen.

import pygame
from countdown import config, screen
from countdown import log

WIDTH, HEIGHT = (1280, 720)

MSG_DEST = (0,0) # coordinates of the message destination 

# Since the configuration isn't initialized yet, we need to explicitly
# initialize here.
def init():
    global displaySurface
    global WIDTH, HEIGHT

    # pygame setup
    pygame.init()
    pygame.mixer.quit()  # Don't need
    pygame.joystick.quit()  # Don't need

    log.debug(f"Support for all image formats: {pygame.image.get_extended()}")
    if config.fullscreen:
        displaySurface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    else:
        displaySurface = pygame.display.set_mode((WIDTH, HEIGHT))

    WIDTH, HEIGHT = displaySurface.get_size()
    log.info(f"Screen size {WIDTH} x {HEIGHT}")

    pygame.mouse.set_visible(False)


def rect():
    return pygame.Rect(0, 0, WIDTH, HEIGHT)


def get_destination(message):
    global MSG_DEST
    width = message.get_width()
    height = message.get_height()
    x = screen.WIDTH // 2 - width // 2
    y = screen.HEIGHT // 2 - height // 2
    MSG_DEST = (x, y)
    return MSG_DEST

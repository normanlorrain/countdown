# An interface the the OS signal API, so we can accept SIGURS1 signals.

import signal
import os

import pygame
from countdown import log

SIGUSR1_EVENT = pygame.event.custom_type()


def handler(signum, _):
    log.info(f"Signal handler called with signal {signum}")
    pygame.event.post(pygame.event.Event(SIGUSR1_EVENT))


def init():
    pass
import pygame
from pygame.locals import *

class PaintWindow:
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title

    def create_window(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

    def update_window(self):
        pygame.display.flip()

    def close_window(self):
        pygame.quit()

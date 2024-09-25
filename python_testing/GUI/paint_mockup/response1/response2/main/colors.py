import pygame

class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def get_pygame_color(self):
        return pygame.Color(self.r, self.g, self.b)

class ColorPalette:
    def __init__(self):
        self.colors = [
            Color(255, 0, 0),  # Red
            Color(0, 255, 0),  # Green
            Color(0, 0, 255),  # Blue
            Color(255, 255, 0),  # Yellow
            Color(0, 255, 255),  # Cyan
            Color(255, 0, 255),  # Magenta
            Color(255, 255, 255),  # White
        ]

    def get_color(self, index):
        return self.colors[index]

    def get_color_count(self):
        return len(self.colors)

import pygame

class ColorPalette:
    def __init__(self, window):
        self.window = window
        self.colors = [
            (255, 0, 0),  # Red
            (0, 255, 0),  # Green
            (0, 0, 255),  # Blue
            (255, 255, 0),  # Yellow
            (0, 255, 255),  # Cyan
            (255, 0, 255),  # Magenta
            (255, 255, 255),  # White
        ]

    def draw(self):
        for i, color in enumerate(self.colors):
            pygame.draw.rect(self.window.screen, color, (10 + (i * 30), 10, 20, 20))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if 10 <= event.pos[0] <= 240 and 10 <= event.pos[1] <= 30:
                    color_index = (event.pos[0] - 10) // 30
                    self.window.painter.fill(color_index)

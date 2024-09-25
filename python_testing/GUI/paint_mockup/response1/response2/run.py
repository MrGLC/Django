import pygame
from main.paint_window import PaintWindow
from main.painter import Painter
from main.colors import ColorPalette
from main.palette import ColorPalette as Palette
from main.settings import Settings

pygame.init()

window = PaintWindow(Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT, Settings.WINDOW_TITLE)
window.create_window()

palette = Palette(window)
painter = Painter(window, ColorPalette())

running = True
while running:
    window.update_window()
    palette.draw()
    painter.handle_events()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    pygame.display.flip()

window.close_window()

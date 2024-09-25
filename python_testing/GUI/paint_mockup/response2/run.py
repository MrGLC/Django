import pygame
from main.paint_window import PaintWindow
from main.painter import Painter
from main.colors import ColorPalette
from main.settings import Settings
from main.utils import get_mouse_position


pygame.init()

window = PaintWindow(Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT, Settings.WINDOW_TITLE)
window.create_window()

palette = ColorPalette()
painter = Painter(window, palette)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            painter.fill(event.user_event.color_index)
        painter.handle_events()

    painter.color_palette_view.draw()
    painter.draw_brush(get_mouse_position())

    window.update_window()

window.close_window()

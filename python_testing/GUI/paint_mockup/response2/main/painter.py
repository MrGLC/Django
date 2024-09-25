import pygame
from pygame.locals import *
from main.colors import ColorPalette
from main.paint_window import PaintWindow
from main.views import ColorPaletteView, DrawingView

class Painter:
    def __init__(self, window, palette):
        self.window = window
        self.palette = palette
        self.current_color = palette.get_color(0)
        self.brush_size = 10
        self.drawing_view = DrawingView(window.screen)
        self.color_palette_view = ColorPaletteView(window.screen, palette)

    def draw_brush(self, pos):
        color = self.current_color.get_pygame_color()
        self.drawing_view.draw_brush(pos, color, self.brush_size)

    def fill(self, color_index):
        self.current_color = self.palette.get_color(color_index)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.window.close_window()
            elif event.type == MOUSEBUTTONDOWN:
                self.drawing_view.start_drawing(get_mouse_position())
            elif event.type == MOUSEBUTTONUP:
                self.drawing_view.stop_drawing()
            elif event.type == MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:
                    self.drawing_view.draw_line(get_mouse_position())

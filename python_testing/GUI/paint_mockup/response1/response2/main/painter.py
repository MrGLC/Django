import pygame
from pygame.locals import *
from main.colors import ColorPalette
from main.paint_window import PaintWindow
from main.utils import get_mouse_position

class Painter:
    def __init__(self, window, palette):
        self.window = window
        self.palette = palette
        self.current_color = palette.get_color(0)
        self.brush_size = 10
        self.is_drawing = False

    def draw_brush(self, pos):
        color = self.current_color.get_pygame_color()
        pygame.draw.circle(self.window.screen, color, pos, self.brush_size)

    def fill(self, color_index):
        self.current_color = self.palette.get_color(color_index)

    def draw_line(self, start_pos, end_pos):
        color = self.current_color.get_pygame_color()
        pygame.draw.line(self.window.screen, color, start_pos, end_pos, self.brush_size)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.window.close_window()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    self.is_drawing = True
                    self.start_pos = get_mouse_position()
            elif event.type == MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button
                    self.is_drawing = False
            elif event.type == MOUSEMOTION:
                if self.is_drawing:
                    end_pos = get_mouse_position()
                    self.draw_line(self.start_pos, end_pos)
                    self.start_pos = end_pos

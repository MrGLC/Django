import pygame

class ColorPaletteView:
    def __init__(self, screen, palette):
        self.screen = screen
        self.palette = palette
        self.color_rects = []

    def draw(self):
        for i, color in enumerate(self.palette.colors):
            rect = pygame.Rect(10 + (i % 8) * 30, 10 + (i // 8) * 30, 20, 20)
            self.screen.fill(color.get_pygame_color(), rect)
            self.color_rects.append(rect)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                for rect in self.color_rects:
                    if rect.collidepoint(event.pos):
                        index = self.color_rects.index(rect)
                        pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'color_index': index}))

class DrawingView:
    def __init__(self, screen):
        self.screen = screen
        self.drawing = False
        self.line_color = (0, 0, 0)
        self.line_width = 10
        self.line_list = []

    def draw_brush(self, pos, color, size):
        self.line_color = color
        self.line_width = size
        if not self.drawing:
            self.line_list.append([pos, pos])
        else:
            self.line_list[-1][1] = pos
        self.draw_lines()

    def start_drawing(self, pos):
        self.drawing = True
        self.line_list.append([pos, pos])

    def stop_drawing(self):
        self.drawing = False

    def draw_line(self, pos):
        if self.drawing:
            self.line_list[-1][1] = pos
        self.draw_lines()

    def draw_lines(self):
        self.screen.fill(self.line_color, self.line_list[0][0], self.line_list[0][1], self.line_width)
        for line in self.line_list[1:]:
            self.screen.line(line[0], line[1], self.line_color, self.line_width)

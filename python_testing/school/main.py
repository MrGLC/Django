import pygame

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
BROWN = (139, 69, 19)
GREY = (200, 200, 200)
PINK = (255, 192, 203)

# Inicializar Pygame
pygame.init()
window_width, window_height = 1800, 1169
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Drawing App")

# Definir los rectángulos de colores y botones
color_squares = {
    BLACK: pygame.Rect(window_width - 210, window_height - 210, 50, 50),
    WHITE: pygame.Rect(window_width - 150, window_height - 210, 50, 50),
    BLUE: pygame.Rect(window_width - 90, window_height - 210, 50, 50),
    YELLOW: pygame.Rect(window_width - 210, window_height - 150, 50, 50),
    RED: pygame.Rect(window_width - 150, window_height - 150, 50, 50),
    GREEN: pygame.Rect(window_width - 90, window_height - 150, 50, 50),
    PURPLE: pygame.Rect(window_width - 210, window_height - 90, 50, 50),
    BROWN: pygame.Rect(window_width - 150, window_height - 90, 50, 50),
}
button_rects = {
    "Erase": pygame.Rect(window_width - 220, 10, 200, 120),
    "Azul": pygame.Rect(window_width - 220, 160, 200, 120),
    "Blanco": pygame.Rect(window_width - 220, 360, 200, 120),
    "Rosa": pygame.Rect(window_width - 220, 560, 200, 120),
}
button_colors = {
    "Azul": BLUE,
    "Blanco": WHITE,
    "Rosa": PINK,
}

# Variables de dibujo
drawn_positions = []
current_color = BLACK
drawing = False
last_pos = None

def draw_interface(screen, color_squares, button_rects, drawn_positions, current_color):
    screen.fill(GREY)  # Rellenar el fondo
    # Dibujar los cuadros de color
    for color, rect in color_squares.items():
        pygame.draw.rect(screen, color, rect)
    # Dibujar los botones con bordes y colores rellenos
    for label, rect in button_rects.items():
        button_color = button_colors.get(label, GREY)  # Por defecto GREY para otros botones
        pygame.draw.rect(screen, button_color, rect)  # Rellenar el botón con color
        pygame.draw.rect(screen, BLACK, rect, 3)  # Dibujar el borde
        text = pygame.font.Font(None, 36).render(label, True, BLACK)
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text, text_rect)
    # Dibujar todas las posiciones previas y líneas
    for item in drawn_positions:
        if len(item) == 2:  # Posición única
            pos, color = item
            pygame.draw.circle(screen, color, pos, 5)
        elif len(item) == 3:  # Línea continua
            start_pos, end_pos, color = item
            pygame.draw.line(screen, color, start_pos, end_pos, 5)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Botón izquierdo del ratón
                drawing = True
                last_pos = event.pos
                # Comprobar si se hizo clic en un cuadro de color
                for color, rect in color_squares.items():
                    if rect.collidepoint(event.pos):
                        current_color = color
                        drawing = False  # Evitar dibujar cuando se selecciona un color
                        break
                # Comprobar si se hizo clic en un botón
                for label, rect in button_rects.items():
                    if rect.collidepoint(event.pos):
                        if label == "Erase":
                            drawn_positions.clear()
                        drawing = False  # Evitar dibujar cuando se presiona un botón
                        break
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Botón izquierdo del ratón
                drawing = False
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                current_pos = event.pos
                drawn_positions.append((last_pos, current_pos, current_color))
                last_pos = current_pos

    draw_interface(screen, color_squares, button_rects, drawn_positions, current_color)
    pygame.display.flip()

pygame.quit()


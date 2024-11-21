import pygame
import math  # Для вычисления координат вершин треугольников

pygame.init()

# Параметры игры
fps = 5000
timer = pygame.time.Clock()
WIDTH, HEIGHT = 800, 600
active_size = 0
active_color = 'white'
painting = []
current_tool = 'brush'

# Инициализация окна
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Paint")

# Функция для рисования меню
def draw_menu(color, size):
    pygame.draw.rect(screen, 'gray', [0, 0, WIDTH, 70])
    pygame.draw.line(screen, 'black', (0, 70), (WIDTH, 70))

    # Кнопки размеров кисти
    xl_brush = pygame.draw.rect(screen, 'black', [10, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (35, 35), 20)
    l_brush = pygame.draw.rect(screen, 'black', [70, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (95, 35), 15)
    m_brush = pygame.draw.rect(screen, 'black', [130, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (155, 35), 10)
    s_brush = pygame.draw.rect(screen, 'black', [190, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (215, 35), 5)
    brush_list = [xl_brush, l_brush, m_brush, s_brush]

    # Кнопки выбора цвета
    pygame.draw.circle(screen, color, (400, 35), 30)
    blue = pygame.draw.rect(screen, (0, 0, 255), [WIDTH - 35, 10, 25, 25])
    red = pygame.draw.rect(screen, (255, 0, 0), [WIDTH - 35, 35, 25, 25])
    green = pygame.draw.rect(screen, (0, 255, 0), [WIDTH - 60, 10, 25, 25])
    yellow = pygame.draw.rect(screen, (255, 255, 0), [WIDTH - 60, 35, 25, 25])
    teal = pygame.draw.rect(screen, (0, 255, 255), [WIDTH - 85, 10, 25, 25])
    purple = pygame.draw.rect(screen, (255, 0, 255), [WIDTH - 85, 35, 25, 25])
    white = pygame.draw.rect(screen, (255, 255, 255), [WIDTH - 110, 10, 25, 25])
    black = pygame.draw.rect(screen, (0, 0, 0), [WIDTH - 110, 35, 25, 25])

    # Кнопки инструментов
    circle_button = pygame.draw.rect(screen, 'black', [250, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (275, 35), 20)
    rectangle_button = pygame.draw.rect(screen, 'black', [310, 10, 50, 50])
    pygame.draw.rect(screen, 'white', [315, 15, 40, 40])
    square_button = pygame.draw.rect(screen, 'black', [370, 10, 50, 50])
    pygame.draw.rect(screen, 'white', [375, 15, 40, 40])
    triangle_button = pygame.draw.rect(screen, 'black', [430, 10, 50, 50])
    pygame.draw.polygon(screen, 'white', [(435, 55), (455, 15), (475, 55)])
    eq_triangle_button = pygame.draw.rect(screen, 'black', [490, 10, 50, 50])
    pygame.draw.polygon(screen, 'white', [(515, 15), (495, 55), (535, 55)])
    rhombus_button = pygame.draw.rect(screen, 'black', [550, 10, 50, 50])
    pygame.draw.polygon(screen, 'white', [(575, 15), (560, 35), (575, 55), (590, 35)])

    tool_buttons = [circle_button, rectangle_button, square_button, triangle_button, eq_triangle_button, rhombus_button]
    color_buttons = [blue, red, green, yellow, teal, purple, white, black]
    colors = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 255, 255), (255, 0, 255), (255, 255, 255), (0, 0, 0)]

    return brush_list, tool_buttons, color_buttons, colors

# Функция для рисования рисунка
def draw_painting(paints):
    for i in range(len(paints)):
        if paints[i][0] == 'circle':
            pygame.draw.circle(screen, paints[i][1], paints[i][2], paints[i][3])
        elif paints[i][0] == 'rectangle':
            pygame.draw.rect(screen, paints[i][1], paints[i][2])
        elif paints[i][0] == 'square':
            pygame.draw.rect(screen, paints[i][1], paints[i][2])
        elif paints[i][0] == 'triangle':
            pygame.draw.polygon(screen, paints[i][1], paints[i][2])
        elif paints[i][0] == 'rhombus':
            pygame.draw.polygon(screen, paints[i][1], paints[i][2])

# Основной игровой цикл
running = True
while running:
    timer.tick(fps)
    screen.fill("white")
    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]

    if left_click and mouse[1] > 70:
        if current_tool == 'brush':
            painting.append((active_color, mouse, active_size))
        elif current_tool == 'circle':
            painting.append(('circle', active_color, mouse, active_size * 3))
        elif current_tool == 'rectangle':
            rect_x, rect_y = mouse[0] - active_size, mouse[1] - active_size
            painting.append(('rectangle', active_color, pygame.Rect(rect_x, rect_y, 4 * active_size, 2 * active_size)))
        elif current_tool == 'square':
            side = 4 * active_size
            painting.append(('square', active_color, pygame.Rect(mouse[0], mouse[1], side, side)))
        elif current_tool == 'triangle':
            triangle_points = [(mouse[0], mouse[1] - 3 * active_size), (mouse[0] - 2 * active_size, mouse[1] + 2 * active_size),
                               (mouse[0] + 2 * active_size, mouse[1] + 2 * active_size)]
            painting.append(('triangle', active_color, triangle_points))
        elif current_tool == 'rhombus':
            rhombus_points = [(mouse[0], mouse[1] - 2 * active_size), (mouse[0] - 2 * active_size, mouse[1]),
                              (mouse[0], mouse[1] + 2 * active_size), (mouse[0] + 2 * active_size, mouse[1])]
            painting.append(('rhombus', active_color, rhombus_points))

    draw_painting(painting)
    if mouse[1] > 70 and current_tool == 'brush':
        pygame.draw.circle(screen, active_color, mouse, active_size)

    brushes, tools, colors, rgb_list = draw_menu(active_color, active_size)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, button in enumerate(brushes):
                if button.collidepoint(event.pos):
                    active_size = 20 - (i * 5)
            for i, button in enumerate(tools):
                if button.collidepoint(event.pos):
                    current_tool = ['circle', 'rectangle', 'square', 'triangle', 'equilateral', 'rhombus'][i]
            for i, button in enumerate(colors):
                if button.collidepoint(event.pos):
                    active_color = rgb_list[i]

    pygame.display.flip()

pygame.quit()

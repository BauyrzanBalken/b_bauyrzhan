import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))  # Увеличено окно
    pygame.display.set_caption("Рисовалка")  # Название окна
    clock = pygame.time.Clock()

    radius = 15
    color = (0, 0, 255)  # Синий по умолчанию
    drawing_mode = 'line'  # Режим рисования по умолчанию
    points = []
    start_pos = None  # Для прямоугольников и кругов

    font = pygame.font.SysFont(None, 24)  # Шрифт для инструкций
    background = pygame.Surface(screen.get_size())  # Создание фона
    background.fill((50, 50, 50))  # Задаём фон (тёмно-серый)

    running = True
    while running:
        for event in pygame.event.get():
            # Выход
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                # Смена режимов рисования
                if event.key == pygame.K_r:
                    color = (255, 0, 0)  # Красный
                elif event.key == pygame.K_g:
                    color = (0, 255, 0)  # Зелёный
                elif event.key == pygame.K_b:
                    color = (0, 0, 255)  # Синий
                elif event.key == pygame.K_l:  # Линия
                    drawing_mode = 'line'
                elif event.key == pygame.K_c:  # Круг
                    drawing_mode = 'circle'
                elif event.key == pygame.K_e:  # Ластик
                    drawing_mode = 'eraser'
                elif event.key == pygame.K_t:  # Прямоугольник
                    drawing_mode = 'rectangle'

            # Обработка кликов мыши
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # ЛКМ
                    if drawing_mode in ['rectangle', 'circle']:
                        start_pos = event.pos  # Начальная позиция
                    elif drawing_mode == 'eraser':
                        pygame.draw.circle(background, (50, 50, 50), event.pos, radius)  # Стираем на фоне
                elif event.button == 4:  # Увеличение кисти
                    radius = min(200, radius + 1)
                elif event.button == 5:  # Уменьшение кисти
                    radius = max(1, radius - 1)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and start_pos:
                    end_pos = event.pos
                    if drawing_mode == 'rectangle':
                        rect = pygame.Rect(*start_pos, end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])
                        pygame.draw.rect(background, color, rect, width=radius)  # Рисуем на фоне
                    elif drawing_mode == 'circle':
                        center = start_pos
                        radius_circle = int(((end_pos[0] - center[0]) ** 2 + (end_pos[1] - center[1]) ** 2) ** 0.5)
                        pygame.draw.circle(background, color, center, radius_circle, width=radius)  # Рисуем на фоне
                    start_pos = None

            if event.type == pygame.MOUSEMOTION:
                if drawing_mode == 'line' and pygame.mouse.get_pressed()[0]:
                    position = event.pos
                    points.append(position)
                    if len(points) > 1:
                        pygame.draw.line(background, color, points[-2], points[-1], radius)  # Рисуем линии на фоне
                elif drawing_mode == 'eraser' and pygame.mouse.get_pressed()[0]:
                    pygame.draw.circle(background, (50, 50, 50), event.pos, radius)  # Стираем на фоне

        # Отображение фона
        screen.blit(background, (0, 0))

        # Отображение инструкции
        instruction = (
            "Инструкция: R - красный, G - зелёный, B - синий, "
            "L - линия, T - прямоугольник, C - круг, E - ластик, "
            "Колёсико мыши - размер кисти"
        )
        text_surface = font.render(instruction, True, (255, 255, 255))  # Белый текст
        screen.blit(text_surface, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

main()

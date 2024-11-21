import pygame
import random
import sys

# Инициализация pygame
pygame.init()

# Размеры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 20  # Размер клетки
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Змейка с уровнями")

# Цвета
WHITE = (255, 255, 255)  # Белый
BLACK = (0, 0, 0)        # Черный
GREEN = (0, 200, 0)      # Зеленый
RED = (200, 0, 0)        # Красный

# Часы для управления частотой кадров
clock = pygame.time.Clock()

# Шрифт для отображения очков и уровня
font = pygame.font.Font(None, 36)

# Настройки игры
speed = 10  # Начальная скорость
snake = [(100, 100), (80, 100), (60, 100)]  # Змейка — список координат (x, y)
direction = "RIGHT"  # Начальное направление движения
food_pos = (200, 200)  # Позиция еды
score = 0  # Текущие очки
level = 1  # Текущий уровень
foods_to_next_level = 3  # Количество еды для перехода на следующий уровень

def generate_food():
    """
    Генерация случайной позиции для еды, которая не перекрывается со змейкой.
    """
    while True:
        x = random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE
        y = random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
        if (x, y) not in snake:
            return (x, y)

def draw_snake():
    """
    Отрисовка змейки на экране.
    """
    for segment in snake:
        pygame.draw.rect(screen, WHITE, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))

def draw_food():
    """
    Отрисовка еды на экране.
    """
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))

def check_collision():
    """
    Проверка столкновений:
    - со стеной
    - с самим собой.
    """
    global running
    head_x, head_y = snake[0]
    # Проверка столкновения со стеной
    if head_x < 0 or head_x >= SCREEN_WIDTH or head_y < 0 or head_y >= SCREEN_HEIGHT:
        running = False
    # Проверка столкновения с телом змейки
    if (head_x, head_y) in snake[1:]:
        running = False

def draw_score_and_level():
    """
    Отображение очков и уровня на экране.
    """
    score_text = font.render(f"Очки: {score}", True, WHITE)
    level_text = font.render(f"Уровень: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

# Основной игровой цикл
running = True
while running:
    screen.fill(BLACK)  # Очистка экрана (заливка черным цветом)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Изменение направления движения змейки
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    # Движение змейки
    head_x, head_y = snake[0]
    if direction == "UP":
        new_head = (head_x, head_y - CELL_SIZE)
    elif direction == "DOWN":
        new_head = (head_x, head_y + CELL_SIZE)
    elif direction == "LEFT":
        new_head = (head_x - CELL_SIZE, head_y)
    elif direction == "RIGHT":
        new_head = (head_x + CELL_SIZE, head_y)
    # Добавляем новую голову и убираем хвост
    snake = [new_head] + snake[:-1]

    # Проверка столкновения с едой
    if snake[0] == food_pos:
        snake.append(snake[-1])  # Увеличиваем длину змейки
        food_pos = generate_food()  # Генерируем новую еду
        score += 1  # Увеличиваем счет
        if score % foods_to_next_level == 0:  # Проверяем, пора ли перейти на новый уровень
            level += 1
            speed += 2  # Увеличиваем скорость игры

    # Проверка столкновений
    check_collision()

    # Отрисовка объектов
    draw_snake()
    draw_food()
    draw_score_and_level()

    # Обновление экрана
    pygame.display.flip()

    # Управление частотой кадров
    clock.tick(speed)

# Завершение работы
pygame.quit()
sys.exit()


import pygame as pg
import random

# Инициализация Pygame
pg.init()

# Параметры окна и игры
w, h, fps = 400, 600, 60
is_running, lose = True, False
screen = pg.display.set_mode((w, h))
pg.display.set_caption('Racer')  # Заголовок окна
clock = pg.time.Clock()

# Глобальные переменные
y = 0
ry = 2
step, enemy_step, score, score_coin = 5, 5, 0, 0
coins_needed_to_speed_up = 5  # Количество монет для увеличения скорости врага

# Загрузка изображений
game_over = pg.image.load("gameover.jpg")
bg = pg.image.load("AnimatedStreet.png")
game_over = pg.transform.scale(game_over, (w, h))

# Шрифты для текста
score_font = pg.font.SysFont("Verdana", 20)
score_coins = pg.font.SysFont("Verdana", 20)


# Класс врага (Enemy)
class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("Enemy.png")  # Загрузка изображения врага
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, w - 40), 0)  # Рандомная начальная позиция

    def update(self):
        """Движение врага вниз."""
        global score
        self.rect.move_ip(0, enemy_step)  # Движение вниз с фиксированной скоростью
        if self.rect.bottom > h + 90:  # Если враг вышел за пределы экрана
            score += 1  # Увеличиваем счёт
            self.rect.top = 0
            self.rect.center = (random.randint(30, 350), 0)

    def draw(self, surface):
        """Отрисовка врага."""
        surface.blit(self.image, self.rect)


# Класс игрока (Player)
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("Player.png")  # Загрузка изображения игрока
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        """Движение игрока по клавишам."""
        pressed_keys = pg.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[pg.K_a]:
            self.rect.move_ip(-step, 0)
        if self.rect.right < w and pressed_keys[pg.K_d]:
            self.rect.move_ip(step, 0)
        if self.rect.top > 0 and pressed_keys[pg.K_w]:
            self.rect.move_ip(0, -step)
        if self.rect.bottom < h and pressed_keys[pg.K_s]:
            self.rect.move_ip(0, step)

    def draw(self, surface):
        """Отрисовка игрока."""
        surface.blit(self.image, self.rect)


# Класс монеты (Coin)
class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("coin.png")  # Загрузка изображения монеты
        self.rect = self.image.get_rect()
        self.value = random.randint(1, 3)  # Случайное значение монеты (1-3 очка)
        self.rect.center = (random.randint(30, w - 30), random.randint(30, h - 130))

    def draw(self):
        """Отрисовка монеты."""
        screen.blit(self.image, self.rect)


# Создание объектов
p = Player()
e = Enemy()

# Группы для врагов и монет
enemies = pg.sprite.Group()
enemies.add(e)

coins = pg.sprite.Group()

# Генерация первой монеты
coin = Coin()
coins.add(coin)

# Основной игровой цикл
while is_running:
    clock.tick(fps)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False

    # Анимация движущегося фона
    screen.blit(pg.transform.scale(bg, (w, h)), (0, y % h))
    screen.blit(pg.transform.scale(bg, (w, h)), (0, -h + (y % h)))
    y += ry

    # Обновление объектов
    p.update()
    e.update()

    # Проверка столкновения с врагом
    if pg.sprite.spritecollideany(p, enemies):
        lose = True  # Если столкнулись, запускаем "game over"

    # Проверка сбора монет
    for coin in coins:
        coin.draw()
        if pg.sprite.collide_rect(p, coin):
            score_coin += coin.value  # Увеличиваем счёт на значение монеты
            coin.kill()  # Удаляем монету
            new_coin = Coin()  # Создаём новую монету
            coins.add(new_coin)  # Добавляем её в группу

    # Увеличение скорости врагов при наборе определённого количества монет
    if score_coin >= coins_needed_to_speed_up:
        enemy_step += 1  # Увеличиваем скорость врагов
        coins_needed_to_speed_up += 5  # Следующий порог увеличения скорости

    # Отрисовка объектов
    e.draw(screen)
    p.draw(screen)

    # Цикл "game over"
    while lose:
        clock.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        screen.blit(game_over, (0, 0))
        pg.display.flip()

    # Вывод счёта в правом верхнем углу
    score_text = score_font.render(f'Score: {score}', True, 'black')
    coins_text = score_coins.render(f'Coins: {score_coin}', True, 'black')
    screen.blit(score_text, (10, 10))
    screen.blit(coins_text, (300, 10))

    # Обновление экрана
    pg.display.flip()

pg.quit()

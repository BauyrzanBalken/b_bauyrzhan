import pygame
import sys

pygame.init()

BALL_RADIUS = 50
BALL_COLOR = (255, 0, 0)  
MOVE_DISTANCE = 20
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
BACKGROUND_COLOR = (255, 255, 255)  


screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Move the Ball")


x = WINDOW_WIDTH // 2
y = WINDOW_HEIGHT // 2


running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    keys = pygame.key.get_pressed()

   
    if keys[pygame.K_UP] and y - BALL_RADIUS > 0:
        y -= MOVE_DISTANCE
    if keys[pygame.K_DOWN] and y + BALL_RADIUS < WINDOW_HEIGHT:
        y += MOVE_DISTANCE
    if keys[pygame.K_LEFT] and x - BALL_RADIUS > 0:
        x -= MOVE_DISTANCE
    if keys[pygame.K_RIGHT] and x + BALL_RADIUS < WINDOW_WIDTH:
        x += MOVE_DISTANCE

   
    screen.fill(BACKGROUND_COLOR)

    
    pygame.draw.circle(screen, BALL_COLOR, (x, y), BALL_RADIUS)

    
    pygame.display.flip()

   
    pygame.time.Clock().tick(30)  


pygame.quit()

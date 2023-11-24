import pygame
import sys

pygame.init()


WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 25
BALL_DIAMETER = 2 * BALL_RADIUS
BALL_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (255, 255, 255)
MOVE_AMOUNT = 20


sc = pygame.display.set_mode((WIDTH, HEIGHT))


ball_x = WIDTH // 2
ball_y = HEIGHT // 2


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

   
    keys = pygame.key.get_pressed()

    
    if keys[pygame.K_UP] and ball_y - MOVE_AMOUNT >= 0:
        ball_y -= MOVE_AMOUNT
    if keys[pygame.K_DOWN] and ball_y + BALL_DIAMETER + MOVE_AMOUNT <= HEIGHT:
        ball_y += MOVE_AMOUNT
    if keys[pygame.K_LEFT] and ball_x - MOVE_AMOUNT >= 0:
        ball_x -= MOVE_AMOUNT
    if keys[pygame.K_RIGHT] and ball_x + BALL_DIAMETER + MOVE_AMOUNT <= WIDTH:
        ball_x += MOVE_AMOUNT

    
    sc.fill(BACKGROUND_COLOR)

    
    pygame.draw.circle(sc, BALL_COLOR, (ball_x + BALL_RADIUS, ball_y + BALL_RADIUS), BALL_RADIUS)

   
    pygame.display.flip()

    
    pygame.time.Clock().tick(30)

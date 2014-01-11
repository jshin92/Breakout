import pygame
import Paddle

FPS = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

dimensions = [700, 500]
pygame.init()
screen = pygame.display.set_mode(dimensions)
pygame.display.set_caption("Breakout")

paddle = Paddle.Paddle(screen)

done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                paddle.moving_right = True
            elif event.key == pygame.K_LEFT:
                paddle.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                paddle.moving_right = False
            elif event.key == pygame.K_LEFT:
                paddle.moving_left = False

    paddle.update()

    screen.fill(BLACK)
    paddle.draw()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
import pygame
import Paddle
import Ball
import Block


FPS = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

dimensions = [700, 500]
pygame.init()
pygame.mixer.init()
impact = pygame.mixer.Sound("sounds/impact.wav")
laser = pygame.mixer.Sound("sounds/laser.wav")
screen = pygame.display.set_mode(dimensions)
pygame.display.set_caption("Breakout")

paddle = Paddle.Paddle(screen)
ball = Ball.Ball(screen, paddle, impact, laser)
num_block_rows = 4
num_block_cols = 6
block_arr = []
for row in range(num_block_rows):
    for col in range(num_block_cols):
        block_arr.append(Block.Block(screen, col * (Block.BLOCK_WIDTH + Block.BLOCK_OFFSET),
                                             row * (Block.BLOCK_HEIGHT + Block.BLOCK_OFFSET)))
done = False
game_over = False
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

    if not game_over:
        paddle.update()
        ball.update(block_arr, game_over)

    screen.fill(BLACK)

    if not game_over:
        for b in block_arr:
            b.draw()
        paddle.draw()
        ball.draw()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
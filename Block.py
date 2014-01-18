import pygame
RED = (255, 0, 0)
BLOCK_WIDTH = 100
BLOCK_HEIGHT = 35
BLOCK_OFFSET = 14


class Block:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(self.screen, RED, [self.x + BLOCK_OFFSET,
                                            self.y + BLOCK_OFFSET,
                                            BLOCK_WIDTH,
                                            BLOCK_HEIGHT])
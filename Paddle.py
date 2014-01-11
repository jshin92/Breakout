import pygame

GREEN = (0, 255, 0)


class Paddle:
    def __init__(self, screen):
        self.screen = screen

        self.x = 100
        self.y = 470
        self.width = 100
        self.height = 15

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.within_right_bound():
            self.x += 10
        elif self.moving_left and self.within_left_bound():
            self.x -= 10

    def within_right_bound(self):
        return self.x <= 600

    def within_left_bound(self):
        return self.x >= 0

    def draw(self):
        pygame.draw.rect(self.screen, GREEN, [self.x, self.y, self.width, self.height])

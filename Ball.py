import pygame
import Block
import pygame.mixer

YELLOW = (255, 255, 0)


class Ball:
    def __init__(self, screen, paddle, impact, laser):
        self.screen = screen
        self.pos = [200, 220]
        self.x_velo = 8
        self.y_velo = 8
        self.radius = 10
        self.paddle = paddle

        self.impact = impact
        self.laser = laser

    def draw(self):
        pygame.draw.circle(self.screen, YELLOW, self.pos, self.radius)

    def collides_with_rect(self, rect_x, rect_y, rect_width, rect_height):
        # using algo from http://stackoverflow.com/questions/401847/
        # find closest point to circle within rectangle
        closest_x = clamp(self.pos[0], rect_x, rect_x + rect_width)
        closest_y = clamp(self.pos[1], rect_y, rect_y + rect_height)
        # calc distance bt circle's center and closest point
        x_dist = self.pos[0] - closest_x
        y_dist = self.pos[1] - closest_y
        # if this dist is < circle's radius, an intersection occurs
        dist_squared = x_dist * x_dist + y_dist * y_dist
        return dist_squared < self.radius * self.radius

    def collides_with_left_right_walls(self):
        return self.pos[0] < 20 or self.pos[0] > 680

    def collides_with_top_wall(self):
        return self.pos[1] < 20 or self.pos[1] > 480

    def update(self, block_arr, game_over):
        self.pos[0] += self.x_velo
        self.pos[1] += self.y_velo

        # collision against walls
        if self.collides_with_left_right_walls():
            self.x_velo *= -1
        elif self.collides_with_top_wall():
            self.y_velo *= -1
        # collision against paddle
        if self.collides_with_rect(self.paddle.x, self.paddle.y, self.paddle.width, self.paddle.height):
            self.y_velo *= -1
            self.impact.play()

        # collision against brick pieces
        for b in block_arr:
            if self.collides_with_rect(b.x + Block.BLOCK_OFFSET, b.y + Block.BLOCK_OFFSET, Block.BLOCK_WIDTH, Block.BLOCK_HEIGHT):
                block_arr.remove(b)
                self.y_velo *= -1
                self.laser.play()
                break


def clamp(val, minimum, maximum):
    if val < minimum:
        val = minimum
    elif val > maximum:
        val = maximum
    return val



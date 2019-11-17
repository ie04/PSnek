from snakeBlock import SnakeBlock
from constants import Directions
import pygame


class Snake:
    def __init__(self, direction=Directions.RIGHT):
        self.head_block = SnakeBlock()
        self.snake_blocks = [self.head_block]
        self.direction = direction

    def add_block(self, snake_block: SnakeBlock):
        self.snake_blocks.append(snake_block)
        if self.direction == Directions.UP | self.direction == Directions.DOWN:
            self.snake_blocks[-1].y = self.snake_blocks[-1 - 1].y + 1
            self.snake_blocks[-1].x = self.snake_blocks[-1 - 1].x
        else:
            self.snake_blocks[-1].x = self.snake_blocks[-1 - 1].x - 1
            self.snake_blocks[-1].y = self.snake_blocks[-1 - 1].y

    def move(self):
        if self.snake_blocks[0].pos.x >= 19:
            return
        if self.direction is Directions.UP:
            self.snake_blocks[0].offset_pos(0, -1)
        elif self.direction is Directions.DOWN:
            self.snake_blocks[0].offset_pos(0, 1)
        elif self.direction is Directions.LEFT:
            self.snake_blocks[0].offset_pos(-1, 0)
        elif self.direction is Directions.RIGHT:
            self.snake_blocks[0].offset_pos(1, 0)
        for i in range(len(self.snake_blocks)):
            if len(self.snake_blocks) == 1:
                break
            self.snake_blocks[1 + i].pos = self.snake_blocks[i].prev_pos

    def display(self, win):
        for block in self.snake_blocks:
            if block.pos.x > 19:
                block.x = 19
            if block.pos.y > 19:
                block.pos.y = 19
            pygame.draw.rect(win, (255, 255, 255), (block.pos.x * 25, block.pos.y * 25, 25, 25))


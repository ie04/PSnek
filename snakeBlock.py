import pygame


class SnakeBlock:
    def __init__(self):
        self.pos = pygame.math.Vector2(0, 0)
        self.prev_pos = self.pos

    def update_pos(self, pos):
        self.prev_pos = self.pos
        self.pos = pos

    def offset_pos(self, x: int, y: int):
        self.prev_pos = self.pos
        self.pos.x += x
        self.pos.y += y



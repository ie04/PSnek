import pygame

from snake import Snake
from snakeBlock import SnakeBlock

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("PySnek")
snake = Snake()
run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    snake.display(win)
    snake.move()
    pygame.display.update()


pygame.quit()


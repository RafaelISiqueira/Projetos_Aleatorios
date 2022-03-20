import pygame, random
from pygame.locals import *


def on_grid_random():
    x = random.randint(0, 400)
    y = random.randint(0, 400)
    return x // 10 * 10, y // 10 * 10


def colisão(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


CIMA = 0
DIREITA = 1
BAIXO = 2
ESQUERDA = 3

pygame.init()
screen = pygame.display.set_mode((550, 500))
pygame.display.set_caption('Snake')

snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((107, 142, 35))


maça_posição = on_grid_random()
maça = pygame.Surface((10, 10))
maça.fill((255, 0, 0))

my_direction = ESQUERDA

clock = pygame.time.Clock()

while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = CIMA
            if event.key == K_DOWN:
                my_direction = BAIXO
            if event.key == K_LEFT:
                my_direction = ESQUERDA
            if event.key == K_RIGHT:
                my_direction = DIREITA

    if colisão(snake[0], maça_posição):
        maça_posição = on_grid_random()
        snake.append((0, 0))

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    if my_direction == CIMA:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == BAIXO:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == DIREITA:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == ESQUERDA:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    screen.fill((222,184,135))
    screen.blit(maça, maça_posição)

    for pos in snake:
        screen.blit(snake_skin, pos)

    pygame.display.update()

import random
import sys

import pygame
from pygame.locals import QUIT

RED = (213, 50, 80)
YELLOW = (255, 255, 102)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 153, 213)
GREEN = (0, 255, 0)

pygame.init()

screen_height = 1000
screen_width = 700
screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption('Snake_Hunt')

clock = pygame.time.Clock()

arialFont = pygame.font.SysFont("Arial", 30)


def message(msg, color):
    mesg = arialFont.render(msg, True, color)
    textRect = mesg.get_rect()
    textRect.center = (screen_height // 2, screen_width // 2)
    screen.blit(mesg, textRect)


randFoodX = random.randrange(0, screen_width - 10)
surplusFoodX = randFoodX % 10
foodx = round(randFoodX - surplusFoodX)
randFoodY = random.randrange(0, screen_width - 10)
surplusFoodY = randFoodY % 10
foody = round(randFoodY - surplusFoodY)

snake_list = []
snake_length = 1
snake_block = 10
x_head = screen_height // 2
y_head = screen_width // 2


def tao_ran(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, BLACK, [x[0], x[1], snake_block, snake_block])


def tao_diem_so(score):
    diem = arialFont.render("Score" + str(score), True, RED)
    screen.blit(diem, [0, 0])


game_close = False

while True:
    while game_close == True:
        x_head_change = 0
        y_head_change = 0
        message("You Lost! Press C-Play Again", RED)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_head_change = -10
                    y_head_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_head_change = 10
                    y_head_change = 0
                elif event.key == pygame.K_UP:
                    x_head_change = 0
                    y_head_change = -10
                elif event.key == pygame.K_DOWN:
                    x_head_change = 0
                    y_head_change = 10

        if (x_head >= screen_width) or (x_head < 0) or (y_head >= screen_height) or (y_head < 0):
            game_close = True

        x_head += x_head_change
        y_head += y_head_change
        screen.fill(BLUE)
        pygame.draw.rect(screen, BLUE, [foodx, foody, snake_block, snake_block])

        snake_head = []
        snake_head.append(x_head)
        snake_head.append(y_head)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        tao_ran(snake_block, snake_list)

        tao_diem_so(snake_length - 1)

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
        if x_head == foodx and y_head == foody:
            foodx = round(random.randrange(0, screen_width - snake_block) % 10)
            foody = round(random.randrange(0, screen_height - snake_block) % 10)
            snake_list += 1
        pygame.display.update()

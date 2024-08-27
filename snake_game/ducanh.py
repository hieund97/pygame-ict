
import pygame, sys, random

screen_width = 1000
screen_height = 700

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

white = (255, 255, 255)
mint = (194, 219, 190)
aqua = (77, 195, 194)
latte = (169, 109, 66)
red = (255, 0, 0)
black = (0, 0, 0)

snake_block = 10

x1 = screen_width / 2
y1 = screen_height / 2
x_change = 0
y_change = 0

randFoodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10
randFoody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10

snake_lst = []
snake_len = 1

def show(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color, x, y):
    font = pygame.font.SysFont("Monospace", 25)
    mesg = font.render(msg, True, color)
    text_rect = mesg.get_rect()
    text_rect.center = (x, y)
    screen.blit(mesg, text_rect)

def show_score(score):
    font = pygame.font.SysFont("Monospace", 17)
    value = font.render("Score: " + str(score), True, latte)
    screen.blit(value, [0, 0])

game_close = False

while True:
    while game_close:
        screen.fill(mint)
        message('You Lost! Press Q-Quit or C-Play Again', aqua, 300, 100)
        message(f'Score: {snake_len - 1}', aqua, 300, 150)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_c:
                    game_close = False
                    x1 = screen_width / 2
                    y1 = screen_height / 2
                    x_change = 0
                    y_change = 0
                    snake_lst = []
                    snake_len = 1

    if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
        game_close = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -snake_block
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = snake_block
                y_change = 0
            elif event.key == pygame.K_UP:
                y_change = -snake_block
                x_change = 0
            elif event.key == pygame.K_DOWN:
                y_change = snake_block
                x_change = 0
    
    screen.fill(mint)
    pygame.draw.rect(screen, red, [randFoodx, randFoody, snake_block, snake_block])
    x1 += x_change
    y1 += y_change

    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_lst.append(snake_head)
    if len(snake_lst) > snake_len:
        del snake_lst[0]

    show(snake_block, snake_lst)
    show_score(snake_len - 1)

    if x1 == randFoodx and y1 == randFoody:
        randFoodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10
        randFoody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10
        snake_len += 1

    pygame.display.update()
    clock.tick(12)

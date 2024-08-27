import pygame, sys, random

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (50, 153, 213)
green = (0, 255, 0)

pygame.init()

screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

snake_block = 10
x_head = 300
y_head = 200

x_head_change = 0
y_head_change = 0

clock = pygame.time.Clock()
fps = 10  

arial = pygame.font.SysFont(None, 50)

def message(msg, color):
    mesg = arial.render(msg, True, color)
    text_rect = mesg.get_rect(center=(screen_width / 2, screen_height / 2))
    screen.blit(mesg, text_rect)

def generate_food():
    rand_food_x = random.randrange(0, screen_width - snake_block, snake_block)
    rand_food_y = random.randrange(0, screen_height - snake_block, snake_block)
    return rand_food_x, rand_food_y

foodx, foody = generate_food()

snake_list = []
snake_length = 1

def show_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])

def show_score(score):
    value = arial.render("Score: " + str(score), True, red)
    screen.blit(value, [0, 0])

game_close = False

while True:
    while game_close:
        message("Aizz, ban da thua roi!", green)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_close = False
                    snake_list = []
                    snake_length = 1
                    x_head = 300
                    y_head = 200
                    x_head_change = 0
                    y_head_change = 0
                    foodx, foody = generate_food()
    if x_head >= screen_width or x_head < 0 or y_head >= screen_height or y_head < 0:
        game_close = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x_head_change == 0:
                x_head_change = -snake_block
                y_head_change = 0
            elif event.key == pygame.K_RIGHT and x_head_change == 0:
                x_head_change = snake_block
                y_head_change = 0
            elif event.key == pygame.K_UP and y_head_change == 0:
                y_head_change = -snake_block
                x_head_change = 0
            elif event.key == pygame.K_DOWN and y_head_change == 0:
                y_head_change = snake_block
                x_head_change = 0

    x_head += x_head_change
    y_head += y_head_change

    screen.fill(white)
    pygame.draw.rect(screen, blue, [foodx, foody, snake_block, snake_block])

    snake_head = [x_head, y_head]
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    for x in snake_list[:-1]:
        if x == snake_head:
            game_close = True

    show_snake(snake_block, snake_list)
    show_score(snake_length - 1)

    if x_head == foodx and y_head == foody:
        foodx, foody = generate_food()
        snake_length += 1

    pygame.display.update()
    clock.tick(fps)
import pygame
import time
import random

pygame.init()

# Các màu sắc
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
grey = (169, 169, 169)
arrow_colors = {
    "UP": grey,
    "DOWN": grey,
    "LEFT": grey,
    "RIGHT": grey
}

# Kích thước màn hình
dis_width = 800
dis_height = 600

# Tạo cửa sổ game
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

# Khung thời gian
clock = pygame.time.Clock()

# Kích thước của rắn
snake_block = 10
snake_speed = 15

# Font chữ
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def draw_arrows():
    center_x = dis_width // 2
    bottom_y = dis_height - 100
    arrow_size = 30
    spacing = 40

    # UP arrow
    pygame.draw.polygon(dis, arrow_colors["UP"], [(center_x, bottom_y - arrow_size - spacing), 
                                                  (center_x - arrow_size / 2, bottom_y - spacing), 
                                                  (center_x + arrow_size / 2, bottom_y - spacing)])
    
    # DOWN arrow
    pygame.draw.polygon(dis, arrow_colors["DOWN"], [(center_x, bottom_y + arrow_size + spacing), 
                                                    (center_x - arrow_size / 2, bottom_y + spacing), 
                                                    (center_x + arrow_size / 2, bottom_y + spacing)])
    
    # LEFT arrow
    pygame.draw.polygon(dis, arrow_colors["LEFT"], [(center_x - arrow_size - spacing, bottom_y), 
                                                    (center_x - spacing, bottom_y - arrow_size / 2), 
                                                    (center_x - spacing, bottom_y + arrow_size / 2)])
    
    # RIGHT arrow
    pygame.draw.polygon(dis, arrow_colors["RIGHT"], [(center_x + arrow_size + spacing, bottom_y), 
                                                     (center_x + spacing, bottom_y - arrow_size / 2), 
                                                     (center_x + spacing, bottom_y + arrow_size / 2)])

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_List):
    for x in snake_List:
        pygame.draw.circle(dis, black, [x[0] + snake_block // 2, x[1] + snake_block // 2], snake_block // 2)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():
    global snake_speed
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    direction = ""

    while not game_over:

        while game_close:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != "RIGHT":
                    x1_change = -snake_block
                    y1_change = 0
                    direction = "LEFT"
                    arrow_colors["LEFT"] = white
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    x1_change = snake_block
                    y1_change = 0
                    direction = "RIGHT"
                    arrow_colors["RIGHT"] = white
                elif event.key == pygame.K_UP and direction != "DOWN":
                    y1_change = -snake_block
                    x1_change = 0
                    direction = "UP"
                    arrow_colors["UP"] = white
                elif event.key == pygame.K_DOWN and direction != "UP":
                    y1_change = snake_block
                    x1_change = 0
                    direction = "DOWN"
                    arrow_colors["DOWN"] = white
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    arrow_colors["LEFT"] = grey
                elif event.key == pygame.K_RIGHT:
                    arrow_colors["RIGHT"] = grey
                elif event.key == pygame.K_UP:
                    arrow_colors["UP"] = grey
                elif event.key == pygame.K_DOWN:
                    arrow_colors["DOWN"] = grey

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.circle(dis, green, [foodx + snake_block // 2, foody + snake_block // 2], snake_block // 2)
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        draw_arrows()

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            snake_speed += 1  # Tăng tốc độ theo điểm số

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
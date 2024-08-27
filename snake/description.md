# Hướng Dẫn Mã Lập Trình Game Snake

Đoạn mã lập trình trò chơi Snake sử dụng thư viện `pygame` của Python để xây dựng một trò chơi có giao diện đồ họa đơn giản. Dưới đây là giải thích chi tiết cách thức hoạt động của từng phần của mã:

## 1. Khởi tạo và Cấu hình Ban đầu

```python
import pygame
import time
import random

pygame.init()
```

- **Import các thư viện**: Mã này sử dụng `pygame` để xử lý đồ họa và sự kiện, `time` để xử lý thời gian, và `random` để tạo các vị trí ngẫu nhiên cho thức ăn.
- **Khởi tạo Pygame**: `pygame.init()` khởi tạo tất cả các mô-đun cần thiết trong `pygame`.

## 2. Thiết lập các hằng số và màu sắc

```python
# Các màu sắc
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Kích thước màn hình
dis_width = 800
dis_height = 600

# Tạo cửa sổ game
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Edureka')

# Khung thời gian
clock = pygame.time.Clock()

# Kích thước của rắn
snake_block = 10
snake_speed = 15

# Font chữ
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
```

- **Màu sắc**: Sử dụng hệ màu RGB để định nghĩa màu cho nền, rắn, thức ăn, và các thông báo.
- **Kích thước cửa sổ**: `dis_width` và `dis_height` xác định kích thước của cửa sổ trò chơi.
- **Tạo cửa sổ trò chơi**: `pygame.display.set_mode()` tạo cửa sổ với kích thước được chỉ định. `pygame.display.set_caption()` thiết lập tiêu đề cho cửa sổ.
- **Khung thời gian**: `clock` dùng để điều chỉnh tốc độ của trò chơi.
- **Kích thước và tốc độ của rắn**: `snake_block` xác định kích thước của mỗi khối rắn, `snake_speed` xác định tốc độ di chuyển của rắn.
- **Font chữ**: `font_style` và `score_font` để hiển thị văn bản và điểm số.

## 3. Các Hàm Hỗ trợ

### a. Hiển thị điểm số

```python
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    dis.blit(value, [0, 0])
```

- **Hiển thị điểm số**: Hàm này dùng để hiển thị điểm số của người chơi trên cửa sổ trò chơi.

### b. Vẽ rắn

```python
def our_snake(snake_block, snake_List):
    for x in snake_List:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
```

- **Vẽ rắn**: Hàm này dùng để vẽ từng khối của rắn trên cửa sổ trò chơi.

### c. Hiển thị thông báo

```python
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
```

- **Hiển thị thông báo**: Hàm này dùng để hiển thị các thông báo, ví dụ như thông báo khi trò chơi kết thúc.

## 4. Vòng lặp Chính của Trò Chơi

```python
def gameLoop():
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

    while not game_over:
        while game_close == True:
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
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
```

- **Khởi tạo trò chơi**: `x1` và `y1` đặt vị trí ban đầu của rắn. `x1_change` và `y1_change` là các biến điều khiển di chuyển của rắn.
- **Vòng lặp chính**: Chạy liên tục cho đến khi trò chơi kết thúc. Xử lý các sự kiện, cập nhật vị trí của rắn, vẽ rắn và thức ăn, và kiểm tra điều kiện thắng/thua.
- **Kết thúc trò chơi**: Khi rắn va vào tường hoặc tự cắn vào chính nó, trò chơi kết thúc và cho phép người chơi chọn giữa thoát hoặc chơi lại.

## Tóm lại

Mã này thiết lập và chạy trò chơi Snake với giao diện đồ họa, cho phép người chơi điều khiển rắn di chuyển để ăn thức ăn và kéo dài kích thước của rắn. Khi rắn va vào tường hoặc tự cắn vào chính nó, trò chơi kết thúc và người chơi có thể chọn chơi lại hoặc thoát.

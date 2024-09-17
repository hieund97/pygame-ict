# Giải thích Mã Lập Trình Game Tic Tac Toe

Đoạn mã lập trình trò chơi Tic Tac Toe sử dụng thư viện `pygame` của Python để xây dựng một trò chơi có giao diện đồ họa đơn giản, cho phép người chơi lần lượt đánh dấu `O` và `X` trên bảng 3x3. Dưới đây là giải thích chi tiết cách thức hoạt động của từng phần của mã:

## 1. Khởi tạo và Cấu hình Ban đầu

```python
import pygame
import sys
import numpy as np

# Khởi tạo Pygame
pygame.init()
```

- **Import các thư viện**: Mã này sử dụng `pygame` để xử lý đồ họa và sự kiện, `sys` để thoát khỏi chương trình và `numpy` để tạo bảng trò chơi dưới dạng mảng 2 chiều.
- **Khởi tạo Pygame**: `pygame.init()` khởi tạo tất cả các mô-đun cần thiết trong `pygame`.

## 2. Thiết lập các hằng số và màu sắc

```python
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
WIN_LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Màu sắc
RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
```

- **Kích thước cửa sổ**: `WIDTH` và `HEIGHT` được đặt là 600, tạo một cửa sổ hình vuông 600x600 pixel. 
- **Thiết lập các thông số khác**: `LINE_WIDTH` xác định độ dày của các đường kẻ bảng, `CIRCLE_RADIUS` và `CIRCLE_WIDTH` xác định bán kính và độ dày của hình tròn, `CROSS_WIDTH` xác định độ dày của hình chữ X.
- **Màu sắc**: Sử dụng hệ màu RGB để định nghĩa màu nền, màu đường kẻ, màu cho các hình `O` và `X`.

## 3. Tạo cửa sổ và bảng trò chơi

```python
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)

# Bảng trò chơi
board = np.zeros((BOARD_ROWS, BOARD_COLS))
```

- **Tạo cửa sổ trò chơi**: `pygame.display.set_mode((WIDTH, HEIGHT))` tạo cửa sổ với kích thước được chỉ định. `pygame.display.set_caption('Tic Tac Toe')` thiết lập tiêu đề cho cửa sổ.
- **Điền màu nền**: `screen.fill(BG_COLOR)` tô màu nền của cửa sổ bằng màu đã định nghĩa.
- **Khởi tạo bảng trò chơi**: `board = np.zeros((BOARD_ROWS, BOARD_COLS))` tạo một mảng 2 chiều 3x3 với giá trị ban đầu là 0, tượng trưng cho các ô trống trên bảng.

## 4. Hàm vẽ và xử lý trò chơi

### a. Vẽ các đường kẻ của bảng

```python
def draw_lines():
    # Đường ngang
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)

    # Đường dọc
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
```

- **Vẽ đường ngang và dọc**: Hàm này sử dụng `pygame.draw.line()` để vẽ các đường kẻ ngang và dọc chia bảng thành 9 ô vuông.

### b. Vẽ các ký hiệu O và X

```python
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (
                    int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)),
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)
```

- **Vẽ O**: `pygame.draw.circle()` vẽ hình tròn (O) nếu ô đó có giá trị là `1`.
- **Vẽ X**: `pygame.draw.line()` vẽ hai đường cắt chéo nhau để tạo thành hình chữ X nếu ô đó có giá trị là `2`.

### c. Các hàm xử lý trò chơi

- **Đánh dấu ô**:

```python
def mark_square(row, col, player):
    board[row][col] = player
```

Hàm này gán giá trị của `player` (1 cho `O` và 2 cho `X`) vào ô được chọn.

- **Kiểm tra ô trống**:

```python
def available_square(row, col):
    return board[row][col] == 0
```

Hàm này kiểm tra xem ô đã được đánh dấu hay chưa.

- **Kiểm tra đầy bảng**:

```python
def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True
```

Hàm này kiểm tra xem tất cả các ô đã được đánh dấu hay chưa.

### d. Kiểm tra chiến thắng và vẽ đường thắng

```python
def check_win(player):
    # Kiểm tra hàng ngang
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True

    # Kiểm tra hàng dọc
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True

    # Kiểm tra đường chéo
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True

    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True

    return False
```

- Hàm `check_win(player)` kiểm tra cả ba hàng ngang, dọc, và hai đường chéo để xác định liệu người chơi có thắng hay không. Nếu có, nó sẽ gọi các hàm tương ứng để vẽ đường thắng.

### e. Các hàm vẽ đường thắng

```python
def draw_horizontal_winning_line(row, player):
    posY = row * SQUARE_SIZE + SQUARE_SIZE // 2

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, posY), (WIDTH - 15, posY), WIN_LINE_WIDTH)


def draw_vertical_winning_line(col, player):
    posX = col * SQUARE_SIZE + SQUARE_SIZE // 2

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT - 15), WIN_LINE_WIDTH)


def draw_asc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    # Đường chéo từ dưới trái lên trên phải
    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), WIN_LINE_WIDTH)


def draw_desc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    # Đường chéo từ trên trái xuống dưới phải
    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), WIN_LINE_WIDTH)


```

- **Vẽ đường thắng**: Các hàm này vẽ đường kẻ trên màn hình để chỉ ra hàng ngang, dọc hoặc đường chéo mà người chơi đã thắng.

## 5. Hàm khởi động lại trò chơi

```python
def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0
```

- Hàm này đặt lại bảng và làm mới cửa sổ để bắt đầu trò chơi mới.

## 6. Vòng lặp chính của trò chơi

```python
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]  # tọa độ x
            mouseY = event.pos[1]  # tọa độ y

            clicked_row = int(mouseY // SQUARE_SIZE)
            clicked_col = int(mouseX // SQUARE_SIZE)

            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                if check_win(player):
                    game_over = True
                player = player % 2 + 1
                draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:  # Nhấn C để chơi lại
                restart()
                game_over = False
                player = 1

            if event.key == pygame.K_q:  # Nhấn Q để thoát
                pygame.quit()
                sys.exit()

    pygame.display.update()
```

- **Xử lý sự kiện**: Vòng lặp chính kiểm tra sự kiện thoát chương trình (`pygame.QUIT`), nhấn chuột (`pygame.MOUSEBUTTONDOWN`) để đánh dấu ô, và nhấn phím (`pygame.KEYDOWN`) để chơi lại (`C`) hoặc thoát (`Q`).
- **Đánh dấu ô và kiểm tra thắng**: Khi người chơi nhấn chuột, chương trình xác định vị trí ô được nhấn, kiểm tra xem ô đó có trống không, và nếu có thì đánh dấu ô bằng ký hiệu của người chơi hiện tại. Sau đó, nó kiểm tra liệu người chơi có thắng không.
- **Cập nhật cửa sổ**: `pygame.display.update()` cập nhật các thay đổi lên màn hình.

## Tóm lại

Mã này thiết lập và chạy một trò chơi Tic Tac Toe với giao diện đồ họa, cho phép hai người chơi thay phiên nhau chơi bằng cách nhấn chuột để đánh dấu các ô trên bảng. Chương trình kiểm tra xem có người chơi nào thắng hoặc bảng đã đầy hay chưa. Người dùng có thể nhấn `C` để chơi lại và `Q` để thoát khỏi trò chơi.

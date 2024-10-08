import pygame
import random
import time
import math

# Khởi tạo Pygame
pygame.init()

# Thiết lập kích thước màn hình và màu sắc
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 400
GRID_SIZE = 4
TILE_SIZE = SCREEN_WIDTH // GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Các màu và hình dạng
SHAPES = ['circle', 'square', 'triangle', 'hexagon']
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), 
          (255, 0, 255), (0, 255, 255), (128, 0, 128), (128, 128, 0)]

# Thiết lập màn hình
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Memory Matching Game")

# Tạo danh sách hình dạng và màu sắc để khớp
pairs = [(shape, color) for shape in SHAPES for color in COLORS[:2]] * 2
random.shuffle(pairs)

# Tạo lưới ô
grid = [[pairs[GRID_SIZE * row + col] for col in range(GRID_SIZE)] for row in range(GRID_SIZE)]
revealed = [[False] * GRID_SIZE for _ in range(GRID_SIZE)]
first_selection = None
second_selection = None
game_over = False
wait_time = 0

# Hàm vẽ hình dạng
def draw_shape(shape, color, rect):
    center = rect.center
    if shape == 'circle':
        pygame.draw.circle(screen, color, center, TILE_SIZE // 4)
    elif shape == 'square':
        pygame.draw.rect(screen, color, rect.inflate(-TILE_SIZE // 4, -TILE_SIZE // 4))
    elif shape == 'triangle':
        points = [
            (center[0], center[1] - TILE_SIZE // 4),
            (center[0] - TILE_SIZE // 4, center[1] + TILE_SIZE // 4),
            (center[0] + TILE_SIZE // 4, center[1] + TILE_SIZE // 4)
        ]
        pygame.draw.polygon(screen, color, points)
    elif shape == 'hexagon':
        angle = math.pi / 3
        points = [
            (center[0] + TILE_SIZE // 4 * math.cos(angle * i),
             center[1] + TILE_SIZE // 4 * math.sin(angle * i)) for i in range(6)
        ]
        pygame.draw.polygon(screen, color, points)

# Hàm vẽ lưới
def draw_grid():
    screen.fill(WHITE)
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if revealed[row][col]:
                shape, color = grid[row][col]
                pygame.draw.rect(screen, WHITE, rect)
                draw_shape(shape, color, rect)
            else:
                pygame.draw.rect(screen, RED, rect)
            pygame.draw.rect(screen, BLACK, rect, 2)

# Hàm kiểm tra trò chơi kết thúc
def check_game_over():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if not revealed[row][col]:
                return False
    return True

# Vòng lặp game
running = True
while running:
    draw_grid()
    pygame.display.flip()

    if wait_time > 0 and pygame.time.get_ticks() > wait_time:
        first_row, first_col = first_selection
        second_row, second_col = second_selection
        if grid[first_row][first_col] != grid[second_row][second_col]:
            revealed[first_row][first_col] = False
            revealed[second_row][second_col] = False
        first_selection = None
        second_selection = None
        wait_time = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over and wait_time == 0:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            row = mouse_y // TILE_SIZE
            col = mouse_x // TILE_SIZE

            if not revealed[row][col]:
                revealed[row][col] = True

                if first_selection is None:
                    first_selection = (row, col)
                else:
                    second_selection = (row, col)
                    # Cho phép cả 2 ô mở
                    if grid[first_selection[0]][first_selection[1]] != grid[row][col]:
                        # Nếu không khớp, chờ 0.5 giây rồi đóng
                        wait_time = pygame.time.get_ticks() + 500
                    else:
                        # Nếu khớp, giữ cả hai ô mở
                        first_selection = None
                        second_selection = None

                game_over = check_game_over()

# Thoát game
pygame.quit()

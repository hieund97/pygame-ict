import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
FPS = 60
ENEMY_COUNT = 5  # Number of enemies

# Setup display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racing Game")
clock = pygame.time.Clock()

# Player car
player_size = [50, 60]
player_pos = [SCREEN_WIDTH//2, SCREEN_HEIGHT - player_size[1] - 10]
player_speed = 10

# Enemy cars
enemy_size = [50, 50]
enemy_list = []
for _ in range(ENEMY_COUNT):
    enemy_list.append([random.randint(0, SCREEN_WIDTH - enemy_size[0]), -random.randint(0, 500)])

enemy_speed = 5

# Score
score = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            running = False

    # Key press handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < SCREEN_WIDTH - player_size[0]:
        player_pos[0] += player_speed

    # Move enemy cars
    for enemy in enemy_list:
        enemy[1] += enemy_speed
        if enemy[1] > SCREEN_HEIGHT:
            enemy[0] = random.randint(0, SCREEN_WIDTH - enemy_size[0])
            enemy[1] = -random.randint(0, 100)
            score += 1  # Increment score as player dodges an enemy

    # Collision detection
    for enemy in enemy_list:
        if (player_pos[0] < enemy[0] + enemy_size[0] and
            player_pos[0] + player_size[0] > enemy[0] and
            player_pos[1] < enemy[1] + enemy_size[1] and
            player_pos[1] + player_size[1] > enemy[1]):
            running = False  # End game on collision

    # Drawing
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, WHITE, (player_pos[0], player_pos[1], *player_size))
    for enemy in enemy_list:
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], *enemy_size))

    # Display score
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

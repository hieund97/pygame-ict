import random

import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

# Load images
images = []
for i in range(7):
    image = pygame.image.load(f"hangman{i}.png")
    images.append(image)

# Fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)

# Game variables
hangman_status = 0
words = ["PYTHON", "DEVELOPER", "PYGAME", "HANGMAN", "COMPUTER"]
word = random.choice(words)
guessed = []
hint_used = False

# Hint button
hint_button = pygame.Rect(WIDTH - 150, HEIGHT - 70, 100, 50)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Setup game loop
FPS = 60
clock = pygame.time.Clock()
run = True

def draw():
    win.fill(WHITE)
    
    # Draw title
    text = TITLE_FONT.render("HANGMAN", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))
    
    # Draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 300))
    
    # Draw hint button
    pygame.draw.rect(win, BLACK, hint_button, 2)
    hint_text = LETTER_FONT.render("HINT", 1, BLACK)
    win.blit(hint_text, (hint_button.x + (hint_button.width - hint_text.get_width()) / 2, hint_button.y + (hint_button.height - hint_text.get_height()) / 2))
    
    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()

def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

def use_hint():
    global hint_used
    if not hint_used:
        hint_used = True
        unguessed_letters = [letter for letter in word if letter not in guessed]
        if unguessed_letters:
            guessed.append(random.choice(unguessed_letters))

while run:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            
            # Check if hint button is clicked
            if hint_button.collidepoint(m_x, m_y):
                use_hint()
        if event.type == pygame.KEYDOWN:
            if event.unicode.isalpha():
                letter = event.unicode.upper()
                if letter not in guessed:
                    guessed.append(letter)
                    if letter not in word:
                        hangman_status += 1
    
    draw()
    
    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break
    
    if won:
        display_message("YOU WON!")
        break
    
    if hangman_status == 6:
        display_message(f"YOU LOST! The word was {word}")
        break

pygame.quit()

import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Alien Shooter")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Game settings
player_size = 50
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT - 2 * player_size]
alien_size = 50
alien_pos = [random.randint(0, SCREEN_WIDTH - alien_size), 0]
alien_speed = 5
bullet_size = [5, 10]
bullet_speed = 10
bullets = []

# Load images
player_image = pygame.Surface((player_size, player_size))
player_image.fill(WHITE)
alien_image = pygame.Surface((alien_size, alien_size))
alien_image.fill(RED)
bullet_image = pygame.Surface(bullet_size)
bullet_image.fill(WHITE)

# Font
font = pygame.font.SysFont("monospace", 35)

# Game variables
score = 0

def draw_objects():
    screen.fill(BLACK)
    screen.blit(player_image, (player_pos[0], player_pos[1]))
    screen.blit(alien_image, (alien_pos[0], alien_pos[1]))
    for bullet in bullets:
        screen.blit(bullet_image, (bullet[0], bullet[1]))
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    pygame.display.update()

def update_alien():
    global alien_pos, player_pos, score
    alien_pos[1] += alien_speed
    if alien_pos[1] > SCREEN_HEIGHT:
        alien_pos = [random.randint(0, SCREEN_WIDTH - alien_size), 0]
        score -= 1

def update_bullets():
    global bullets, alien_pos, alien_size, alien_speed, score
    for bullet in bullets:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)
        if (alien_pos[0] < bullet[0] < alien_pos[0] + alien_size and
            alien_pos[1] < bullet[1] < alien_pos[1] + alien_size):
            bullets.remove(bullet)
            alien_pos = [random.randint(0, SCREEN_WIDTH - alien_size), 0]
            score += 1

def detect_collision():
    if (player_pos[0] < alien_pos[0] < player_pos[0] + player_size and
        player_pos[1] < alien_pos[1] < player_pos[1] + player_size):
        return True
    return False

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_pos[0] -= 10
            elif event.key == pygame.K_RIGHT:
                player_pos[0] += 10
            elif event.key == pygame.K_SPACE:
                bullets.append([player_pos[0] + player_size // 2, player_pos[1]])

    # Update game state
    update_alien()
    update_bullets()
    if detect_collision():
        print("Game Over!")
        pygame.quit()
        sys.exit()

    draw_objects()
    clock.tick(30)

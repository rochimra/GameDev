import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Subway Surfers Clone')

# Load assets
player_img = pygame.image.load('C:\GitHub\GameDev\TC_Batch_16\Asset\meteor.png')
player_img = pygame.transform.scale(player_img, (50, 50))
background_img = pygame.image.load('C:\GitHub\GameDev\TC_Batch_16\Asset\meteor.png')
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
obstacle_img = pygame.image.load('C:\GitHub\GameDev\TC_Batch_16\Asset\meteor.png')
obstacle_img = pygame.transform.scale(obstacle_img, (50, 50))
coin_img = pygame.image.load('C:\GitHub\GameDev\TC_Batch_16\Asset\meteor.png')
coin_img = pygame.transform.scale(coin_img, (30, 30))

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (100, HEIGHT // 2)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

# Obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = obstacle_img
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = random.randint(50, HEIGHT - 50)

    def update(self):
        self.rect.x -= 7  # Move obstacle left
        if self.rect.right < 0:
            self.kill()

# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = random.randint(50, HEIGHT - 50)

    def update(self):
        self.rect.x -= 5  # Move coin left
        if self.rect.right < 0:
            self.kill()

# Initialize sprite groups
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
coins = pygame.sprite.Group()

# Create player
player = Player()
all_sprites.add(player)

# Game loop
running = True
clock = pygame.time.Clock()
score = 0
while running:
    clock.tick(FPS)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Create obstacles and coins
    if random.randint(1, 30) == 1:
        obstacle = Obstacle()
        all_sprites.add(obstacle)
        obstacles.add(obstacle)

    if random.randint(1, 60) == 1:
        coin = Coin()
        all_sprites.add(coin)
        coins.add(coin)

    # Check collisions
    if pygame.sprite.spritecollide(player, obstacles, False):
        print("Game Over!")
        running = False

    collected_coins = pygame.sprite.spritecollide(player, coins, True)
    score += len(collected_coins)

    # Draw
    screen.blit(background_img, (0, 0))
    all_sprites.draw(screen)

    # Draw score
    font = pygame.font.SysFont(None, 36)
    text = font.render(f'Score: {score}', True, BLACK)
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.flip()

pygame.quit()

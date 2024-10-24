import pygame as pg
import random as ran

# Initialize Pygame
pg.init()
pg.mixer.init()

# Create the game window
WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Dodge The Enemies')

# Load and scale the background image
image = pg.image.load('C:\\GitHub\\GameDev\\TC_Batch_16\\Asset\\jkt48.jpg')
image = pg.transform.scale(image, (800, 600))

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set the game speed
FPS = 60
clock = pg.time.Clock()

# Initialize the highest score variable
highest_score = 0

# Load background music
pg.mixer.music.load("C:\\GitHub\\GameDev\\TC_Batch_16\\Asset\\BGM.wav")
pg.mixer.music.set_volume(0.5)
pg.mixer.music.play(-1)

# Load ship hit rock sound effect
hit_sound = pg.mixer.Sound("C:\\GitHub\\GameDev\\TC_Batch_16\\Asset\\monster2.wav")
hit_sound.set_volume(0.5)

# Player class
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('C:\\GitHub\\GameDev\\TC_Batch_16\\Asset\\ship.png')
        self.image = pg.transform.scale(self.image, (50, 50))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
        self.speed = 5

    def update(self):
        keys = pg.key.get_pressed()
        # Move the player based on keyboard input
        if keys[pg.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pg.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys[pg.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pg.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

# Class for Enemies
class Enemies(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('C:\\GitHub\\GameDev\\TC_Batch_16\\Asset\\meteor.png')
        self.image = pg.transform.scale(self.image, (50, 50))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = ran.randint(0, WIDTH - 50)
        self.rect.y = ran.randint(-100, -50)
        self.speed = ran.randint(2, 6)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.x = ran.randint(0, WIDTH - 75)
            self.rect.y = ran.randint(-100, -50)
            self.speed = ran.randint(2, 6)

# Function to draw text
def draw_text(text, font, color, x, y):
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, (x, y))

# Function to create menu buttons
def draw_button(text, x, y, w, h, inactive_color, active_color, action=None):
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pg.draw.rect(screen, active_color, (x, y, w, h))
        if click[0] == 1 and action is not None:
            action()
    else:
        pg.draw.rect(screen, inactive_color, (x, y, w, h))

    font = pg.font.SysFont(None, 40)
    text_surf = font.render(text, True, WHITE)
    screen.blit(text_surf, (x + (w / 5), y + h / 5))

# Membuat Function start game
def start_game():
    global highest_score

    # Initialize sprite groups
    all_sprites = pg.sprite.Group()
    enemies = pg.sprite.Group()

    # Create player
    player = Player()
    all_sprites.add(player)

    # Create enemies
    for i in range(5):  # 5 enemies at the beginning
        enemy = Enemies()
        all_sprites.add(enemy)
        enemies.add(enemy)

    # Create score, time, and level
    score = 0
    start = pg.time.get_ticks()
    level = 1
    game_over_time = 0  # Initialize game_over_time

    # Loop game
    run = True
    game_over = False
    while run:
        clock.tick(FPS)

        # Close the game if 'x' is pressed
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        # Level up logic
        if score >= 10 * level:
            level += 1
            for i in range(5):
                enemy = Enemies()
                enemy.speed = ran.randint(2 + level, 6 + level)
                all_sprites.add(enemy)
                enemies.add(enemy)

        # Game over logic
        if not game_over:
            # Update all sprites
            all_sprites.update()

        # Check if the player hits an enemy
        hits = pg.sprite.spritecollide(player, enemies, False)
        if hits:
            hit_sound.play()
            game_over = True
            game_over_time = (pg.time.get_ticks() - start) // 1000  # Calculate survival time score

        # Update highest score
        if game_over_time > highest_score:
            highest_score = game_over_time

        # Calculate final score
        score = (pg.time.get_ticks() - start) // 1000

        # Display background
        screen.blit(image, (0, 0))

        # Draw objects
        all_sprites.draw(screen)

        # Display score
        font = pg.font.SysFont(None, 30)
        text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(text, (10, 10))

        # Display level
        font = pg.font.SysFont(None, 30)
        text = font.render(f"Level: {level}", True, WHITE)
        screen.blit(text, (10, 30))

        # Display game over and highest score
        if game_over:
            over_text = font.render(f"Game Over! Your Best Score: {highest_score}", True, WHITE)
            screen.blit(over_text, (WIDTH // 2 - 150, HEIGHT // 2))

            # Draw restart game button
            draw_button("Restart Game", WIDTH // 3, HEIGHT // 3 + 150, 250, 60, BLUE, RED, start_game)

        # Update display
        pg.display.flip()

    pg.quit()

# Create main menu function
def main_menu():
    menu = True
    while menu:
        # Display background
        screen.blit(image, (0, 0))

        # Display game title
        font = pg.font.SysFont(None, 70)
        draw_text("Dodge The Enemies", font, WHITE, WIDTH // 4, HEIGHT // 4)

        # Display start button
        draw_button("Start Game", WIDTH // 3, HEIGHT // 3, 200, 60, BLUE, RED, start_game)

        # Close game if 'x' is pressed
        for event in pg.event.get():
            if event.type == pg.QUIT:
                menu = False

        pg.display.update()
        clock.tick(15)

# Start the program
if __name__ == '__main__':
    main_menu()

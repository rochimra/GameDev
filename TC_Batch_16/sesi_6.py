import pygame as pg
import random as ran

# Inisialisasi pygame
pg.init()

# Membuat jendela game
WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Dodge The Enemies')

# Image Sebagai Background
image = pg.image.load('C:\GitHub\GameDev\TC_Batch_16\Asset\jkt48.jpg')
image = pg.transform.scale(image,(800,600))

# Warna
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)

# Kecepatan game
FPS = 60
clock = pg.time.Clock()

# Class untuk Player
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((50,50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
        self.speed = 5

    def update(self):
        keys = pg.key.get_pressed()
        # Kondisi jika kita gerakan objek atas bawah kiri kanan
        if keys[pg.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pg.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys[pg.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pg.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

# Class untuk Enemies
class Enemies (pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((50,50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = ran.randint(0, WIDTH - 75)
        self.rect.y = ran.randint(-100,-50)
        self.speed = ran.randint(10,15)
    
    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.x = ran.randint(0, WIDTH - 75)
            self.rect.y = ran.randint(-100,-50)
            self.speed = ran.randint(2,6)

# Inisialisasi Sprite Group Enemy
all_sprites = pg.sprite.Group()
enemies = pg.sprite.Group()

# Membuat Player
player = Player()
all_sprites.add(player)

# Membuat Enemies
for i in range(5): # Ada 5 musuh di awal
    enemy = Enemies()
    all_sprites.add(enemy)
    enemies.add(enemy)

# Membuat Score
score = 0
start = pg.time.get_ticks()

# Loop Game
run = True
game_over = False
while run:
    clock.tick(FPS)

    # Menutup game jika tekan x
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    # Logika Game Over
    if not game_over:
        # Update semua sprites
        all_sprites.update()

        # Mengecek apakah player hit enemies
        hits = pg.sprite.spritecollide(player, enemies, False)
        if hits:
            game_over = True
            game_over_time = (pg.time.get_ticks() - start) // 1000 # Menghitung waktu bertahan hidup

        # Menghitung Score Akhir
        score = (pg.time.get_ticks()-start) // 1000

    # Menampilakan background
    screen.blit(image, (0,0))

    # Menggambar objek
    all_sprites.draw(screen)
    
    # Menampilkan score
    font = pg.font.SysFont(None,30)
    text = font.render(f"score: {score}", True, WHITE)
    screen.blit(text, (10,10))

    # Menampilkan game over
    if game_over:
        over_text = font.render(f"Game Over! Final Score: {game_over_time}", True, WHITE)
        screen.blit(over_text, (WIDTH // 2 - 150, HEIGHT // 2))

    # Update tampilan layar
    pg.display.flip()
    pg.display.update() 
    
pg.quit()
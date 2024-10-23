import pygame as pg
import random as ran

# Inisialisasi pygame
pg.init

# Membuat jendela game
WIDTH = 800
HEIGHT = 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Dodge The Enemies')

# Image Sebagai Background
image = pg.image.load('path')
image = pg.transform.scale((800,600))

# Warna
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)

# Kecepatan game
FPS = 60
clock = pg.time.Clock()

# Kelas untuk player
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

# Inisialisasi Sprite Game
all_sprites = pg.sprite.Group()

# Membuat Player
player = Player()
all_sprites.add(player)

# Loop Game
run = True
while run:
    # Menutup game jika tekan x
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    # Menampilakan background
    screen.blit(image, (0,0))

    # Menggambar objek
    all.sprite


pg.quit()
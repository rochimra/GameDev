# pygame
import pygame as pg
# print(pygame.__version__)

pg.init
screen = pg.display.set_mode((800,600))
pg.display.set_caption('My First Game')

# Tambah Image
image = pg.image.load('C:\\Users\RAJASA\Documents\GameDev\jkt48.jpg')
image = pg.transform.scale(image, (200,200))

# loop game
run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    # White Background
    screen.fill((255,255,255))
    
    # Menampilkan Gambar
    screen.blit(image,(0,0))

    # Update Tampilan Layar
    pg.display.update()

pg.QUIT()
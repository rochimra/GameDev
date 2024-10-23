# pygame
import pygame as pg
# print(pygame.__version__)

pg.init
screen = pg.display.set_mode((800,600))
pg.display.set_caption('My First Game')

# Tambah Image
image = pg.image.load('C:\GitHub\GameDev\Asset\jkt48.jpg')
image = pg.transform.scale(image, (800,600))

# Menginisialisasi posisi dan ukuran persegi
rect_x = 100
rect_y = 100
rect_width = 20
rect_height = 15
# RectPosSize = rect_x, rect_y, rect_width, rect_height

# Menginisialisasi warna persefi
rect_color = (0,0,255) # Warna biru
speed = 1
rectangle_drawn = False

# loop game
run = True
while run:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    # Menerima input dari mouse
    mouse_x, mouse_y = pg.mouse.get_pos() # Untuk mendapat posisi kursos mouse
    mouse_buttons = pg.mouse.get_pressed() # Untuk mendeteksi left click mouse

    # Menentukan kondisi jika leftclick memunculkan objek (persegi panjang)
    if mouse_buttons[0]: # 0 untuk left clic, 1 untuk scroll click, 2 untuk right click
        if not rectangle_drawn:
            rect_x, rect_y = mouse_x - rect_width//2, mouse_y - rect_height//2
            rectangle_drawn = True
        else:
            pass
        
    # Membuat objek berubah warna
    elif mouse_buttons[2]:
        # if (rect_x <= mouse_x <= rect_width + rect_x) and (rect_y <= mouse_y <= rect_height + rect_y):
        if rectangle_drawn:
            rect_color = (255,0,0) # Merubah Objek menjadi merah
    
    # Membuat kondisi jika tombol keyboard ditekan atas, bawah
    keys = pg.key.get_pressed()
    if rectangle_drawn:
        if keys [pg.K_UP]:
            rect_y -= speed
        if keys [pg.K_DOWN]:
            rect_y += speed
        if keys [pg.K_LEFT]:
            rect_x -= speed
        if keys [pg.K_RIGHT]:
            rect_x += speed


    # # White Background
    # screen.fill((255,255,255))
    
    # Menampilkan Gambar
    screen.blit(image,(0,0))

    if rectangle_drawn:
        pg.draw.rect(screen, (rect_color), (rect_x, rect_y, rect_width, rect_height))

    # Update Tampilan Layar
    pg.display.update()

pg.QUIT()
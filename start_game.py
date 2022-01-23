import pygame
from Classes.Lawnmower import  Lawnmower
from Classes.Grass import Grass

pygame.init()

run = True
clock = pygame.time.Clock()


win = pygame.display.set_mode((800, 600))
lawnmower = Lawnmower(200,300)
grass = Grass(800,600)

def draw_window(win):
    win.fill((255,255,255))
    grass.draw(win)
    lawnmower.draw(win)
    pygame.display.update()

while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        run = False
    if keys[pygame.K_UP]:
        lawnmower.move(0)
    if keys[pygame.K_DOWN]:
        lawnmower.move(1)
    if keys[pygame.K_LEFT]:
        lawnmower.move(2)
    if keys[pygame.K_RIGHT]:
        lawnmower.move(3)

    lawnmower.cut(grass)

    draw_window(win)

print ("done")
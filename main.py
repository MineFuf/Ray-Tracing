import pygame as pg
from settings import *
from ray import *
borders = []
for b in range(BORDER_COUNT):
    borders.append(Border())
borders.append(Game_Border(Coordinates(0, 0), Coordinates(WIDTH, 0)))
borders.append(Game_Border(Coordinates(0, 0), Coordinates(0, HEIGHT)))
borders.append(Game_Border(Coordinates(WIDTH, 0), Coordinates(WIDTH, HEIGHT)))
borders.append(Game_Border(Coordinates(0, HEIGHT), Coordinates(WIDTH, HEIGHT)))


while True:
    clock.tick(FPS)
    pg.display.set_caption("{:.2f}".format(clock.get_fps()))
    for e in pg.event.get():
        if e.type == pg.QUIT:
            print('Good bye.')
            exit()

    keys = pg.key.get_pressed()
    if keys[pg.K_ESCAPE]:
        print('Good bye.')
        exit()

    x, y = pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]
    rays = []
    for dir in range(RAYS_COUNT):
        rays.append(Ray(dir * (360 / RAYS_COUNT), borders, Coordinates(x, y)))

    screen.fill((32, 32, 32))
    for b in borders:
        b.draw(screen)
    for r in rays:
        r.draw(screen)

    pg.display.flip()

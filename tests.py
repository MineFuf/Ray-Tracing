import pygame as pg

win = pg.display.set_mode((512, 512))
while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            exit()
    print(pg.mouse.get_pos())
    pg.display.update()

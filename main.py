import pygame as pg
from settings import *
from vector import *
from colors import *
clrs = Colors()

vec1rot = 0
vec2rot = 90

vec1l = 100
vec2l = 100


while True:
    clock.tick(FPS)
    for e in pg.event.get():
        if e.type == pg.QUIT:
            exit()

    keys = pg.key.get_pressed()
    if keys[pg.K_UP]:
        vec2rot += 1
    if keys[pg.K_DOWN]:
        vec2rot -= 1
    if keys[pg.K_RIGHT]:
        vec2l += 1
    if keys[pg.K_LEFT]:
        vec2l -= 1

    if keys[pg.K_w]:
        vec1rot += 1
    if keys[pg.K_s]:
        vec1rot -= 1
    if keys[pg.K_d]:
        vec1l += 1
    if keys[pg.K_a]:
        vec1l -= 1

    if vec2rot > 360: vec2rot -= 360
    if vec2rot < 0: vec2rot += 360

    screen.fill(clrs.DARK_GREY)
    vec1 = Vector(vec(vec1l, 0).rotate(-vec1rot), clrs.RED, START_POS)
    vec2 = Vector(vec(vec2l, 0).rotate(-vec2rot),  clrs.BLUE, START_POS)
    # vec3 = Vector(vec(200, 0).rotate(-90), clrs.YELLOW, START_POS)
    last_vec = Vector(vec1.v + vec2.v,  clrs.GREEN, START_POS)

    vec1.draw(screen)
    vec2.draw(screen)
    # vec3.draw(screen)
    last_vec.draw(screen)

    pg.display.flip()

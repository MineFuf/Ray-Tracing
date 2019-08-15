from random import randint
from settings import *
import pygame as pg
from math import pow, sqrt
vec = pg.math.Vector2


class Ray:
    def __init__(self, dir, borders, pos):
        self.dir = dir
        self.borders = borders
        self.pos = pos
        self.pos2 = self.pos2_pos()

    def pos2_pos(self):
        v = vec(1, 0).rotate(self.dir)
        coo = Coordinates(v.x + self.pos.x, v.y + self.pos.y)
        spos = None
        for b in self.borders:
            inf = True
            ans = self.try_border(b, coo)
            # print('Spos is {}'.format(spos))
            # print('Ans is {}'.format(ans))
            if ans is not None:
                if spos is None:
                    spos = ans
                else:
                    l_original = self.lenght(self.pos, spos)
                    l_new = self.lenght(self.pos, ans)
                    if min(l_original, l_new) == l_original:
                        pass
                    elif min(l_original, l_new) < l_original:
                        spos = ans
                        # print('Previous: {}, New: {}'.format(l_original, l_new))
        return spos

    def lenght(self, point1, point2):
        x = point1.x - point2.x
        y = point1.y - point2.y
        l = sqrt(pow(x, 2) + pow(y, 2))
        return l

    def try_border(self, border, coo):
        # Try if lines are parael
        x1, y1 = self.pos.x, self.pos.y
        x2, y2 = coo.x, coo.y
        x3, y3 = border.pos.x, border.pos.y
        x4, y4 = border.pos2.x, border.pos2.y
        d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        # print(d)
        if d == 0:
            # print('D is 0')
            return None
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / d
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / d
        if t >= 0 and 0 <= u <= 1:
            Px, Py = x1 + t * (x2 - x1), y1 + t * (y2 - y1)
            return Coordinates(Px, Py)
        else:
            return None

    def draw(self, sur):
        pg.draw.line(sur, (255, 128, 0), (self.pos.x, self.pos.y),
                     (self.pos2.x, self.pos2.y))


class Border:
    def __init__(self):
        self.pos = self.gen_random()
        self.pos2 = self.gen_random()

    def draw(self, sur):
        pg.draw.line(sur, (255, 255, 255), (self.pos.x, self.pos.y),
                     (self.pos2.x, self.pos2.y))

    def gen_random(self):
        coo = Coordinates(randint(0, WIDTH), randint(0, HEIGHT))
        # print('{}:{}'.format(coo.x, coo.y))
        return coo

class Game_Border:
    def __init__(self, first, second):
        self.pos = first
        self.pos2 = second

    def draw(self, sur):
        pg.draw.line(sur, (255, 255, 255), (self.pos.x, self.pos.y),
                     (self.pos2.x, self.pos2.y))

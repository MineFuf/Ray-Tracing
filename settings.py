from pygame import display, time
from math import pow


# Class Coordinates for simplifiing workflow :-)
class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Define some variables
FPS = 120
WIDTH = int(512 * 1.5)
HEIGHT = int(512 * 1)
BORDER_SIZE_COUNT = 15
BORDER_COUNT = int((WIDTH * HEIGHT) / pow(512, 2) * BORDER_SIZE_COUNT)
RAYS_COUNT = 360
screen = display.set_mode((WIDTH, HEIGHT))
clock = time.Clock()

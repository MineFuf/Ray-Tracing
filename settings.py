<<<<<<< current
from pygame import display, time


# Class Coordinates for simplifiing workflow :-)
class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Define some variables
FPS = 60
WIDTH = int(512 * 1.5)
HEIGHT = int(512 * 1)
START_POS = Coordinates(32, HEIGHT / 2)
screen = display.set_mode((WIDTH, HEIGHT))
clock = time.Clock()

# Define colors
=======
from pygame import display, time


# Class Coordinates for simplifiing workflow :-)
class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Define some variables
FPS = 60
WIDTH = int(512 * 1.5)
HEIGHT = int(512 * 1)
START_POS = Coordinates(32, HEIGHT / 2)
screen = display.set_mode((WIDTH, HEIGHT))
clock = time.Clock()

# Define colors
>>>>>>> before discard

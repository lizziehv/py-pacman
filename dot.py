# Dot Class for pac-man

from cs1lib import *


class Dot:

    def __init__(self, x_coordinate, y_coordinate):
        self.x = x_coordinate
        self.y = y_coordinate
        self.r = 1
        self.g = 1
        self.b = 1
        self.eaten = False

    def draw(self):
        set_stroke_color(self.r, self.g, self.b)
        set_fill_color(self.r, self.g, self.b)
        draw_rectangle(self.x - 2, self.y - 2, 4, 4)

    def change_color(self):
        self.r = 0
        self.b = 0
        self.g = 0
        self.eaten = True

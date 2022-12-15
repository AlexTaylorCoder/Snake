from turtle import Turtle
from random import randint

WIDTH = 800
HEIGHT = 800
PADDING = 30
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(0.5,0.5)
        self.color("red")
        self.goto(*self.rand_coords())
    def move(self):
        self.goto(*self.rand_coords())
    def rand_coords(self):
        return (randint(PADDING,WIDTH // 2 - PADDING),randint(PADDING,HEIGHT // 2 - PADDING))
    # def __del__(self):



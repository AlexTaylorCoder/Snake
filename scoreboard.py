from turtle import Turtle

FONT_FAMILY = ("Arial",32,"normal")
WIDTH = 800
HEIGHT = 800
PADDING = 70

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.pu()
        self.goto(0, HEIGHT // 2 - PADDING)
        self.color("white")
        self.hideturtle()
        self.write(self.count, font = FONT_FAMILY, align="center")
    def update(self):
        self.clear()
        self.count += 1
        self.write(self.count, font= FONT_FAMILY)
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", font = FONT_FAMILY, align="center")
        
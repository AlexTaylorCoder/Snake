from turtle import Turtle

FONT_FAMILY = ("Arial",22,"normal")
WIDTH = 800
HEIGHT = 800
PADDING = 70

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        with open("stats.txt") as file:
            content = file.read()
            self.highscore = int(content)
        self.pu()
        self.color("white")
        self.hideturtle()
        self.draw()
    def update(self):
        self.count += 1
        self.draw()
    def draw(self):
        self.clear()
        self.goto(40, HEIGHT // 2 - PADDING)
        self.write(f'Score: {self.count} Highscore: {self.highscore}', font = FONT_FAMILY, align="center")
    def game_over(self):
        if self.count > self.highscore:
            self.highscore = self.count
            with open("stats.txt","w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.draw()
        
    
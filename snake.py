from turtle import Turtle
from food import Food

WIDTH = 800
HEIGHT = 800
PADDING = 30
DIST = 10
BUFFER = 20
class Snake():
    def __init__(self):
        self.seg = []
        for n in range(3):
            t = Turtle("square")
            t.pu()
            t.color("white")
            t.goto(n * 20,0)
            self.seg.append(t)
    def add_seg(self,x,y):
        t = Turtle("square")
        t.pu()
        t.color("white")
        t.goto(x,y)
        self.seg.append(t)
    def move(self,pellet,score):
        for i in range(len(self.seg)-1,0,-1):
            new_x = self.seg[i-1].xcor()
            new_y = self.seg[i-1].ycor()
            self.seg[i].goto(new_x,new_y)
        self.head = self.seg[0]
        self.head.forward(DIST)
        return self.collision(pellet,score)
    def collision(self,pellet,score):
        #Could also use .distance(pellet), may consider refactoring collision and adding to main
        x, y = self.head.xcor(), self.head.ycor()
        if (x - BUFFER < pellet.xcor() < x + BUFFER) and y - BUFFER < pellet.ycor() < y + BUFFER:
            self.add_seg(x,y)
            pellet.move()
            score.update()
        elif x == WIDTH // 2 or y == HEIGHT // 2:
            score.game_over()
            return False
        else:
            for i in range(1,len(self.seg)):
                if self.seg[i].xcor() == x and self.seg[i].ycor() == y:
                    score.game_over()
                    return False
        


        
from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score


width = 800
height = 800
padding = 30

s = Screen()
s.setup(width,height)
s.bgcolor("black")
s.tracer(0)
s.title("snake")

score = Score()
pellet = Food()
snake = Snake()
seg = snake.seg

s.update()
s.listen()
        
flag = True
while flag:

    if snake.move(pellet,score) is False:
        break
    head = snake.head
    print(head.heading())
    if head.heading() != 270:
        s.onkey(lambda: head.setheading(90) ,"w")
    if head.heading() != 90:
        s.onkey(lambda: head.setheading(270),"s")
    if head.heading() != 180:
        s.onkey(lambda: head.setheading(0),"d")
    if head.heading() != 0:
        s.onkey(lambda: head.setheading(180),"a")



    s.update()
    time.sleep(.04)
s.exitonclick()
        



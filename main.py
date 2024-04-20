from turtle import Turtle
from random import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("coral")
timmy.speed(10)

# Drawing initial shape. In here, we draw a solid square.
# Therefore, the square is expected to be the main character/part of the drawing.
for _ in range(4):
    timmy.forward(100)
    timmy.left(90)

# Drawing random lines
for _ in range(100):
    steps = int(random() * 100)
    angle = int(random() * 360)
    timmy.right(angle)
    timmy.forward(steps)


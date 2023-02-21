import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y = random.randint(0, 280)

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=2, stretch_len=1)

        self.left(90)

    def go_left(self):
        self.goto(300, Y)
        self.goto(-350, Y)

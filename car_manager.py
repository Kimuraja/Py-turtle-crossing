import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y = random.randint(0, 260)

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(300, Y)
        self.left(180)

    def go_left(self):

        self.fd(10)

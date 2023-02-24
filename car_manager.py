import random
from turtle import Turtle
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.STARTING_MOVE_DISTANCE = 5
        self.pu()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.left(180)
        self.goto(x=280, y=random.randint(-280, 280))

    def generate_car(self):
        i = Turtle("square")
        i.STARTING_MOVE_DISTANCE = 5
        i.pu()
        i.shapesize(stretch_wid=1, stretch_len=2)
        i.color(random.choice(COLORS))
        i.left(180)
        i.goto(x=280, y=random.randint(-280, 280))

    def move(self):
        self.fd(self.STARTING_MOVE_DISTANCE)

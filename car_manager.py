import random
from turtle import Turtle
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


# TODO, Slow down cars !

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.segment = []

    def new_car(self):
        new = Turtle("square")
        new.left(180)
        new.pu()
        new.shapesize(stretch_wid=1, stretch_len=2)
        new.color(random.choice(COLORS))
        new.goto(320, random.randint(-250, 250))
        # for _ in range(len(COLORS)):
        self.segment.append(new)

    def move(self):
        for i in range(0, len(self.segment), 5):
            self.segment[i].fd(STARTING_MOVE_DISTANCE)

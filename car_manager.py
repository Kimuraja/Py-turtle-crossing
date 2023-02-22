import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
X = 280



class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.segment = []
        self.generate_more_cars()

    def generate_more_cars(self):
        for _ in COLORS:
            self.new_car()

    def new_car(self):
        new = Turtle()
        new.shape("square")
        new.pu()
        new.shapesize(stretch_wid=1, stretch_len=2)
        new.color(random.choice(COLORS))
        new.goto(X, random.randint(-260, 260))
        self.segment.append(new)

    def move(self):
        for seg_num in range(0, len(self.segment)):
            self.segment[seg_num].goto(X, random.randint(-260, 260))
        self.segment[0].forward(MOVE_INCREMENT)

from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []

    def create_car(self):
        rand_chance = random.randint(1, 6)
        if rand_chance == 1:
            i = Turtle("square")
            i.pu()
            i.shapesize(stretch_wid=1, stretch_len=2)
            i.color(random.choice(COLORS))
            i.left(180)
            i.goto(x=280, y=random.randint(-250, 250))
            self.all_cars.append(i)

    def move_car(self):
        for i in range(0, len(self.all_cars)):
            self.all_cars[i].fd(STARTING_MOVE_DISTANCE)

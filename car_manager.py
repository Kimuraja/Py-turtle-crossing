import random
from turtle import Turtle

COLORS = ["#005f73", "#ee9b00", "#ae2012", "#0a9396", "#e9d8a6", "#ca6702"]


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.STARTING_MOVE_DISTANCE = 5

    def create_car(self):
        rand_chance = random.randint(1, 2)
        if rand_chance == 1:
            i = Turtle("square")
            i.color("#001219")
            i.shapesize(stretch_wid=1, stretch_len=2)
            i.pu()
            i.color(random.choice(COLORS))
            i.left(180)
            i.goto(x=280, y=random.randint(-250, 250))
            self.all_cars.append(i)

    def move_car(self):
        for car in self.all_cars:
            car.fd(self.STARTING_MOVE_DISTANCE)

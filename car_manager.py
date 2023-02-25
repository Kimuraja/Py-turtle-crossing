import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.STARTING_MOVE_DISTANCE = 5

    def create_car(self):
        rand_chance = random.randint(1, 2)
        if rand_chance == 1:
            i = Turtle("square")
            i.shapesize(stretch_wid=1, stretch_len=2)
            i.pu()
            i.color(random.choice(COLORS))
            i.left(180)
            i.goto(x=280, y=random.randint(-250, 250))
            self.all_cars.append(i)

    def move_car(self):
        for car in self.all_cars:
            car.fd(self.STARTING_MOVE_DISTANCE)

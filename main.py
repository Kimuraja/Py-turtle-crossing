import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


p = Player()
s = Screen()
s.setup(width=600, height=600)
s.tracer(0)
s.bgcolor("#edf2f4")
car = CarManager()
p.starting_position()

s.listen()
s.onkeypress(p.move, "Up")

game_is_on = True
while game_is_on:
    s.update()
    car.generate_more_cars()
    car.move()
    time.sleep(0.1)

s.exitonclick()
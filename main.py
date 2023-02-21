import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

car = CarManager()
p = Player()
s = Screen()
s.setup(width=600, height=600)
s.tracer(0)

p.starting_position()

s.listen()
s.onkeypress(p.move, "Up")

game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.1)
    # car.go_left()
    # if car.xcor() < -320:
    #     game_is_on = False



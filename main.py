import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

score = Scoreboard()
p = Player()
s = Screen()
s.setup(width=600, height=600)
s.tracer(0)
s.bgcolor("#edf2f4")
car = CarManager()
p.starting_position()
# new = car.add_segment()
s.listen()
s.onkeypress(p.move, "Up")

game_is_on = True
while game_is_on:
    s.update()
    car.generate_car()
    time.sleep(0.1)
    score.update_scoreboard()
    car.move()

    if p.ycor() == 290:
        p.reset_game()
        car.STARTING_MOVE_DISTANCE += 10
        score.increase_score()

    if car.distance(p) < 20:
        score.game_over()
        game_is_on = False

s.exitonclick()

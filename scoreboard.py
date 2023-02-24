from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("#2d3142")
        self.hideturtle()
        self.clear()
        self.pu()
        self.goto(0, 260)
        self.num = 0

    def increase_score(self):
        self.num += 1

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f'Score: {self.num}', move=False, align='center', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg='GAME OVER', move=False, align='center', font=FONT)
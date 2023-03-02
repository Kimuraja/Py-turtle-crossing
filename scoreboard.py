from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("#2d3142")
        with open("data.txt", mode="r") as file:
            self.high_score = file.read()
        self.hideturtle()
        self.clear()
        self.pu()
        self.goto(0, 260)
        self.num = 0

    def increase_score(self):
        self.num += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f'Score: {self.num} High Score: {self.high_score}', move=False, align='center', font=FONT)

    def game_over(self):
        if self.num > int(self.high_score):
            self.high_score = self.num
            with open("data.txt", mode="w") as file:
                scr = str(self.high_score)
                file.write(scr)
        self.goto(0, 0)
        self.write(arg='GAME OVER', move=False, align='center', font=FONT)
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-150, 200)
        self.write(f"trip_master: {self.l_score}", align="center", font=("Courier", 24, "normal"))
        self.goto(150, 200)
        self.write(f"alla_ket_master: {self.r_score}", align="center", font=("Courier", 24, "normal"))

    def increase_l_score(self):
        self.l_score += 1
        self.update_scoreboard()

    def increase_r_score(self):
        self.r_score += 1
        self.update_scoreboard()
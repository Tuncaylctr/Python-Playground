from turtle import Turtle


# comments about paths
# / is basically the root directory
# when using relative path instead of absolute path, we can use ./ to indicate the current directory
# ../  if we want to go up one level in the directory structure
# u can doo multiple ../ to go up multiple levels

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("/Users/macbook/Desktop/Python-Playground/project-snake-game/data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg = f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("/Users/macbook/Desktop/Python-Playground/project-snake-game/data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
        # def game_over(self):
        #     self.goto(0, 0)
        #     self.write(arg = "GAME OVER", move=False, align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        
from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-200, 270)
        self.level = 0
        self.score()

    def score(self):
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.level += 1
        self.score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

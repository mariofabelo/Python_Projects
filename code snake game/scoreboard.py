from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = ("Arial", 24, "normal"))


    def update(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align = "center", font = FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)


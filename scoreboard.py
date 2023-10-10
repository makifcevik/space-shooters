from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update()

    def increase(self):
        self.score += 1
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f"score: {self.score}", font=FONT, align=ALIGNMENT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER!", align=ALIGNMENT, font=FONT)

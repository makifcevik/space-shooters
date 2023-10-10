from turtle import Turtle


SPEED = 1
SCALE = 0.45


class Bullet(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=SCALE, stretch_len=SCALE)
        self.color("green")
        self.speed("fastest")

    def move(self):
        self.setheading(90)
        self.forward(SPEED)

        if self.ycor() > 300:
            self.hideturtle()
            return

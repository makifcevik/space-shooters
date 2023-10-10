from turtle import Turtle
from bullet import Bullet

SCALE = 2
SPEED = 30


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.left(90)
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=SCALE, stretch_len=SCALE)
        self.speed("fastest")
        self.goto(x=0, y=-250)
        self.bullets = []

    def move_left(self):
        x = self.xcor()
        x -= SPEED
        if x <= -220:
            x = -220
        self.goto(x, self.ycor())

    def move_right(self):
        x = self.xcor()
        x += SPEED
        if x >= 220:
            x = 220
        self.goto(x, self.ycor())

    def shoot(self):
        bullet = Bullet()
        bullet.setx(self.xcor())
        bullet.sety(self.ycor() + 30)
        bullet.showturtle()
        bullet.move()
        self.bullets.append(bullet)

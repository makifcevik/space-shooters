from turtle import Turtle
import random

MIN_SIZE = 15
MAX_SIZE = 40
MIN_VELOCITY = 2
MAX_VELOCITY = 12


class Asteroid(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shapes = ["circle", "square", "triangle"]
        self.colors = ["blue", "grey", "purple", "pink", "green", "yellow", "cyan"]

        # assign random velocity
        self.velocity = random.randint(MIN_VELOCITY, MAX_VELOCITY) / 10

        # assign random shape and color
        random_index = random.randint(0, len(self.shapes) - 1)
        self.shape(self.shapes[random_index])
        random_index = random.randint(0, len(self.colors) - 1)
        self.color(self.colors[random_index])

        # assign random size
        rand_w = random.randint(MIN_SIZE, MAX_SIZE) / 10
        rand_h = random.randint(MIN_SIZE, MAX_SIZE) / 10
        self.shapesize(stretch_wid=rand_w,stretch_len= rand_h)

        self.penup()
        self.speed("fastest")

        # assign random horizontal position
        rand_x = random.randint(-200, 200)
        self.goto(x=rand_x, y=330)
        self.showturtle()

    def move(self):
        self.setheading(270)
        self.forward(self.velocity)

        if self.ycor() < -300:
            self.hideturtle()
            return

from turtle import Screen
from player import Player
from asteroid import Asteroid
from scoreboard import Scoreboard
import time

WIDTH = 500
HEIGHT = 600

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("Space Invaders")
screen.bgcolor("black")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

# player input
screen.listen()
screen.onkeypress(key="Left", fun=player.move_left)
screen.onkeypress(key="Right", fun=player.move_right)
screen.onkey(key="space", fun=player.shoot)
screen.onkey(key="Escape", fun=screen.bye)

current_time = time.time()
game_over = False
asteroids = []
spawn_cycles = 0


# remove the bullets that are out of border and move the others
def move_bullets():
    for bullet in player.bullets:
        if not bullet.isvisible():
            player.bullets.remove(bullet)
        else:
            bullet.move()


def initialize_asteroids():
    global current_time
    global game_over
    global spawn_cycles

    # spawn asteroids
    spawn_time = 2 - spawn_cycles / 20
    if spawn_time < 0.4:
        spawn_time = 0.4
    if time.time() - current_time > spawn_time:
        current_time = time.time()
        asteroid = Asteroid()
        asteroids.append(asteroid)
        spawn_cycles += 1

    # remove the asteroids that are out of border and move the others
    for asteroid in asteroids:
        if not asteroid.isvisible():
            asteroids.remove(asteroid)
        else:
            asteroid.move()

        # blow up asteroids
        for bullet in player.bullets:
            if bullet.distance(asteroid) < 40:
                asteroid.goto(asteroid.xcor(), -350)
                asteroid.hideturtle()
                scoreboard.increase()

        # ship crashed state
        if player.distance(asteroid) < 30:
            scoreboard.game_over()
            game_over = True


# game loop
while not game_over:
    screen.update()
    move_bullets()
    initialize_asteroids()

screen.exitonclick()

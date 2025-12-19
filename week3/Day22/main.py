# xuv9rsd8maid
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
screen = Screen()
turtle = Turtle()

# this block sets up the screen
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Clone")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
#  These are the controls for the right paddle
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
# these are the controls for the Left Paddle
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()
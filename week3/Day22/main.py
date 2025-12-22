# xuv9rsd8maid
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
from week3.Day22.scoreboard import Scoreboard

screen = Screen()
turtle = Turtle()
scoreboard: Scoreboard = Scoreboard()

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
    time.sleep(0.01)
    screen.update()
    ball.move()
    scoreboard.write_score()

#     Detect collision with the wall
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

#     hitting the right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

#     reset the ball
    if ball.xcor() > 380 or ball.xcor() < -380:
        if ball.xcor() > 380:
            scoreboard.score_p1 += 1
        elif ball.xcor() < -380:
            scoreboard.score_p2 += 1
        ball.reset()

#     Detect a Winner
    if scoreboard.detect_winner():
        game_is_on = False


screen.exitonclick()
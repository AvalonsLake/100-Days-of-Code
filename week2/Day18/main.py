import turtle as t
import random

adam = t.Turtle()
t.colormode(255)

colors = [(133, 164, 202), (225, 150, 101), (30, 43, 64),(201, 136, 148), (163, 59, 49), (236, 212, 88), (44, 101, 147), (136, 181, 161), (148, 64, 72), (51, 41, 45),(161, 32, 29), (60, 115, 99), (59, 48, 45), (170, 29, 32), (215, 83, 73), (236, 167, 157)]


adam.hideturtle()
adam.speed(0)
adam.penup()
for i in range(100):
    if i % 10 == 0:
        adam.goto(-230, -235 + (i * 5))
    adam.color(random.choice(colors))
    adam.dot(20)
    adam.penup()
    adam.forward(50)


t.Screen().exitonclick()
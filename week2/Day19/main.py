from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle wil win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
starting_positions = [-90, -50, -10, 30, 70, 110]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle",)
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=starting_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You Won! {winning_color} turtle won the race!")
            else:
                print(f"You Lost! {winning_color} turtle won the race!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
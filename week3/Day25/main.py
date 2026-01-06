import turtle
import pandas

screen = turtle.Screen()
scoreboard = turtle.Turtle()

screen.title("U.S States game")
image = "blank_states_img.gif"
screen.bgcolor("black")
screen.addshape(image)
turtle.shape(image)

states_named = 0
scoreboard.color("white")
scoreboard.hideturtle()
scoreboard.penup()
scoreboard.goto(-35, 250)


data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
print(state_list)

known_states = []

game_is_on = True
while game_is_on:
    scoreboard.clear()
    scoreboard.write(f"{states_named}/50", font=("Arial", 24, "normal"))
    if states_named == 50:
        game_is_on = False
    answer_state = screen.textinput(title="Guess the State!", prompt="What's another state's name?").title()
    print(answer_state)

    if answer_state in state_list:

        known_states.append(answer_state)

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
        states_named += 1

    if answer_state == "Exit":
        game_is_on = False
        states_to_learn = [state for state in state_list if state not in known_states]
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")



# listing the states to learn

# looping through rows in pandas
# for (index, row) in Dictionary.iterrows()
# README!!
#     Use this code for the maze challenge at the link below
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if wall_on_right() & front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
    else:
        turn_left()
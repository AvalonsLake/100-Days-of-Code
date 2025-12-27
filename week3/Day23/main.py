import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
level = Scoreboard()
car_manager = CarManager()

# Player Movement
screen.onkeypress(player.move_up, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # Level Indicator
    level.get_score()

    # Car Generation
    car_manager.create_car()
    car_manager.move_cars()

    # check for car collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    if player.ycor() > 280:
        player.reset()
        level.raise_score()
        car_manager.raise_speed()


level.game_over()
screen.exitonclick()


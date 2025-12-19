from turtle import Turtle
placement = "center"
font = ("Curiur", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()

    def get_point(self):
        self.score += 1

    def write_score(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.write(f"Score: {self.score} ", False, align=placement, font=font)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=placement, font=font)
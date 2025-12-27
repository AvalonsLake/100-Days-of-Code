from turtle import Turtle

FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        self.level = 1
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-210, 250)
        self.shape("square")
        self.color("black")

    def get_score(self ):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def raise_score(self):
        self.level += 1

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("  GAME OVER\n"
                   f"Your Score: {self.level}", align="center", font=FONT)

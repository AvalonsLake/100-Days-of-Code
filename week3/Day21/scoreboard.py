from turtle import Turtle
placement = "center"
font = ("Curiour", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        with open("data.txt", "r") as data:
            self.highscore = int(data.read())
        super().__init__()
        self.clear()
        self.penup()
        self.hideturtle()
        self.color("white")

    def get_point(self):
        self.score += 1

    def write_score(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score} Highscore: {self.highscore} ", False, align=placement, font=font)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False, align=placement, font=font)

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.highscore}\n")

        self.score = 0
        self.write_score()
        self.goto(0, 0)
        self.write("GAME OVER", False, align=placement, font=font)
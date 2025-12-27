from turtle import Turtle
placement = "center"
font = ("Couriur", 20, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        self.score_p1 = 0
        self.score_p2 = 0
        super().__init__()

    def score_p1(self):
        self.score_p1 += 1

    def score_p2(self):
        self.score_p2 += 1

    def write_score(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,260)
        self.write(f" {self.score_p1} | {self.score_p2}", align=placement, font=font)

    def detect_winner(self):
        if self.score_p1 >= 10:
            self.clear()
            self.penup()
            self.hideturtle()
            self.goto(0, 0)
            self.write("Player 1 Wins!\n "
                       f"      {self.score_p1} | {self.score_p2}", False, align=placement, font=font)
            return True
        if self.score_p2 >= 10:
            self.clear()
            self.penup()
            self.hideturtle()
            self.goto(0, 0)
            self.write("Player 2 Wins!\n "
                       f"      {self.score_p1} | {self.score_p2}", False, align=placement, font=font)
            return True

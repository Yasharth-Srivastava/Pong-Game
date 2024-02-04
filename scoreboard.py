from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.one_score = 0
        self.two_score = 0

    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.two_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.one_score, align="center", font=("Courier", 80, "normal"))

    def winner_scorecard_left(self):
        self.goto(0,0)
        self.write("Left Player wins", align="center", font=("Courier", 20, "normal"))

    def winner_scorecard_right(self):
        self.goto(0,0)
        self.write("Right Player wins", align="center", font=("Courier", 20, "normal"))

    def point_one_score(self):
        self.one_score += 1
        self.update_scoreboard()

    def point_two_score(self):
        self.two_score += 1
        self.update_scoreboard()
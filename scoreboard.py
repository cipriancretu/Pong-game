"""Import turtle library"""
from turtle import Turtle


class Scoreboard(Turtle):
    """This function set up the soreboard"""
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
    """This function update the scoreboard"""
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
    """This function update the scorboard and add a point for the left player"""
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
    """This function update the scorboard and add a point for the right player"""
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

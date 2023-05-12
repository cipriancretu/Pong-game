"""Import the turtle library"""
from turtle import Turtle


class Paddle(Turtle):
    """This function set up the paddles para
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
    """This function set the moving of the paddle up"""
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    """This function set the moving of the paddle down"""
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

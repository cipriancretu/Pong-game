"""Import the turtle library"""
from turtle import Turtle


class Ball(Turtle):
    """This Function set up the ball"""
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.1
    """This function set up the ball movment"""
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    """This function set up the bounce of the turtle, ball"""
    def bounce_y(self):
        self.y_move *= -1
    """This function set up the bounce of the turtle, ball"""
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
    """This function reset the ball"""
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

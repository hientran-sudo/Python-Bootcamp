from turtle import Turtle
START = (0, -280)
class Tim(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("blue")
        self.penup()
        self.x_pos = 0
        self.y_pos = -280
        self.setheading(90)
        self.goto(START)

    def go_up(self):
        self.forward(20)

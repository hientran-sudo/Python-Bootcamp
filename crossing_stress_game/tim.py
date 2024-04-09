from turtle import Turtle

class Tim(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("blue")
        self.penup()
        self.x_pos = 0
        self.y_pos = -280
        self.setheading(90)
        self.goto(self.x_pos, self.y_pos)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.x_pos, new_y)

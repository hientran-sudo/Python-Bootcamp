from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.create_paddle()

    def create_paddle(self):
        self.shape(name="square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)

        self.penup()
        self.goto(self.x_pos, self.y_pos)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.x_pos, new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.x_pos, new_y)

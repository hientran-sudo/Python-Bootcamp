from turtle import Turtle, Screen
init_snake=[(0,0),(-20,0),(-40,0)]

screen = Screen()
screen.tracer(0)

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for dot in init_snake:
            tim = Turtle(shape="square")
            tim.penup()
            tim.goto(dot)
            self.snake.append(tim)

    def move(self):
        self.head.color("blue")
        for i in range(len(self.snake)-1,0,-1):
            self.snake[i].goto(self.snake[i-1].xcor(),self.snake[i-1].ycor())

        #self.head.right(90)
        self.head.forward(20)

    def up(self):
        self.head.color("blue")
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        self.head.color("blue")
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        self.head.color("blue")
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        self.head.color("blue")
        if self.head.heading() != 0:
            self.head.setheading(180)

    def head_x_cor(self):
        return self.head.xcor()

    def head_y_cor(self):
        return self.head.ycor()

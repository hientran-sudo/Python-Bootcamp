from turtle import Turtle, Screen
init_snake=[(0,0),(-20,0),(-40,0)]

screen = Screen()
screen.tracer(0)

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
    
    def create_snake(self):
        for dot in init_snake:
            tim = Turtle(shape="square")
            tim.penup()
            tim.goto(dot)
            self.snake.append(tim)
            
    def move(self):
        self.snake[0].color("blue")
        for i in range(len(self.snake)-1,0,-1):
            self.snake[i].goto(self.snake[i-1].xcor(),self.snake[i-1].ycor())
        
        #self.snake[0].right(90)
        self.snake[0].forward(20)
    
    def up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)

    def down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)

    def left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)

    def right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)
   
 

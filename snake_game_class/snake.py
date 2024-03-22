from turtle import Turtle, Screen
import time
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
            
    def move_forward(self):
        screen.update()
        time.sleep(0.1)
        self.snake[0].color("blue")
        for i in range(len(self.snake)-1,0,-1):
            self.snake[i].goto(self.snake[i-1].xcor(),self.snake[i-1].ycor())
        
        #self.snake[0].right(90)
        self.snake[0].forward(20)
    
    def turn_right(self):
        screen.update()
        time.sleep(0.1)
        self.snake[0].color("blue")
        for i in range(len(self.snake)-1,0,-1):
            self.snake[i].goto(self.snake[i-1].xcor(),self.snake[i-1].ycor())
        
        self.snake[0].right(90)
        self.snake[0].forward(20)

    def turn_left(self):
        screen.update()
        time.sleep(0.1)
        self.snake[0].color("blue")
        for i in range(len(self.snake)-1,0,-1):
            self.snake[i].goto(self.snake[i-1].xcor(),self.snake[i-1].ycor())
        
        self.snake[0].left(90)
        self.snake[0].forward(20)    
 

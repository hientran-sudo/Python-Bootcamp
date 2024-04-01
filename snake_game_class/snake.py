from turtle import Turtle

 init_snake=[(0,0),(-20,0),(-40,0)]

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

     def grow(self):
         new = Turtle(shape="square")
         new.penup()
         self.snake.append(new)

     def move(self):
         for i in range(len(self.snake)-1,0,-1):
             self.snake[i].goto(self.snake[i-1].xcor(),self.snake[i-1].ycor())

         self.head.forward(20)
         self.head.speed('slowest')

     def up(self):
         if self.head.heading() != 270:
             self.head.setheading(90)

     def down(self):
         if self.head.heading() != 90:
             self.head.setheading(270)

     def right(self):
         if self.head.heading() != 180:
             self.head.setheading(0)

     def left(self):
         if self.head.heading() != 0:
             self.head.setheading(180)

     def head_x_cor(self):
         return self.head.xcor()

     def head_y_cor(self):
         return self.head.ycor()

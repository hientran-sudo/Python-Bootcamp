from turtle import Screen
from snake import Snake

screen = Screen()
snake = Snake()
  
screen.listen()
screen.onkey(key="Up", fun=snake.move_forward)
screen.onkey(key="Right", fun=snake.turn_right)
screen.onkey(key="Left", fun=snake.turn_left)

screen.exitonclick()

from turtle import Screen
from snake import Snake

screen = Screen()
snake = Snake()
  
screen.listen()
screen.onkey(key="s", fun=snake.move_forward)
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)

screen.exitonclick()

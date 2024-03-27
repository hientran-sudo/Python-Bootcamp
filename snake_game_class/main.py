from turtle import Screen
from snake import Snake
import time, math

screen = Screen()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    dis_x = snake.head_x_cor() - food.food_x_cor()
    dis_y = snake.head_y_cor() - food.food_y_cor()
    distance = math.sqrt(dis_x**2 + dis_y**2)

    if distance < 15:
        print("nom nom")
      
screen.exitonclick()

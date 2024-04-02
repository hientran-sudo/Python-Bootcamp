from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time, math, random

# screen initalization
screen = Screen()
screen.tracer(0)
score = 0
screen.title("Snake Game")

# objects initalization
scoreboard = Scoreboard()
snake = Snake()
food = Food()

# screen listener
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)

# game body
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # calculate distance
    dis_x = snake.head_x_cor() - food.x_cor
    dis_y = snake.head_y_cor() - food.y_cor

    distance = math.sqrt(dis_x**2 + dis_y**2)
    #print(distance)

    if distance < 20:
        print("nom nom")
        food.remove_food()
        snake.grow()

        scoreboard.add_score()
        scoreboard.update_score()

        food = Food()

    # detect if hit the wall
    if snake.head_x_cor() >= 385 or snake.head_x_cor() <= -385 or snake.head_y_cor() >= 325 or snake.head_y_cor() <= -325:
        scoreboard.game_over()
        game_is_on = False

    # detect if hit himself
    for i in range(len(snake.snake)-1):
        if snake.head_x_cor() == snake.snake[i].xcor():
            print("Bruh")

screen.exitonclick()

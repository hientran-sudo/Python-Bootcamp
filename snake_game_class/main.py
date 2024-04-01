 from turtle import Screen
 from snake import Snake
 from food import Food
 import time, math, random

 # screen initalization
 screen = Screen()
 screen.tracer(0)
 score = 0
 screen.title(f"Snake Game - Score: {score}")

 # objects initalization
 snake = Snake()
 food = Food(random.randint(-280,280), random.randint(-280,280))
 #food.create_food()

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
         #food.remove_food()
         snake.grow()
         food = Food(random.randint(-280,280), random.randint(-280,280))
         score = score + 1
         screen.title(f"Snake Game - Score: {score}")
      
screen.exitonclick()

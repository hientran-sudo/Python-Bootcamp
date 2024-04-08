from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
ball = Ball()

lscore = Scoreboard()
rscore = Scoreboard()
lscore.left()
rscore.right()

screen.listen()
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    # detect if ball out of bound right
    if ball.distance(r_paddle) > 50 and ball.xcor() > 320:
        ball.out_bound()
        lscore.add_lscore()

    # detect if ball out of bound left
    if ball.distance(l_paddle) > 50 and ball.xcor() < -320:
        ball.out_bound()
        rscore.add_rscore()

screen.exitonclick()

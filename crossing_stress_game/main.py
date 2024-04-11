from turtle import Screen
from tim import Tim
from car import Car
#from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Crossing Turtle")
screen.tracer(0)

tim = Tim()
car = Car()

screen.listen()
screen.onkey(fun=tim.go_up, key="Up")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    car.generate_car()
    car.move()
      
screen.exitonclick()

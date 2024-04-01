from turtle import Turtle
 import random

 class Food:
     def __init__(self, x_cor, y_cor):
         self.x_cor = x_cor
         self.y_cor = y_cor

         food = Turtle(shape="circle")
         food.penup()
         food.color("green")
         food.goto(x_cor, y_cor)

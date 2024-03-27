from turtle import Turtle
import random

class Food:
    def __init__(self):
        self.create_food()

    def create_food(self):
        food = Turtle(shape="classic")
        food.penup()
        food.color("green")
        food.goto(self.food_x_cor(), self.food_y_cor())

    def food_x_cor(self):
        x_cor=random.randint(-280,280)
        return x_cor

    def food_y_cor(self):
        y_cor=random.randint(-280,280)
        return y_cor

from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.x_cor = random.randint(-300,250)
        self.y_cor = random.randint(-300,250)

        self.shape("circle")
        self.penup()
        self.color("green")
        self.goto(self.x_cor, self.y_cor)

    def remove_food(self):
        self.reset()

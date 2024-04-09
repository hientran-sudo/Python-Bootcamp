from turtle import Turtle
import random

colors = ["black", "red", "grey"]
class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.x_pos = random.randint(-280,280)
        self.y_pos = random.randint(-280,280)
        self.generate_car()

    def generate_car(self):
        self.shape(name="square")
        self.color(random.choice(colors))
        self.shapesize(stretch_wid=1, stretch_len=2)

        self.penup()
        self.goto(self.x_pos, self.y_pos)

    def move(self):
        self.speed(1)
        self.backward(20)

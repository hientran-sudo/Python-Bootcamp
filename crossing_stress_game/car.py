from turtle import Turtle
import random

colors = ["black", "red", "grey", "green", "yellow", "orange"]
class Car:
    def __init__(self):
        self.set = []
        
    def generate_car(self):
        frequent = random.randint(1, 6)
        if frequent == 1:
            new = Turtle("square")
            new.color(random.choice(colors))
            new.shapesize(stretch_wid=1, stretch_len=2)

            new.penup()
            new.goto(380, random.randint(-240,280))
            self.set.append(new)

    def move(self):
        for car in self.set:
            car.backward(20)

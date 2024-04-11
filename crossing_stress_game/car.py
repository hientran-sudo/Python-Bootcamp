from turtle import Turtle
import random

colors = ["black", "red", "grey", "green", "yellow", "orange"]
speed_level = [1, 3, 6, 10, 0]

class Car:
    def __init__(self):
        self.set = []
        self.i = 0
        
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

    def speed_up(self):
        for car in self.set:
            car.speed(speed_level[self.i]) 
        self.i = self.i + 1

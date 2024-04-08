from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

    def left(self):
        self.lscore = 0
        self.goto(-360,250)
        self.write(f"{self.lscore}", font=("Arial", 24, "normal"))

    def add_lscore(self):
        self.lscore = self.lscore + 1
        self.clear()
        self.write(f"{self.lscore}", font=("Arial", 24, "normal"))

    def right(self):
        self.rscore = 0
        self.goto(340,250)
        self.write(f"{self.rscore}", font=("Arial", 24, "normal"))
        
    def add_rscore(self):
        self.rscore = self.rscore + 1
        self.clear()
        self.write(f"{self.rscore}", font=("Arial", 24, "normal"))

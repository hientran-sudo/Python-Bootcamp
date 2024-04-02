from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(-380,280)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", font=("Arial", 24, "normal"))

    def add_score(self):
        self.score = self.score + 1
        self.clear()

    def game_over(self):
        self.goto(-5,0)
        self.write("Game Over", align= "center", font=("Arial", 24, "normal"))

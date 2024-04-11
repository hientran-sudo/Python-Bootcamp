from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()

    def level(self):
        self.level = 1
        self.goto(-360,250)
        self.write(f"Level: {self.level}", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(-100,0)
        self.write("Game Over", font=("Arial", 24, "normal"))
   
    def level_up(self):
        self.level = self.level + 1
        self.clear()
        self.write(f"Level: {self.level}", font=("Arial", 24, "normal"))

    

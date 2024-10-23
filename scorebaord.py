from turtle import Turtle 


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_scorebaord()


    def update_scorebaord(self):
        self.write(f"Score = {self.score}", align="center", font=("Arial", 15, "normal"))


    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 15, "normal"))


    def increase_score(self):
        self.score += 1 
        self.clear()
        self.update_scorebaord()

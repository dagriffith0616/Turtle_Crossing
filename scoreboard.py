from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 270)
        self.update_score()



    def update_score(self):
        self.write(f"Level: {self.level}", False, 'left', FONT)



    def score(self):
        self.level += 1
        self.clear()
        self.update_score()
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.pencolor('red')
        self.write("GAME OVER!", False, 'center', FONT)

from turtle import Turtle
FONT = ("Courier", 12, "normal")


class ScoreCard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.goto(x=-250, y= 250)
        self.write(f"Score: {self.level}", align="center", font=FONT)

    def update_score(self):
        self.clear()
        self.increase_score()
        self.write(f"Score: {self.level}", align="center", font=FONT)

    def increase_score(self):
        self.level += 1

    def over(self):
        self.home()
        self.write("Game Over", align="center", font=FONT)


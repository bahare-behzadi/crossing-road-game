FONT = ("Courier", 15, "normal")

from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(-260, 260)
        self.color("black")
        self.write(arg=f"LEVEL= {self.level}", align='Center', font=FONT)
        self.hideturtle()

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(arg=f"LEVEL= {self.level}", align='Center', font=FONT)

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.color("red")
        self.write(arg=f"GAME OVER", align='Center', font=FONT)
        self.hideturtle()
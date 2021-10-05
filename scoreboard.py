from turtle import Turtle

ALIGNMENT = "left"
FONT = ("Courier", 20, "bold")
STARTING_LOCATION = (-270, 250)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.level = -1
        self.goto(STARTING_LOCATION)

    def level_counting(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)
        return self.level

    def game_over(self):
        self.goto(-0, 0)
        self.clear()
        self.write(f"Game Over \n Level: {self.level} ", align="center", font=FONT)

from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280, 270)
        self.level = 1
        self.write(f"Level: {self.level}", False, align="left", font=FONT)

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", False, align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", False, align="center", font=FONT)

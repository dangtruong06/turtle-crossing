from turtle import Turtle

FONT = ("Courier", 30, "normal")
POS = (-230, 230)

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(POS)
        self.hideturtle()
        self.refresh()

    def increase_level(self):
        self.level += 1
        if not self.level > 3:
            self.clear()
            self.refresh()

    def refresh(self):
        self.write(f"Level {self.level}", align="center", font=FONT)

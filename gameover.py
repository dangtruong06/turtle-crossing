from turtle import Turtle

class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.write("Game Over", align="center", font=("Courier", 40, "bold"))
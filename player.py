from turtle import Turtle
STARTING_POS = (0,-270)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POS)

    def move_up(self):
        self.forward(10)

    def move_down(self):
        self.forward(-10)

    def reset(self):
        self.goto(STARTING_POS)
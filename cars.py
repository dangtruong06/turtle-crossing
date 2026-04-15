from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class Car(Turtle):
    #when we make a new car, assign random height
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.hideturtle()
        self.car_speed = 5

    def add_car(self):
        chance = random.randint(1,6)
        if chance == 1:
            car = Turtle("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            random_y =  random.randint(-220,220)
            car.goto(300, random_y)
            self.car_list.append(car)

    def move(self):
        for car in self.car_list:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += 10

    def hide(self):
        for car in self.car_list:
            car.hideturtle()
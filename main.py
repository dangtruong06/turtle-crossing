from turtle import Screen
from player import Player
from cars import Car
from level import Level
from gameover import GameOver
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
screen.listen()

screen.onkey(turtle.move_up, "Up")
screen.onkey(turtle.move_down, "Down")

game_on = True

car = Car()
level = Level()

while game_on:
    screen.update()
    time.sleep(0.1)

    car.add_car()
    car.move()

    #check for turtle reaching the end
    if turtle.ycor() > 280:
        level.increase_level()
        if level.level > 3:
            game_on = False

        car.increase_speed()
        turtle.reset()
        car.hide()

    #check for collision
    for c in car.car_list:
        if c.distance(turtle) < 25:
            game_on = False

game = GameOver()

screen.exitonclick()
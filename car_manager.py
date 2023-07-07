from turtle import Turtle
from random import choice, randint


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create(self):
        self.hideturtle()
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=2, stretch_len=1)
        new_car.color(choice(COLORS))
        new_car.penup()

        new_car.setheading(90)
        new_car.goto(300, randint(-250, 250))
        self.all_cars.append(new_car)


    def car_move(self):
        for car in self.all_cars:
            car.goto(car.xcor()-self.car_speed, car.ycor())

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

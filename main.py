import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('green')
screen.bgpic("road.png")
screen.listen()
player = Player()
scoreboard = Scoreboard()
screen.onkey(fun=player.up, key="Up")
game_is_on = True
time_sleep = 0.1
number_of_loops = 0
car = CarManager()
while game_is_on:
    time.sleep(time_sleep)
    screen.update()
    if number_of_loops % 6 == 0:
        car.create()
    car.car_move()
    number_of_loops += 1
    for each_car in car.all_cars:
        if player.distance(each_car) < 20:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() > 280:
        player.restart()
        scoreboard.increase_level()
        car.level_up()

screen.exitonclick()

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("The Turtle Crossing")
screen.tracer(0)


player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(fun=player.move, key="Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    for car in car_manager.cars:
        if car.distance(player) < 10:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() >= 280:
        scoreboard.update_scoreboard()
        player.reset_position()
        car_manager.increase_speed()


screen.exitonclick()

from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle crossing")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(fun=player.move, key="Up")
scoreboard.level_counting()

game_is_on = True
while game_is_on:
    time.sleep(car_manager.move_speed)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    if player.ycor() > 280:
        scoreboard.level_counting()
        player.reset_level()
        car_manager.move_speed *= 0.5
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()

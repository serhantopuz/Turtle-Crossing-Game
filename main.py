import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.onkey(player.move, "Up")
    car_manager.create_cars()
    if car_manager.move_cars(player) == 1:
        scoreboard.game_over()
        game_is_on = False
    if player.check_finish():
        car_manager.increase_speed()
        scoreboard.update_level()


screen.exitonclick()


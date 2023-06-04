import time
from turtle import Screen

from scorecard import ScoreCard
from player import Player
from car_manager import CarManager


screen = Screen()
screen.setup(height=600, width=600)
screen.tracer(0)
player = Player()
cars = CarManager()
score = ScoreCard()
screen.listen()
screen.onkey(player.move_player, "w")



is_game_on = True

while is_game_on:
    time.sleep(0.15)
    screen.update()
    cars.create_cars()
    cars.move_forward()
    for car in cars.all_cars:
        if car.distance(player) < 20:
            is_game_on = False
            score.over()

    if player.game_over():
        player.goto_start()
        cars.levelup()
        score.update_score()





screen.exitonclick()
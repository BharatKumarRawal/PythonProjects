from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.create_cars()
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            rand_y = random.randint(-250, 250)
            new_car.goto(x=300, y=rand_y)
            self.all_cars.append(new_car)


    def move_forward(self):
        for cars in self.all_cars:
            cars.backward(STARTING_MOVE_DISTANCE)


    def levelup(self):
        self.car_speed += MOVE_INCREMENT






from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.starting_x_cor = 300
        self.between_cars = 30
        self.move_speed = 5

    def create_cars(self):
        car = Turtle("square")
        car.penup()
        car.color(random.choice(COLORS))
        car.shapesize(stretch_wid=1, stretch_len=2)
        random_ycor = random.randint(-240, 240)
        car.goto(self.starting_x_cor, random_ycor)
        self.cars.append(car)
        self.starting_x_cor += self.between_cars

    def move_cars(self, player):
        for car in self.cars:
            car.backward(self.move_speed)
            if car.xcor() < -330:
                self.cars.remove(car)
            if car.distance(player) < 20.5:
                return 1

    def increase_speed(self):
        self.move_speed += 4
        self.between_cars += 15


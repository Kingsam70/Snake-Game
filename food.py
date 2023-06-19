from turtle import Turtle
from random import randint


FOOD_COLOR = "red"


class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.penup()
        self.color(FOOD_COLOR)
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.goto(randint(-270, 270), randint(-270, 270))

    def reset(self):
        """resets the position of the food on collision with the snake"""
        self.goto(randint(-270, 270), randint(-270, 270))

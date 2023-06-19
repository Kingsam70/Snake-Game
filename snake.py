from turtle import Turtle

coordinates = ((0, 0), (-20, 0), (-40, 0))
HEAD_COLOR = "red"


class Snake:
    def __init__(self):
        self.segments = []
        self.create_turtle()
        self.head = self.segments[0]
        self.head.color(HEAD_COLOR)


    def extend(self):
        """extends the length of the snake when takes up the food"""
        tim_the_dictator = Turtle("square")
        tim_the_dictator.penup()
        tim_the_dictator.goto(self.segments[-1].xcor(), self.segments[-1].ycor())
        self.segments.append(tim_the_dictator)

    # Below up, down, right, left functions in order to control the snake movement
    def up(self):
        if not self.head.heading() == 270:
            self.head.setheading(90)

    def down(self):
        if not self.head.heading() == 90:
            self.head.setheading(270)

    def right(self):
        if not self.head.heading() == 180:
            self.head.setheading(0)

    def left(self):
        if not self.head.heading() == 0:
            self.head.setheading(180)

    def move(self):
        """moves the head of the snake forward by 20 and other segments to follow the position of the head"""
        for segment in range(len(self.segments) - 1, 0, -1):
            xcor = self.segments[segment - 1].xcor()
            ycor = self.segments[segment - 1].ycor()

            self.segments[segment].goto(xcor, ycor)

        self.head.forward(20)

    def create_turtle(self):
        """creates the initial for of snake (3 segments)"""
        for coordinate in coordinates:
            tim = Turtle("square")
            tim.penup()
            tim.goto(coordinate)
            self.segments.append(tim)


from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)

game_running = True
while game_running:
    screen.update()
    snake.move()
    time.sleep(0.1)

    # Quits the game when snake touches wall
    if snake.head.xcor() >= 290 or snake.head.xcor() <= -290:
        game_running = False
        scoreboard.game_over()

    elif snake.head.ycor() >= 300 or snake.head.ycor() <= -290:
        game_running = False
        scoreboard.game_over()

    # Check collision with the food and if so increase length of the snake
    if snake.head.distance(food) < 15:
        print("Collision with food")
        food.reset()
        snake.extend()  # extends the length of the snake on collision with a food
        scoreboard.increase_score()

    # Check collision with its own tail and if so end the game
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_running = False


screen.exitonclick()

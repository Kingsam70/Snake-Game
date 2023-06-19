from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        with open("./high_score.txt") as file:
            content = file.read()
            self.high_score = int(content)

        self.hideturtle()
        self.penup()
        self.goto(-180, 260)

        self.forward(100)
        self.fillcolor("green")
        self.write(f"High Score: {self.high_score}       |        Score: {self.score}", move=False, align='center', font=('Arial', 20, 'normal'))


    def increase_score(self):
        """increases the score"""
        self.score += 1
        self.clear()
        self.write(f"High Score: {self.high_score}       |        Score: {self.score}", move=False, align='center',font=('Arial', 20, 'normal'))

    def game_over(self):
        """prints large game over on the screen when the game is over"""
        self.home()
        self.write("GAME OVER", move=False, align='center', font=('Arial', 30, 'normal'))
        if self.score > self.high_score:
            with open("./high_score.txt", "w") as file:
                file.write(str(self.score))

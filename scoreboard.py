from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()

    def updtade_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font="normal")



    def increase_score(self):
        self.score += 1
        self.clear()
        self.updtade_score()
from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.life = 3
        self.goto(-340, -290)
        self.color("white")
        self.write(f"SCORE: {self.score} LIFE: {self.life}", align="left", font=FONT)

    def increase_score(self):
        self.score += 200
        self.clear()
        self.write(f"SCORE: {self.score} LIFE: {self.life}", align="left", font=FONT)

    def decrease_life(self):
        self.life -= 1
        self.clear()
        self.write(f"SCORE: {self.score} LIFE: {self.life}", align="left", font=FONT)

    def game_over(self):
        self.clear()
        self.home()
        self.write("GAME OVER", align="center", font=FONT)

    def win_screen(self):
        self.clear()
        self.home()
        self.write("YOU'VE WON!", align="center", font=FONT)

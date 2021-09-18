from turtle import Turtle


class Player(Turtle):

    def __init__(self, position):
        super().__init__()
        self.create_player()
        self.setpos(position)

    def create_player(self):
        self.shape("square")
        self.penup()
        self.turtlesize(1, 5)
        self.color("white")

    def move_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

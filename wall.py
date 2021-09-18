import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Wall(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.x_pos = x
        self.y_pos = y
        self.x_new = 0
        self.create_block()

    def create_block(self):
        self.shape("square")
        self.shapesize(1, 4)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(self.x_pos, self.y_pos)

    def hide_block(self):
        self.x_new = self.xcor() - 300
        self.reset()
        self.goto(self.x_new, self.ycor())


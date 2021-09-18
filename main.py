import time
from turtle import Screen
from player import Player
from ball import Ball
from wall import Wall
from score import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Breakout game")

all_wall_blocks = []


def create_wall():
    # Create wall
    global all_wall_blocks
    all_wall_blocks = []
    y_pos = 280
    for _ in range(1, 9):
        x_pos = 330
        for _ in range(1, 9):
            block = Wall(x_pos, y_pos)
            all_wall_blocks.append(block)
            x_pos -= 95
        y_pos -= 30


def game_prog():
    screen.tracer(0)
    screen.bgcolor("black")
    player = Player((0, -250))
    ball = Ball()
    screen.listen()
    screen.onkeypress(player.move_left, "Left")
    screen.onkeypress(player.move_right, "Right")
    screen.onkeypress(player.move_left, "a")
    screen.onkeypress(player.move_right, "d")
    score = Score()
    create_wall()
    game = True

    while game:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # Detection with left and right wall
        if ball.xcor() > 360 or ball.xcor() < -360:
            ball.bounce_x()

        # Detection with up wall
        if ball.ycor() > 290:
            ball.bounce_y()

        # Detection with a player
        if ball.distance(player) < 40:
            ball.bounce_y()

        # Detection if ball misses player
        if ball.ycor() < -290:
            ball.reset_position()
            score.decrease_life()

        if score.life < 0:
            screen.clearscreen()
            screen.bgcolor("black")
            score.game_over()
            game = False

        # Detection if ball hit the wall
        for x in range(len(all_wall_blocks)):
            if ball.distance(all_wall_blocks[x]) < 40:
                if len(all_wall_blocks) > 0:
                    all_wall_blocks[x].hide_block()
                    all_wall_blocks.remove(all_wall_blocks[x])
                    ball.bounce_y()
                    score.increase_score()
                    break
                else:
                    score.win_screen()
                    time.sleep(5)
                    game = False


while True:
    user_input = screen.textinput("Do you wanna play?", "Do you want to start a new game? (Y/N) ")
    answer = user_input.lower()
    if answer == "y" or answer == "yes":
        screen.clearscreen()
        game_prog()
    else:
        screen.exitonclick()

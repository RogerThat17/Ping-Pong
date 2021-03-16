from turtle import Screen

from paddle import Paddle

from ball import Ball

from scoreboard import Scoreboard

import time

screen = Screen()
screen.title("Ping Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()
score = Scoreboard()


screen.listen()

screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()

    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_ball_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_ball_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()

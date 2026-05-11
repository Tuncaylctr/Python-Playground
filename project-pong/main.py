from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)


l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(l_paddle.move_up, "w")
is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_right()
    if ball.collision_with_wall():
        ball.bounce_y()

    if ball.collision_with_paddle(r_paddle) or ball.collision_with_paddle(l_paddle):
        ball.bounce_x()

    if  ball.ball_out_of_bounds_right() :
        scoreboard.increase_l_score()
        ball.reset_position()

    if ball.ball_out_of_bounds_left():
        scoreboard.increase_r_score()
        ball.reset_position()

    

    















screen.exitonclick()
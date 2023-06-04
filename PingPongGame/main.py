from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scorecard import Scorecard
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong Game")

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scorecard()
screen.tracer(0)







screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")



game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
        #bounce the ball
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < - 340:
        ball.bounce_back()
        time.sleep(0.05)

    if ball.xcor() > 380:
        ball.reset_position()
        score.increase_l_score()

    if ball.xcor() < -380:
        ball.reset_position()
        score.increase_r_score()

screen.exitonclick()

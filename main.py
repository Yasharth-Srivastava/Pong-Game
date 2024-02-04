from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
paddle_one = Paddle((350,0))
paddle_two = Paddle((-350,0))
main_ball = Ball((0,0))
scoreboard = Scoreboard()
scoreboard.update_scoreboard()

screen.listen()
screen.onkey(paddle_one.go_up, "Up")
screen.onkey(paddle_one.go_down, "Down")
screen.onkey(paddle_two.go_up, "w")
screen.onkey(paddle_two.go_down, "s")

score_1 = 0
score_2 = 0

game_on = True
while game_on:
    time.sleep(main_ball.move_speed)
    screen.update()
    main_ball.move()
   

    #Detect collision with wall

    if main_ball.ycor() > 280 or main_ball.ycor() < -280:
        main_ball.bounce_y()

    #Detect collision with paddle

    if main_ball.distance(paddle_one) < 50 and main_ball.xcor() > 330 or main_ball.distance(paddle_two) < 50 and main_ball.xcor() < -330:
        main_ball.bounce_x()

    #Detect Paddle one miss

    if main_ball.xcor() > 380:
        main_ball.reset_position_x()
        scoreboard.point_two_score()
        scoreboard.update_scoreboard()
        score_1 = score_1+1
        if score_1 == 5:
            scoreboard.winner_scorecard_left()
            game_on = False

    #Detect Paddle two miss

    if main_ball.xcor() < -380:
        main_ball.reset_position_y()
        scoreboard.point_one_score()
        scoreboard.update_scoreboard()
        score_2 = score_2+1
        if score_2 == 5:
            scoreboard.winner_scorecard_right()
            game_on = False


screen.exitonclick()
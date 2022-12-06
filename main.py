from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")

screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")

game_on = True
while game_on:
    time.sleep(ball.move_speed) 
    screen.update() 
    ball.move()  
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    #detect collisions with the r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 325:
        ball.bounce_x()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -325:
        ball.bounce_x()
    
    #detect if the ball has missed the paddle
    #R paddle
    if ball.xcor() > 360  :
        print("ball missed")
        ball.reset_ball()
        scoreboard.l_point()
        
    #L paddle    
    if  ball.xcor() < -360 :
        print("ball missed")
        ball.reset_ball()
        scoreboard.r_point()
        
screen.exitonclick()

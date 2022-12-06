from turtle import Turtle
import random

class Ball(Turtle):
    
    def __init__(self) :
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.x_move = random.randint(5,20) # defining a random number that will be added as we move the ball
        self.y_move = random.randint(5,20) 
        self.move_speed = 0.1 # initialising the speed of the ball
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
        
    def bounce_y(self):
        self.y_move *= -1 # now the direction will be reveresed and the ball will 
        
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9 #everytime it hits the paddle it will increase speed
        
    def reset_ball(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()
        
        
    
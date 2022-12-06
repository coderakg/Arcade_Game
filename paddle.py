from turtle import Turtle

class Paddle(Turtle): # because we want it to inherit from the turtle class
    
    def __init__(self,position) :
        super().__init__()
        # self.speed("fastest")
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(position)
        self.shapesize(stretch_len=1,stretch_wid=5)
    
    def go_up(self):
        new_y = self.ycor() + 20 
        self.goto(self .xcor(),new_y)

    def go_down(self):
        new_y = self.ycor() - 20 
        self.goto(self .xcor(),new_y)
    
    
    
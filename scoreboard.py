from turtle import Turtle


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        with open("left_hs.txt") as left_hs: 
            self.left_highscore = int(left_hs.read())
            print(self.left_highscore)
        self.r_score = 0
        with open("right_hs.txt") as right_hs: # right hs
            self.right_highscore = int(right_hs.read())
            print(self.right_highscore)
        self.update_score()
        
    def update_score(self):
        self.goto(-240,220)
        self.clear()
        self.write(f"Left Score :{self.l_score}" , align="center",font=("Courier",20,"normal"))
        self.goto(-240,-260)
        if self.l_score > self.left_highscore:
            self.left_highscore = self.l_score
            with open("left_hs.txt",mode="w") as left_file:
                left_file.write(f"{self.left_highscore}")
        self.write(f"Left Highscore : {self.left_highscore}" , align="center",font=("Courier",20,"normal"))
        self.goto(255,220)
        self.write(f"Right Score :{self.r_score}" , align="center",font=("Courier",20,"normal"))
        self.goto(240,-260)
        if self.r_score > self.right_highscore:
            self.right_highscore = self.r_score
            with open("right_hs.txt",mode="w") as right_file:
                right_file.write(f"{self.right_highscore}")
        self.write(f"Right Highscore : {self.right_highscore} " , align="center",font=("Courier",20,"normal"))
        
    def l_point(self):
        self.l_score += 1
        self.update_score()
        
    def r_point(self):
        self.r_score += 1 
        self.update_score()       

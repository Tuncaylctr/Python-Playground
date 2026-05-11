from turtle import Turtle
from scoreboard import Scoreboard
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move_right(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def move_left(self):
        new_x = self.xcor() - self.x_move
        new_y = self.ycor() - self.y_move
        self.goto(new_x, new_y)

    def collision_with_wall(self):
        if self.ycor() > 280 or self.ycor() < -280:
            return True
    
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9  # Increase speed after each paddle hit
    # Unstick the ball by nudging it past the collision boundary
        if self.xcor() > 320:
            self.setx(319)
        elif self.xcor() < -320:
            self.setx(-319)

    def collision_with_paddle(self, paddle):
        if self.distance(paddle) < 50 and (self.xcor() > 320 or self.xcor() < -320):
            return True
        

    def ball_out_of_bounds_right(self):
        if self.xcor() > 380 :
            return True

    def ball_out_of_bounds_left(self):
        if self.xcor() < -380:
            return True
        
    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1  
    
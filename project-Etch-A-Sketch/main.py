from turtle import Turtle,Screen

tuncay = Turtle()
screen = Screen()



def move_forward():
    tuncay.forward(10)

def move_backward():
    tuncay.backward(10)

def turn_left():
    tuncay.left(10)

def turn_right():
    tuncay.right(10)
    
def clear_screen():
    tuncay.clear()
    tuncay.penup()
    tuncay.home()
    tuncay.pendown()

screen.listen()


screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)


















screen.exitonclick()


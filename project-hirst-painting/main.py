# import colorgram

# color = colorgram.extract("/Users/macbook/Desktop/Python-Playground/project-hirst-painting/image.jpg", 30)
# rgb_list = []
# for i in color:
#     rgb_item = (i.rgb.r, i.rgb.g, i.rgb.b )
#     rgb_list.append(rgb_item)

# print(rgb_list)

import turtle as turtle_module
import random
tuncay = turtle_module.Turtle()
turtle_module.colormode(255)   
tuncay.penup()
tuncay.hideturtle()
color_list =[(243, 237, 230), (221, 148, 84), (51, 105, 137), (153, 83, 54), (245, 229, 235), (215, 229, 237), (120, 162, 188), (233, 243, 238), (145, 65, 93), (220, 86, 58), (41, 37, 32), (166, 152, 44), (206, 127, 154), (50, 124, 85), (200, 85, 118), (27, 50, 73), (73, 160, 122), (231, 201, 111), (40, 57, 108), (113, 181, 151), (51, 36, 48), (121, 34, 56), (102, 119, 170), (243, 158, 182), (27, 51, 40), (45, 160, 180), (248, 167, 154), (7, 103, 77), (112, 43, 34), (143, 213, 224)] 

tuncay.setheading(225)
tuncay.forward(300)
tuncay.setheading(0)    
tuncay.speed("fastest")

number_of_dots = 100

for dot_count  in range(1, number_of_dots + 1):

    tuncay.dot(20, random.choice(color_list))
    tuncay.forward(50)

    if dot_count % 10 == 0:
        tuncay.setheading(90)
        tuncay.forward(50)
        tuncay.setheading(180)
        tuncay.forward(500)
        tuncay.setheading(0)




screen = turtle_module.Screen()
screen.exitonclick()
# with open("weather_data.csv") as file:
#     weather_data = file.readlines()
#     print(weather_data)


# import csv

# with open ("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperature = []
#     for row in data:
#         if row[1]  != 'temp':
#             temperature.append(int(row[1]))
#     print (temperature)

# import pandas
# data =pandas.read_csv("/Users/macbook/Desktop/Python-Playground/project-us-state-game/weather_data.csv")
# # data_list = data["temp"].to_list()
# # temperature_sum = 0
# # number_of_items = len(data_list)
# # for temp in data_list:
# #     temperature_sum += temp
# # print(temperature_sum / number_of_items)

# # print(sum(data_list)/number_of_items)

# # print(data["temp"].mean())

# # print(data["temp"].max())
# # print(data.temp)
# monday_data = data[data.day == "Monday"]
# monday_temp = monday_data.temp[0]
# monday_temp_F = (monday_temp * 9/5) + 32
# print(monday_temp_F)

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")


 #Central Park Squirrel Data Analysis
# import pandas

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(grey_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)

# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
# }

# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")


import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


df = pd.read_csv("50_states.csv")
state_list =df["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in state_list if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in state_list:
        guessed_states.append(answer_state)
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        state_data = df[df["state"] == answer_state]
        writer.goto(int(state_data.x.item()), int(state_data.y.item()))
        writer.write(answer_state)






screen.exitonclick()
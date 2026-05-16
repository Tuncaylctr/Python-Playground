# with open("file1.txt") as file1:
#   list1 = file1.readlines()
    
# with open("file2.txt") as file2:
#   list2 = file2.readlines()
    
# result = [int(num) for num in list1 if num in list2]
 
# print(result)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word: len(word) for word in sentence.split()}
# print(result)

# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

# weather_f = {date:(temp_c * 9/5) + 32      for  (date,temp_c)   in weather_c.items()}

# print(weather_f)


# student_dict ={"student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}

# for (key, value) in student_dict.items():
#     print(value)
#     print(key)

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
# for (index, row) in student_data_frame.iterrows():
#     print(row.student)
#     print(row.score)


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
import pandas
with open("nato_phonetic_alphabet.csv") as file:
    data = pandas.read_csv(file)
    nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}



#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
output_list = [nato_dict[letter] for letter in word]
print(output_list)
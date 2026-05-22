#FileNotFound
# with open('data.txt', 'r') as file:
#     data = file.read()
#     print(data)

#KeyError
# my_dict = {'name': 'Alice', 'age': 30}
# print(my_dict['gender'])
#IndexError
# my_list = [1, 2, 3]
# print(my_list[5])

#TypeError
# result = 'Hello' + 5

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["dasdad"])

# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# # finally:
# #     file.close()
# #     print("File was closed.")

# finally:
#     raise TypeError("errorrrrrr")


# height = float(input("Height: "))
# weight =  int (input("Weight: "))

# if height > 3 :
#     raise ValueError("Human height should not be over 3 meters.")
# bmi = weight/height ** 2
# print(bmi)


fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
  try:
    fruit = fruits[index]
  except IndexError:
    print("Fruit pie")
  else:
    print(fruit + " pie")
 
make_pie(4)


facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]
 
 
def count_likes(posts):
 
    total_likes = 0
    for post in posts:
      try:
        total_likes = total_likes + post['Likes']
      except KeyError:
        pass 
    
    return total_likes
 
 
count_likes(facebook_posts)


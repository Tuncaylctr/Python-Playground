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

# fruits = ["Apple", "Pear", "Orange"]

# def make_pie(index):
#   try:
#     fruit = fruits[index]
#   except IndexError:
#     print("Fruit pie")
#   else:
#     print(fruit + " pie")
 
# make_pie(4)


# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]
 
 
# def count_likes(posts):
 
#     total_likes = 0
#     for post in posts:
#       try:
#         total_likes = total_likes + post['Likes']
#       except KeyError:
#         pass 
    
#     return total_likes
 
# count_likes(facebook_posts)
import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

#  PASSWORD GENERATOR  #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

#  SAVE PASSWORD #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        return
    else:
        try:
            with open("data.json", "r") as data_file:  # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        except json.JSONDecodeError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
    website_entry.delete(0, END)
    password_entry.delete(0, END)

#find password
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file: 
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="error", message=f"NO details for {website} exists.")

#  UI SETUP  #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#Entries
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()
email_entry = Entry(width=38)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "default@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

#Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
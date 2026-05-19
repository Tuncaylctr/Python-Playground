
# def add(*args):
#     x=0
#     for n in args:
#         x += n
#     return x

# def calculate(n,**kwargs):
   
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     return n

# print(calculate(2, add=3, multiply=5))

# class Car:
#     def __init__(self, **kw):
#         self.make = kw.get("make")
#         self.model = kw.get("model")
#         self.color = kw.get("color")

# print(add(1,2,3,4,5))

from tkinter import *




def convert():
    try:
        n = float(input_entry.get())
        km = round(n * 1.60934, 2)
        answer_label.config(text=f"{km}")
    except ValueError:
        answer_label.config(text="Invalid")


#window
screen = Tk()
screen.title("Mile to Km Converter")
screen.minsize(width=300, height=150)
screen.config(padx=40, pady=40)

#label
miles_label = Label(text="Miles")
miles_label.grid(column=3, row=0)

km_label = Label(text="Km")
km_label.grid(column=3, row=1)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)


answer_label = Label(text="0")
answer_label.grid(column=1, row=1)

#button
calculate_button = Button(text="Calculate", command=convert)
calculate_button.grid(column=1, row=2)

#entry
input_entry = Entry(width=7)
input_entry.grid(column=1, row=0)









screen.mainloop()


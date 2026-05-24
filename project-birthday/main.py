# import smtplib

# my_email= "shoponline787878@gmail.com"
# password = ""

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="tuncaylctr@yahoo.com",
#         msg="Subject:Hello!\n\nkenangotdu!")

# import datetime as dt
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)

# date_of_birth = dt.datetime(year = 2006 , month = 9 , day = 26)
# print(date_of_birth)
# import random
# import datetime as dt
# import smtplib
# now = dt.datetime.now()
# current_day = now.weekday()
# my_email= "shoponline787878@gmail.com"
# password = ""
# print(current_day)

# if current_day == 4:
#     with open('quotes.txt', 'r') as quotes:
#         lines = quotes.readlines()
#         quote_of_day = random.choice(lines)
#         # x = random.randint(0,101)
#         # quote_of_day = lines[x]

#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs="tuncaylctr@yahoo.com",
#             msg=f"Subject:Friday motivation\n\n{quote_of_day}")

#To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.

from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )

        





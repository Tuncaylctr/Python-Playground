# import requests
# import datetime
# MY_LAT = 56.949650
# MY_LONG = 24.105186

# # response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # response.raise_for_status()

# # data = response.json()

# # longitude = data["iss_position"]["longitude"]
# # latitude = data["iss_position"] ["latitude"]
# # iss_position = (longitude,latitude)

# # print(iss_position)

# parameters ={
#     "lat" : MY_LAT,
#     "lng" : MY_LONG,
#     "formatted" : 0 ,
#     "tzid": "Europe/Riga"}

# #https://api.sunrise-sunset.org/json?lat=56.949650&lng=24.105186
# response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters) 
# response.raise_for_status()
# data =response.json()
# sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
# sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

# print(sunrise)
# print(sunset)

# time_now = datetime.datetime.now()
# print(time_now.hour)

import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"


MY_LAT = 51.507351 # latitude
MY_LONG = -0.127758 #  longitude

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 < iss_latitude < MY_LAT + 5 and MY_LONG - 5 < iss_longitude < MY_LONG + 5 :
            return True
 
def is_night():
      
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if sunrise >= time_now or sunset <= time_now :
         return True
    

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs= "tuncaylctr@yahoo.com" ,
                msg=f"Subject:LOOK UP!!!\n\nThe ISS is above you in the sky"
        )


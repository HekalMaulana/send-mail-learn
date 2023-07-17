# import smtplib
#
# my_email = "hekalmaulanaa@gmail.com"
# my_password = "khwgkbmlqzbwgixg"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(from_addr=my_email, to_addrs="hekalmaulanaa@yahoo.com",
#                         msg="Subject:Hello\n\nHi Muhammad Hekal Maulana")


# import datetime as dt
#
# now = dt.datetime.now()
# print(now)
# day = now.day
# print(day)
# month = now.month
# print(month)
# year = now.year
# print(year)
#
# date_of_birth = dt.datetime(year=2004, month=7, day=19)
# print(date_of_birth)
#
# name_of_day = now.strftime("%A")
# print(name_of_day)
# name_of_month = now.strftime("%B")
# print(name_of_month)

import datetime as dt
import smtplib
import random

# Variable
my_email = "hekalmaulanaa@gmail.com"
my_password = "khwgkbmlqzbwgixg"

# Get a current of week day
now = dt.datetime.now()
current_day_of_week = now.weekday()

# Get a list quotes and choice the quotes
with open("quotes.txt", "r") as data_file:
    list_quotes = data_file.readlines()

quotes_choice = random.choice(list_quotes)

# Condition when the day is tuesday
if current_day_of_week == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="hekalmaulanaa@yahoo.com",
                            msg=f"Subject:Daily Quotes\n\n{quotes_choice}")
else:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="hekalmaulanaa@yahoo.com",
                            msg=f"Subject:Daily Quotes\n\nNo quotes for today")

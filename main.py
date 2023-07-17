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


import datetime as dt

now = dt.datetime.now()
print(now)
day = now.day
print(day)
month = now.month
print(month)
year = now.year
print(year)

date_of_birth = dt.datetime(year=2004, month=7, day=19)
print(date_of_birth)

name_of_day = now.strftime("%A")
print(name_of_day)
name_of_month = now.strftime("%B")
print(name_of_month)
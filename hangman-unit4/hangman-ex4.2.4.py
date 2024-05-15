import calendar
import datetime
user_date = input("Enter a date: ")
if(calendar.weekday(int(user_date[6:10]),int(user_date[3:5]),int(user_date[:2]))==0):
    print("Monday")


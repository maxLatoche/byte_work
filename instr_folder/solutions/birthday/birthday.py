import time
import datetime

def age_to_time():     
    years = int(input("How old are you? "))     
    months = years*12
    days = years*365
    hours = days * 24
    minutes = hours * 60
    print("months : {0}, days : {1}, hours : {2}, and minutes : {3}".format(months,days,hours,minutes))
    

def birthday_to_time():
    age = str(input("What's your birthday?(YYYY-MM-DD)"))   
    convert = datetime.datetime.strptime(age,"%Y-%m-%d")
    now = datetime.datetime.now()
    diff = now - convert
    days = int(diff.days)
    months = int(days / 30)
    hours = days * 24
    minutes = hours * 60
    print("months : {0}, days : {1}, hours : {2}, and minutes : {3}".format(months,days,hours,minutes))

birthday_to_time()
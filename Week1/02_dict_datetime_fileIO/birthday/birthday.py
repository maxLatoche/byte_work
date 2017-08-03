import datetime
import calendar
from datetime import timedelta

def age_to_time(your_age):
	#establish bday = now - your_age
	now = datetime.datetime.now()
	tdelta = timedelta(days=your_age*365)
	byear = now - tdelta
	#get the difference between those 2
	diff = now - byear
	#convert days to months
	def delta_to_months(diff, )
	#convert days to hours
	#convert days to minutes
	#age = now - byear
	print(diff)	


def birthday_to_time():
	pass

age_to_time(27)
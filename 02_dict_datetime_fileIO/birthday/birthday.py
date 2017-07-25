import datetime
from datetime import timedelta

def age_to_time(your_age):
	'''
	Answered the wrong question dummy
	#get current date
	tday = datetime.date.today()
	#create timedelta w your_age
	tdelta = timedelta(days=your_age*365)
	#return current date - timedelta
	bday = tday - tdelta 
	print(bday.months)
	'''
	#establish bday, now - your_age
	now = datetime.datetime.today()
	tdelta = timedelta(days=your_age*365)
	byear = now - tdelta

	#age = now - byear
	print(byear)	


def birthday_to_time():
	pass

age_to_time(27)
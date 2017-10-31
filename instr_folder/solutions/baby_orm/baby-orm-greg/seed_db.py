from user_class import Model
from user_class import Users
from user_class import Stocks
from faker import Faker
import random
import string

fake = Faker()
size = 25

for i in range(size):
	firstname = fake.name().split(' ')[0]
	fake_user = Users(name = firstname, address = fake.address(), balance = random.randrange(21, 100000))
	fake_user.save()
	print('Saved' + str(i + 1))

for j in range(size):
	ticker = random.sample(string.ascii_uppercase, random.randrange(2,5))
	stockprice = float(random.randrange(2, 391)) + round(random.random(),2)
	fake_stock = Stocks(symbol = ''.join(ticker), price = stockprice)
	fake_stock.save()
	print('Saved' + str(j + 1))
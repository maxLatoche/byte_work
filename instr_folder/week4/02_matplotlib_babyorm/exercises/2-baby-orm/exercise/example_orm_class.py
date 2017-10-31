import sqlite3

conn = sqlite3.connect('babyorm.db')
c = conn.cursor()

class Model:
	def __init__(self, **kwargs):
		for i in kwargs.keys():
			setattr(self, i, kwargs[i])

	@classmethod
	def all(cls):
		query = "SELECT * FROM {}".format(cls.__name__)
		c.execute(query)
		conn.commit()
		object_list = []
		for i in c.fetchall():
			blargs = {str(c.description[j][0]):i[j] for j in range(len(i))}
			object_list.append(cls(**blargs))
		return object_list

### Don't touch the code for these.
class Users(Model):
	pass

class Stocks(Model):
	pass

if __name__ == '__main__':
	timmy = Users(name='Timmy', id=45, house='tree')
	print(timmy.id, timmy.house)

	print("Stocks.all()")
	for i in Stocks.all():
		print(i.id, i.symbol, i.price)

	conn.close()

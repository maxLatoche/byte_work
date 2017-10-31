import sqlite3
from collections import OrderedDict

class Model:
	def __init__(self, **kwargs):
		for arg in kwargs:
			setattr(self, arg, kwargs[arg])

	def save(self):
		conn = sqlite3.connect('babyorm.db')
		c = conn.cursor()

		attrs = self.__make_ordered_dict()
		values = self.__get_attr_values(attrs)

		if(hasattr(self, 'id')):
			statement = self.__build_update_statement(attrs)
			values.append(self.id)
			c.execute(statement, values)
		else:
			statement = self.__build_insert_statement(attrs)
			c.execute(statement, values)
			self.id = c.lastrowid

		conn.commit()
		conn.close()
		return True

	def __get_attr_values(self, attrs):
		values = []
		for key in attrs:
			values.append(attrs[key])
		return values

	def __build_update_statement(self, attrs):
		counter = 0
		statement = "UPDATE {0} SET ".format(type(self).__name__)
		for key in attrs:
			statement += str(key)
			statement += "=(?)"
			if(counter != len(attrs) - 1):
				statement += ', '
				counter += 1

		statement += " WHERE id = (?)"
		return statement

	def __build_insert_statement(self, attrs):
		columns = ''
		question_marks = ''
		counter = 0
		for key in attrs:
			columns += str(key)
			question_marks += '?'
			if(counter != len(attrs) - 1):
				columns += ','
				question_marks += ','
				counter += 1

		statement = "INSERT INTO {0}({1}) VALUES ({2})".format(type(self).__name__, columns, question_marks)
		return statement

	def __make_ordered_dict(self):
		attrs = OrderedDict()
		for key in self.__dict__:
			if(str(key) == 'id'):
				continue
			else:
				attrs[key] = self.__dict__[key]
		return attrs

	@classmethod
	def all(self):
		conn = sqlite3.connect('babyorm.db')
		c = conn.cursor()
		statement = 'SELECT * FROM {0}'.format(self.__name__)
		c.execute(statement)
		column_names = self.__get_column_names(c.description)

		obj_array = self.__make_objects(c.fetchall(), column_names)
		conn.close()
		return obj_array

	@classmethod
	def __get_column_names(self, description):
		column_names = []
		for t in description:
			column_names.append(t[0])
		return column_names

	@classmethod
	def __make_objects(self, sql_return, column_names):
		obj_array = []

		for obj in sql_return:
			index = 0
			class_obj = {}
			for arg in column_names:
				class_obj[arg] = obj[index]
				index += 1

			obj_array.append(self(**class_obj))

		return obj_array

	@classmethod
	def create(self, **kwargs):
		new_instance = self(**kwargs)
		new_instance.save()
		return new_instance

	@classmethod
	def filter(self, **kwargs):
		statement_obj = self.__build_condition(kwargs)
		conn = sqlite3.connect('babyorm.db')
		c = conn.cursor()
		statement = 'SELECT * FROM {0} WHERE {1}'.format(self.__name__, statement_obj['condition'])
		c.execute(statement, statement_obj['values'])
		column_names = self.__get_column_names(c.description)
		obj_array = self.__make_objects(c.fetchall(), column_names)
		conn.close()
		if(len(obj_array) == 0):
			return None
		else:
			return obj_array

	@classmethod
	def get(self, **kwargs):
		statement_obj = self.__build_condition(kwargs)
		conn = sqlite3.connect('babyorm.db')
		c = conn.cursor()
		statement = 'SELECT * FROM {0} WHERE {1} LIMIT 1'.format(self.__name__, statement_obj['condition'])
		c.execute(statement, statement_obj['values'])
		column_names = self.__get_column_names(c.description)
		obj_array = self.__make_objects(c.fetchall(), column_names)
		conn.close()
		if(len(obj_array) == 0):
			return None
		else:
			return obj_array[0]

	@staticmethod
	def __build_condition(kwargs):
		condition = ''
		values = []
		counter = 0
		for arg in kwargs:
			condition += str(arg) + "=" + "(?)"
			values.append(kwargs[arg])
			if(counter != len(kwargs) - 1):
				condition += " AND "
				counter += 1
		return {"condition":condition, "values":values}

	@classmethod
	def delete():
		pass

	@classmethod
	def order_by():
		pass

	@classmethod
	def count():
		pass

class Users(Model):
	pass

class Stocks(Model):
	pass
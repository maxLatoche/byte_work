'''

class Movie:
	def __init__(self, cast, characters, release, genre):
		self.cast = cast
		self.characters
		self.release
		self.release

	def get_cast(self):
		return "{cast} is in the cast".format(cast = self.cast)

	def get_characters(self):
		return "{characters} are the characters".format(cast = self.characters)

	def get_release(self):
		return "{release}".format(cast = self.cast)

	def get_cast(self):
		return "{cast} is in the cast".format(cast = self.cast)


class Athlete:

	legs = 2
	arms = 2
	is_rich = True

	def __init__(self, name, sport, team, height, weight):
		self.name = name
		self.sport = sport
		self.team = team
		self.height = height
		self.weight = weight

S_Crosby = Athlete("Sidney", "hockey", "penguins", 6.1, 200)
'''

class Vehicle:
	motor_type = "combustion"

	def __init__(self, make, wheels):
		self.make = make
		self.wheels = wheels

class Car(Vehicle):

	def __init__(self, make, wheels, model):
		super().__init__(self, make, wheels)
		self.model = model

	def get_model:
		return self.model

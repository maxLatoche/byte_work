# class Car:
#     """
#     We are making a car class
#     """

#     def __init__(self, make, model, year = 3000):
#         self.make = make
#         self.model = model
#         self.year = year
#         print("You made a new car")

#     def hello(self):
#         print("You have started your car, it is a {year} {make} {model}".format(year = self.year, make = self.make, model = self.model))


# my_car = Car(make = "Bugatti", model = "Veyron", year = 2015)
# your_car = Car("Protege", "Mazda", 1991)
# julissa_car = Car("Protege", "Mazda")

# my_car.hello()




# class Movie:

#     def __init__(self, cast, characters, release, genre):
#         self.cast = cast
#         self.characters = characters
#         self.release = release
#         self.genre = genre

#     def get_cast(self):
#         return self.cast

#     def get_characters(self):
#         return self.characters

#     def get_release(self):
#         return self.release

#     def get_genre(self):
#         return self.genre

# people = ["Robert Downey Jr.", "Chris Evans", "Mark Ruffalo", "Chris Hemsworth", "Scarlett Johansson", "Jeremy Renner", "Tom Hiddleston"]

# heroes = ["Iron Man", "Captain America", "The Hulk", "Thor", "Black Widow", "Hawkeye", "Loki"]

# the_avengers = Movie(people, heroes , "April 11, 2012", "Fantasy/Science fiction film")

# print(the_avengers.get_characters())




# class Show:

#     cinema = "Hollywood"

#     def __init__(self, cast, characters, release, genre):
#         self.cast = cast
#         self.characters = characters
#         self.release = release
#         self.genre = genre

#     def give_cast(self):
#         return self.cast

#     def give_char(self):
#         return self.characters

#     def give_date(self):
#         return self.release
    
#     def give_genre(self):
#         return self.genre

# p_cast = "Damian Lewis, Paul Giammatti"
# p_char = "Bobby Axelrod, Chuck Rhoades"

# p_s_show = Show(p_cast , p_char , 2016, 'Drama')

# top_gun = Show("Tom Cruise, Val Kilmer", "Maverick, Iceman", 1986, "Action")

# aos = Show("Chloe Bennett, Clark Gregg, Ming-Na Wen", "Skye, Coulson, May", 2013, "Comic")


# print(p_s_show.cinema) 
# print(p_s_show.release)

# print(top_gun.cinema) 
# print(top_gun.release) 

# print(aos.cinema)
# print(aos.release)



# class Athlete:

#     arms = 2
#     legs = 2
#     is_rich = True

#     def __init__(self, sport, team, height, weight):
#         self.sport = sport
#         self.team = team
#         self.height = height
#         self.weight = weight
        
#     def get_info(self):
#         print("{} player for {}. He is {} and weighs {}".format(self.sport,self.team,self.height,self.weight))
        

# david_b = Athlete(sport = "Football", team = "LA Galaxy.", height = "6ft", weight = "165 lbs.")

# steve_nash = Athlete("Basketball", team='retired', height='6', weight="N/A")

# david_b.get_info()



# name = "Jason"

def hello():
    name = "Barry"

    print(name)
    return "Hello " + name

def goodbye():

    new_name = hello()
    
    return "Goodbye" + new_name

print(goodbye())
# print(hello())














# class TV_Show:
#     def __init__(self, show, cast, characters, release, genre):
#         self.show = show
#         self.cast = cast
#         self.characters  = characters
#         self.release = release
#         self.genre = genre
#     def my_show(self):
#         return ("My Favorite Show Is {}".format(self.show))
#     def my_cast(self):
#         pass
#     def my_characters(self):
#         pass
#     def my_release(self):
#         pass

#     def my_genre(self):
#         pass

# jasons_show = TV_Show(show = "The Black Donnellys", cast = ["I don't remember", "Olivia Wilde"], characters = ["Donnelly Brothers", "some bad irish people", "some bad italian people"], release = 2008, genre = "Badass")

# print(jasons_show.my_show())




# class Car:
#     """
#         We're making a class for Cars
#         the car is my lover
#     """
#     wheels = 4 # this is a class variable    
#     def __init__(self, make, model, year):
#         self.make   =   make
#         self.model  =   model #this is an instance variable
#         self.year   =   year

#     def hello(self):
#         print("You have a started your car, it is a {year} {make} {model}".format(year = self.year, make=self.make, model=self.model))

#     def how_many(self):
#         print("You have {x} wheels".format(x = self.wheels))

#     def blah(self, x):
#         print("this is ", x)


# my_car = Car(make="Bugatti", model="Veyron", year="2080")
# henry_car = Car(make="Audi", model="R8", year="2016")
# my_car.hello()
# my_car.how_many()
# henry_car.hello()
# henry_car.how_many()
























# class Athlete:

#     legs = 2
#     arms = 2
#     is_rich = True

#     def __init__(self, name, sport, team, weight):
#         self.name = name
#         self.team = team
#         self.sport = sport
#         self.weight = weight

#     def appendages(self):
#         return(self.arms + self.legs)

# jeff = Athlete(name='jeff', sport='swimming', team='sharks', weight=500)
# jason = Athlete(name='jason', sport='crickey', team='spellers', weight=500)

# print(jeff.appendages())



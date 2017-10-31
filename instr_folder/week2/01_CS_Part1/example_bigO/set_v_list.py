import string
import timeit

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def make_moby():
    my_list_of_moby_dick = []

    with open('mobydick.txt') as lines:
        for line in lines:
            if line != "\n":
                line = line.translate(string.punctuation).split(" ")
                for word in line:
                    if word != '\n':
                        my_list_of_moby_dick.append(word.lower())

    return my_list_of_moby_dick

def make_dictionary():
    my_list_of_words = []
    with open('words.txt') as fp:
        for line in fp:
            my_list_of_words.append(line.rstrip()) #rstrip returns a copy of the string but all characters are removed at the end. By default this is targeting white space
    return my_list_of_words

def spell_check(list_of_potential_misspelleds, list_of_corrently_spelled):
    misspelled_words = []
    for word in list_of_potential_misspelleds:
        if word not in list_of_corrently_spelled:
            misspelled_words.append(word)

# makes dictionary of all words in moby
moby = make_moby()
print("done making moby")
my_dict = make_dictionary()
print("done making dictionary")


###### Example 1
###### How fast will this run? Does commenting out "moby" change the timeit printed?

# spell check list
# my_list = ['jeff', 'is', 'a', 'teacher', 'at', 'byte', 'hakuna', 'matata']
# wrapped = wrapper(spell_check, my_list, my_dict)
# print(timeit.timeit(wrapped, number=100))



###### Example 2
###### Do we think this will run faster or slower than previously? 
###### The text file "moby" has 15000 lines
###### The text file "words" has 106000 lines

# specll check moby
wrapped = wrapper(spell_check, moby, my_dict)
print(timeit.timeit(wrapped, number=2))

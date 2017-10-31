import sqlite3
from collections import OrderedDict

class Model:
    def __init__(self, **kwargs):
        for arg in kwargs:
            setattr(self, arg, kwargs[arg])
            
    def save(self):
        conn = sqlite3.connect('orm.sqlite3')
        cursor = conn.cursor()

        attribute_keys_string = "("
        question_marks = "("
        count = 0
        for key in self.__dict__:
            if(count == 0):
                attribute_keys_string += (key)
                question_marks += "(?)"
            else:
                attribute_keys_string += (", " + key)
                question_marks += ", (?)"
            count += 1
        attribute_keys_string += ")"
        question_marks += ")"


        if(hasattr(self, 'id')):
            cursor.execute("UPDATE {type(self).__name__} SET {attribute_keys_string}  WHERE id = (?);".format(**locals()), list(self.__dict__.values()) + [self.id])
        else:
            exec_string = "INSERT INTO {0} {1} VALUES {2};".format(type(self).__name__, attribute_keys_string, question_marks)
            cursor.execute(exec_string, list(self.__dict__.values()))
            conn.commit()
            conn.close()
            print(exec_string)

car = Model(name='Prius', company='Toyota', year=2010)
print(type(car).__name__)
#
# string = ""
# for key in car.__dict__:
#     string += (key + "=(?),")
#
# print([type(car).__name__] + list(car.__dict__.values()))

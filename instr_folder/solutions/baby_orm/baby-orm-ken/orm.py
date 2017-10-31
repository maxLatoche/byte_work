from collections import OrderedDict
import sqlite3

db = sqlite3.connect('babyorm.db')
cur = db.cursor()

class Model:
  def __init__(self, **kwargs):
    for arg in kwargs:
      setattr(self, arg, kwargs[arg])

  @classmethod
  def __create_instances(cls, objects):
    instances = [cls(**obj) for obj in objects]
    return instances

  @classmethod
  def __construct_conditions(cls, **kwargs):
    conditions = ["{}='{}'".format(value, kwargs[value]) for value in kwargs]
    return " AND ".join(conditions)

  @classmethod
  def all(cls, **kwargs):
    sql_string = 'SELECT * FROM {0}'.format(cls.__name__)
    cur.execute(sql_string)
    column_names = [x[0] for x in cur.description]
    rows = cur.fetchall()
    dicts = [dict(zip(column_names, x)) for x in rows]
    all = cls.__create_instances(dicts)
    return all

  @classmethod
  def get(cls, **kwargs):
    sql_string = "SELECT * FROM {} WHERE ".format(cls.__name__)
    sql_string += cls.__construct_conditions(**kwargs)
    sql_string += " LIMIT 1"
    cur.execute(sql_string)
    rows = cur.fetchall()
    column_names = [x[0] for x in cur.description]
    dicts = [dict(zip(column_names, x)) for x in rows]
    one = cls.__create_instances(dicts)
    # Need to handle if one is empty
    return one[0]



###don't touch the code for these
class Users(Model):
  pass

class Stocks(Model):
  pass

users = Users.all()
cinn = Users.get(id=11)
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simple_migrations.settings')

import django
django.setup()

# Import the models that you will need here


def seed():
  pass


def add_employee():
  pass


if __name__ == '__main__':
    print "Starting seed script..."
    seed()


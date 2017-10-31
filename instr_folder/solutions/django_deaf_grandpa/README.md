Week 5 Day 1
============

Welcome to Week 5! We'll be starting web and the Django framework this week.

Things to do:  
### Install Postgres.
#### On Ubuntu
```bash
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib libpq-dev python-dev python3-dev
```
#### On Fedora
```
sudo yum update
sudo yum install postgresql-server postgresql-contrib postgresql-devel python-devel python3-devel libevent-devel
```
### On OS X

[In this tutorial, you will learn how to install PostgreSQL on a Mac with the Postgres Graphic Installer, the Postgres.app Mac app, and with Homebrew.](http://www.gotealeaf.com/blog/how-to-install-postgresql-on-a-mac)

#### Further Configuration (all distros)
```
sudo su postgres
###You should now be at the postgres user bash prompt
psql
###You should now be in the psql prompt -> postgres=#
CREATE ROLE <your os username> WITH login password '<your password>';
ALTER ROLE <your os username> WITH superuser createdb createrole;
\q
exit
###Should be good to go
```
#### If you are getting a  FATAL: Ident authentication failed for user error
```
sudo su postgres
psql
SHOW hba_conf; ###copy the output of this
\q
open copied output in text editor
change the words "ident" to "trust" so these lines match
local	all	all	trust
host	all	127.0.0.1/32	trust
save, exit
service postgresql restart ###restart
```

#### Virtualenv

Now you need to install Virtualenv. `sudo pip3 install virtualenv`

Inside each exercise, make a new folder called `venv`. Then `virtualenv venv`

Your folder structure should look like this:
```
1-deaf-grandpa  
    project
        project
        deafgrandpa
        venv
        manage.py
```
To enter the virtual env, type `source venv/bin/activate`

To install Django and the Postgres Driver to the virtualenv: `pip3 install django-toolbelt` - NO SUDO!

Good practice is to take a freeze frame of your dependencies, that can later be used to install all the requirements.
```
pip3 freeze > requirements.txt
```
To leave the virtual environment, type `deactivate`

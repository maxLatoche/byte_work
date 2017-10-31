Anagram Server
===============

We're going to be building an [anagram](http://en.wikipedia.org/wiki/Anagram) server. 

Did you know your computer comes with a huge word dictionary? It's in `/usr/share/dict/words`. Do some of your unix ninja moves on it - how many words does it have?

###0: Import the dictionary

We're going to be importing this dictionary into a database. We need to search it to find anagrams for words that users input.

Go to `project/settings.py` and under DATABASES, enter your username and password.

Now, create your postgres database:

		createdb anagrams
		
For reference, if you ever want to drop your db:

		dropdb anagrams

Create the Word model in `anagrams/models.py` - for now, we only need one char field called "word".

Migrate your models, and we're almost ready to go.

		python3 manage.py makemigrations anagrams
		python3 manage.py migrate 

Now take all the words in the unix word list and seed your DB with them. Make sure you print the contents of the word list first so you know what you're getting.

Put this functionality in your models, or create a new file in the anagrams directory. 

Check your db in the shell. Are your words all in there?

###2: Write your anagram code

Open `anagrams/urls.py` and `anagrams/views.py`.

Line 8 in urls is routing the traffic to our index view function.

The first argument is regex to match the users input. It expects one or more of any word character, captures it in the group and is passed as variable word to the index view function.

[Read this on URL routing in Django](https://docs.djangoproject.com/en/dev/topics/http/urls/). Seriously, do it.

Start the server. You should see something like this:

<img src = "http://i.imgur.com/UXptpgq.png">

Now it's your job to write the logic to scan the words in the DB and get all the anagrams for the user's word. You'll need to write that code in the index function. 

There is a template in `anagrams/templates/anagrams`. Read about [Django templating](https://docs.djangoproject.com/en/dev/topics/templates/) to display your anagrams. 

Also read about [render](https://docs.djangoproject.com/en/dev/topics/http/shortcuts/#django.shortcuts.render)

###3: Benchmarking

How fast is your site? Write a benchmark function for searching your database that prints the time the request took to the console.

###4: GOTTA GO FAST

Improve the speed of your app using an index and maybe another field...what are you going to store and index to make it faster? 

Migrate again to commit your schema changes to the database. Rewrite your seed also if you made any changes. Run your server and get the benchmark. How much time did you improve by? 


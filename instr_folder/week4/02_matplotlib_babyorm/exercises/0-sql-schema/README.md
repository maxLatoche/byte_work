SQL Relationships Refresher
===========================

This one *should* be easy, but make sure you do it.

`CREATE TABLE`s in SQLite to model the following relationships.

### Model a Many-to-One Relationship
* A *person* has a name, nickname, date of birth, and many laptops.
* A *laptop* has a model, amount of RAM, and belongs to one person.

### Model a Many-to-Many Relationship
* A *movie* has a name, a release date, and many actors.
* An *actor* has a name, date of birth, and many movies.


You may use Python with `import sqlite3` or raw SQL.

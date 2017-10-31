McNugget Numbers
==================

#### Description

In the 1980s, while eating McDonald's with his son, mathematician Henri Picciotto reasoned [McNugget Numbers](http://en.wikipedia.org/wiki/Coin_problem#McNugget_numbers).

At McDonalds’ Restaurants at the time, Chicken McNugget meals were available in sizes of 6 McNuggets, 9 McNuggets, or 20 McNuggets.

A number is a McNugget number if it can be the sum of the number of McNuggets purchased in an order before eating any of them.

Some Examples:

        20 + 6 == 26
        9 + 9 + 9 + 9 + 9 == 45
        20 + 9 + 6 == 35
        ...etc

###Challenge

* You should write a function which will return a list that contains all numbers which are NOT McNugget number.
	* All numbers that cannot be created with the 6,9,20 combination

### BONUS

* Determine all numbers that are not McNugget numbers using today's order sizes - `4`, `6`, `10`, `20` and `40`.

### HINT

* Use a while loop

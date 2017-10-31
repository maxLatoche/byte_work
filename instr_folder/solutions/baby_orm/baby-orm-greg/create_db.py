import sqlite3

conn = sqlite3.connect('babyorm.db')
c = conn.cursor()
c.execute('''DROP TABLE IF EXISTS `Users`;''')
c.execute("""CREATE TABLE `Users` (
		`id` INTEGER,
		`name` VARCHAR,
		`address` VARCHAR,
		`balance` REAL,
		PRIMARY KEY (`id`)
	)""")

c.execute('''DROP TABLE IF EXISTS `Stocks`;''')
c.execute("""CREATE TABLE `Stocks` (
		`id` INTEGER,
		`symbol` VARCHAR,
		`price` REAL,
		PRIMARY KEY (`id`)
	)""")
conn.commit()
conn.close()
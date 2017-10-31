import sqlite3

db = 'living.db'

BUILDINGS =[
    ["Empire State", "New York", 1930],
    ["Bradbury", "Los Angeles", 1893],
    ["White House", "Washington D.C.", 1800],
]

RESIDENTS = [
    ["Jay", "Z", 100000,1],
    ["Kobe", "Bryant", 90000,2],
    ["Barack", "Obama", 50000,3],
]
conn = sqlite3.connect(db)
c = conn.cursor()

print("Destroying old data")
c.execute("DELETE FROM buildings")
c.execute("DELETE FROM residents")

for building in BUILDINGS:
    c.execute("""
        INSERT INTO buildings ("name", "city", "build_year") VALUES (?, ?, ?, )""",(building[0], building[1], building[2]))

conn.commit()

for resident in RESIDENTS:
    c.execute("""
        INSERT INTO residents ("first_name", "last_name", "rent", "building_id") VALUES (?, ?, ?, ?)""",(resident[0], resident[1], resident[2], resident[3]))

conn.commit()

c.close()
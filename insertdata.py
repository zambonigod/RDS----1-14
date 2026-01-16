import sqlite3

conn = sqlite3.connect('points.db')

cursor = conn.cursor()

query = """
insert into points (x,y) 
values 
(8,9),
(10,11),
(12,13);
"""

cursor.execute(query)
conn.commit()
conn.close()
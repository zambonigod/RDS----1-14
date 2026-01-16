import sqlite3

conn = sqlite3.connect('points.db')

cursor = conn.cursor()

query = """
delete from points where id > 3;
"""

cursor.execute(query)
conn.commit()
conn.close()
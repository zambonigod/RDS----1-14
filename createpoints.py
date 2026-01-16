import sqlite3

conn = sqlite3.connect('points.db')

cursor = conn.cursor()

query = """
create table if not exists points(
    id integer primary key autoincrement,
    x real,
    y real
);

"""

cursor.execute(query)
conn.commit()
conn.close()
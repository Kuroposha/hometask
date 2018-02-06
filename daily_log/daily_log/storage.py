import os.path as Path
import sqlite3


sql_dir = Path.join(Path.dirname(__file__), 'resourses', 'schema.sql')

with sqlite3.connect(':memory:') as conn, open(sql_dir) as f:

    conn.executescript(f.read())



    # conn.execute(sql_dir)
    # try:
    #     coursor = conn.execute(sql_dir)
    #     print(cursor.fetchall())
    # except sqlite3.Error as e:
    #     print(e)

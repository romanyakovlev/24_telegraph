import sqlite3
from settings import path_to_db_file

conn = sqlite3.connect(path_to_db_file)
c = conn.cursor()
c.execute('''CREATE TABLE telegraphs
                (post_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                header text, signature text, body text)''')
conn.commit()
conn.close()

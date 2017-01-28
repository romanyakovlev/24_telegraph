import sqlite3


conn = sqlite3.connect('telegraph.db')
c = conn.cursor()
c.execute('''CREATE TABLE telegraphs
          (post_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
           header text, signature text, body text)''')
c.execute('''INSERT INTO telegraphs(header, signature, body)
                VALUES ('Example','Example','Example')''')
conn.commit()
conn.close()

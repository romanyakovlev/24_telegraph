import sqlite3


conn = sqlite3.connect('telegraph.db')

c = conn.cursor()

c.execute('''CREATE TABLE telegraphs
          (header text UNIQUE, signature text, body text)''')

c.execute("INSERT INTO telegraphs VALUES ('header1','title1','body1')")

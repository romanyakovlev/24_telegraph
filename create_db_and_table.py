import psycopg2
from settings import path_to_db_file

conn = psycopg2.connect("dbname='test_python' user='roman1' host='localhost' password='password'" )
c = conn.cursor()
c.execute('''CREATE TABLE telegraphs
                (post_id SERIAL NOT NULL,
                header text, signature text, body text)''')
conn.commit()
conn.close()

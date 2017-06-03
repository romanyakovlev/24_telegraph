import psycopg2
from settings import url

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

c = conn.cursor()
c.execute('''CREATE TABLE telegraphs
                (post_id SERIAL NOT NULL,
                header text, signature text, body text)''')
conn.commit()
conn.close()

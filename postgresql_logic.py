from flask import Flask, g
import psycopg2
import psycopg2.extras
from settings import app, url


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
        )
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def query_db(query, args=(), one=False, lastrowid_show=False):
    db = get_db()
    if lastrowid_show:
        cur = db.cursor()
    else:
        cur = db.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(query, args)
    rv = cur.fetchall()
    db.commit()
    cur.close()
    if lastrowid_show is True:
        return rv[0][0]
    return rv[0]


def get_post(post_id):
    return query_db("SELECT * FROM telegraphs WHERE post_id=%s",
                               (post_id,), one=True)


def update_post(post_dict):
    query_db("UPDATE telegraphs SET signature=%s,body=%s,header=%s WHERE post_id=%s RETURNING post_id;",
             (post_dict['signature'], post_dict['body'], post_dict['header'],
              post_dict['post_id']), one=True)
    b = query_db("SELECT * FROM telegraphs WHERE post_id=%s",
                 (post_dict['post_id'],), one=True)
    return b


def create_post(post_dict):
    return query_db("INSERT INTO telegraphs(header, signature, body) VALUES (%s, %s, %s) RETURNING post_id;",
                               (post_dict['header'],post_dict['signature'],post_dict['body']),
                                one=True, lastrowid_show=True)

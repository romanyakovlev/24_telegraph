from flask import Flask, g
import sqlite3


app = Flask(__name__)


DATABASE = 'telegraph.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def query_db(query, args=(), one=False):
    db = get_db()
    cur = db.execute(query, args)
    rv = cur.fetchall()
    db.commit()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def get_header(header):
    return query_db("SELECT * FROM telegraphs WHERE header=?",
                    (header,), one=True)


def update_row(post_dict):
    query_db("UPDATE telegraphs SET signature=?,body=? WHERE header=?",
             (post_dict['signature'], post_dict['body'],
              post_dict['header']), one=True)
    b = query_db("SELECT * FROM telegraphs WHERE header=?",
                 (post_dict['header'],), one=True)
    print(b['body'])
    return b

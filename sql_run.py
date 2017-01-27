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


def query_db(query, args=(), one=False, lastrowid_show=False):
    db = get_db()
    cur = db.execute(query, args)
    rv = cur.fetchall()
    db.commit()
    post_lastrowid = cur.lastrowid
    cur.close()
    if lastrowid_show is True:
        return post_lastrowid
    return (rv[0] if rv else None) if one else rv


def get_post(post_id):
    return query_db("SELECT * FROM telegraphs WHERE post_id=?",
                    (post_id,), one=True)


def update_row(post_dict):
    query_db("UPDATE telegraphs SET signature=?,body=?,header=? WHERE post_id=?",
             (post_dict['signature'], post_dict['body'], post_dict['header'],
              post_dict['post_id']), one=True)
    b = query_db("SELECT * FROM telegraphs WHERE post_id=?",
                 (post_dict['post_id'],), one=True)
    return b


def create_post(post_dict):
    return query_db("INSERT INTO telegraphs(header, signature, body) VALUES (?,?,?)",
                               (post_dict['header'],post_dict['signature'],post_dict['body']),
                                one=True, lastrowid_show=True)

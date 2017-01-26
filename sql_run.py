import sqlite3


def get_header(header):
    conn = sqlite3.connect('telegraph.db')
    c = conn.cursor()
    post_info = c.execute("SELECT * FROM telegraphs WHERE header=?",
                          (header,)).fetchone()
    conn.commit()
    conn.close()
    if not post_info:
        return None
    post_dict = {'header':  post_info[0], 'signature': post_info[1],
                 'body': post_info[2]}
    return post_dict


def update_row(post_dict):
    conn = sqlite3.connect('telegraph.db')
    c = conn.cursor()
    print(post_dict['signature'])
    c.execute("UPDATE telegraphs SET signature=?,body=? WHERE header=?",
              (post_dict['signature'], post_dict['body'], post_dict['header']))
    post_info = c.execute("SELECT * FROM telegraphs WHERE header=?",
                          (post_dict['header'],)).fetchone()
    conn.commit()
    conn.close()
    post_dict_ = {'header':  post_info[0], 'signature': post_info[1],
                  'body': post_info[2]}
    return post_dict_

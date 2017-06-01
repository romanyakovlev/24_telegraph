from flask import render_template, request, jsonify, make_response, abort, send_from_directory
from sqlite_logic import get_post, update_post, create_post
from settings import app, f
import json
import os


def update_or_create_cookie_list(post_id):
    cookie_data = request.cookies.get('post_ids')
    if cookie_data:
        post_id_cookie_list = json.loads(cookie_data)
    else:
        post_id_cookie_list = []
    if post_id_cookie_list:
        post_id_cookie_list.append(post_id)
    else:
        post_id_cookie_list = [post_id]
    return post_id_cookie_list


def check_post_id_in_list(post_id):
    cookie_data = request.cookies.get('post_ids')
    if cookie_data:
        post_id_cookie_list = json.loads(cookie_data)
    else:
        post_id_cookie_list = []
    can_you_edit = bool(int(post_id) in post_id_cookie_list)
    return can_you_edit

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/', methods=['GET', 'POST'])
def start_page():
    if request.method == "GET":
        return render_template('start_page.html')
    if request.method == "POST":
        post_id = create_post(request.form)
        post_header = get_post(post_id)['header']
        response = make_response(jsonify({'post_id': post_id, 'post_header': post_header}))
        post_id_cookie_list = update_or_create_cookie_list(post_id)
        response.set_cookie('post_ids', json.dumps(post_id_cookie_list))
        return response


@app.route('/<post_id>', methods=['GET', 'POST'])
def post_page(post_id):
    if request.method == "GET":

        post_dict = get_post(post_id)
        print(post_dict)
        if not post_dict:
            abort(404)
        can_you_edit = check_post_id_in_list(post_id)
        return render_template('post_page.html', can_you_edit=can_you_edit, **post_dict)
    if request.method == "POST":
        updated_form_dict = update_post(request.form)
        return jsonify(**updated_form_dict)


if __name__ == "__main__":
     port = int(os.environ.get("PORT", 5000))
     app.run(host='0.0.0.0', port=port)

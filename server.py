from flask import Flask, render_template, request, jsonify
from sql_run import get_header, update_row

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == "GET":
        return render_template('form.html')
    if request.method == "POST":
        return jsonify(**request.form)


@app.route('/<post_id>', methods=['GET', 'POST'])
def post(post_id):
    if request.method == "GET":
        post_dict = get_header(post_id)
        if not post_dict:
            return 'No {} in base'.format(post_id)
        print(post_dict)
        return render_template('post_page.html', **post_dict)
    if request.method == "POST":
        updated_form_dict = update_row(**request.form)
        print(updated_form_dict)
        return jsonify(**updated_form_dict)


if __name__ == "__main__":
    app.run()

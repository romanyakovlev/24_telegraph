from flask import Flask, render_template, request, jsonify
from sql_run import get_post, update_row, create_post

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == "GET":
        return render_template('form.html')
    if request.method == "POST":
        post_id = create_post(request.form)
        return jsonify({'post_id':post_id})


@app.route('/json/post/<post_id>', methods=['GET'])
def get_post_json(post_id):
    if request.method == "GET":
        post_dict = get_post(post_id)
        return jsonify(**post_dict)


@app.route('/post/<post_id>', methods=['GET', 'POST'])
def post_page(post_id):
    if request.method == "GET":
        return render_template('form.html')
    if request.method == "POST":
        updated_form_dict = update_row(request.form)
        return jsonify(**updated_form_dict)


if __name__ == "__main__":
    app.run(port=8000)

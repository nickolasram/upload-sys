import os
from flask import Flask, render_template, send_from_directory, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from user_file.user_file import User_file
from databaseManagement import repo, collection


ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = repo
# 16 meg limit
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
app.add_url_rule(
    "/uploads/<name>", endpoint="download_file", build_only=True
)
# app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            return User_file.upload(User_file, file)
    return render_template('home.html')

@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

# @app.route('/filescheck/')
# def filescheck():
#     output = ''
#     cursor = collection.find({})
#     for document in cursor:
#         output += document
#     return output
#     # return render_template('filescheck.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
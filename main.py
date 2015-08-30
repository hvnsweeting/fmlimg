import os

from flask import (Flask, url_for, request, redirect, render_template, flash)
from werkzeug import secure_filename

app = Flask(__name__)
app.debug = True
app.secret_key = 'asdlfjailsjfaweijlajf'

app.config['UPLOAD_DIR'] = "upload"


@app.route('/')
def list_files():
    '''Return list of uploaded files'''
    return render_template('list_files.html',
                           files=os.listdir(app.config['UPLOAD_DIR']))


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        try:
            f.save(os.path.join(app.config['UPLOAD_DIR'], filename))
        except Exception:
            flash('Failed to upload.')
            return redirect(url_for("upload_file"))
        flash('You were successfully uploaded file')
        return redirect(url_for("list_files"))
    else:
        return render_template("upload_form.html")

if __name__ == "__main__":
    app.run()

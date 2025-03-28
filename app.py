## Chapter 5
import os.path
from fileinput import filename

from Tools.scripts.make_ctype import method
# 5.1
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/form_login', methods=['GET', 'POST'])
def form_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username and password:
            if username=='admin' and password=='123456':
                return render_template('form_login.html', message='Login Succeed')
            else:
                return render_template('form_login.html', message='Login Failed')
        else:
            return render_template('form_login.html', message='Please input your username and password')
    else:
        return render_template('form_login.html')

@app.route('/form_upload_file', methods=['GET', 'POST'])
def form_upload_file():
    path = os.path.join(os.path.dirname(__file__), 'media/uploads')
    if not os.path.exists(path):
        os.makedirs(path)

    if request.method=='POST':
        files = request.files
        myfile = files['myfile']
        if myfile:
            filename = secure_filename((myfile.filename))
            file_name = os.path.join(path, filename)
            myfile.save(file_name)
    return render_template('form_upload.html')


if __name__=='__main__':
    app.run()
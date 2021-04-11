from flask import Flask, render_template, request, url_for, session , redirect, make_response
import requests
 

app = Flask(__name__)
app.secret_key = 'jd0291udjsoidn-ada-sbdadbp1'


@app.route('/')
@app.route('/index')
def index():
    if 'username' in session:
        return render_template('index.html', name='Привет ' + session['username'])
    else:
        return render_template('index.html')


@app.route('/register/', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        return render_template('index.html', name='Привет ' + session['username'])
    else:
        return render_template('register.html')


@app.route('/out/')
def out():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

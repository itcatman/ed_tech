from flask import Flask, render_template, request, url_for, session , redirect, make_response
import requests
 

app = Flask(__name__)
app.secret_key = 'jd0291udjsoidn-ada-sbdadbp1'


@app.route('/')
@app.route('/index')
def index():
    if 'username' in session:
        return render_template('index.html', name=session['username'])
    else:
        return render_template('index.html', name='No session')


@app.route('/register/', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        # session['password'] = request.form['password']
        return render_template('index.html', name=session['username'])
        #return redirect(url_for('index'))
    else:
        return render_template('register.html')
    
    #return render_template('register.html')



if __name__ == '__main__':
    app.run(debug=True)
    app.secret_key = 'super_secret_key'

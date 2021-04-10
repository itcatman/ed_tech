from flask import Flask, render_template, request, url_for
import datetime
import hashlib
import os
import json

app = Flask(__name__)
#Переменные
server_time = 0
Response_time = 0
total = 1
total_admin = 1

users = [
    {
        'id': 0,
        'name': 'Imran Akhmedov',
        'password': '123',
        'Class': '8',
        'birthday': '08.11.2006'
    } 
]

#Routes
@app.route('/')
def hello_world():
    return render_template('index.html', time = server_time)

@app.route('/status')
def status():
    server_time = datetime.datetime.now()
    Response_time = 'Coming soon'
    #    return 'Server time:' + str(server_time) + ' \nResponse time:' + str(Response_time) + ' '
    return render_template('/status/status.html', time=server_time, request=Response_time, total = total, total_admins = total_admin)
    
@app.route('/api/')
def api():
    return "It's work!!!"

@app.route('/api/users/register/',  methods=["GET"])
def api_register_Json():
    value = request.json
    return "JSON value sent: " + str(value)

@app.route('/register', methods=["GET", "POST"])
def register_user():
    if request.method == 'POST':
        mail = request.form.get('mail')
        name = request.form.get('name')
        password = request.form.get('password')

@app.route('/api/admin', methods=["GET", "POST"])
def admin_panel():
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        object = request.json
        return (object)
        
    else:
        return redirect("/")


if __name__ == '__main__':
    app.run()
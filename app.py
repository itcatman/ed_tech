from flask import Flask, render_template, request
import datetime
app = Flask(__name__)
#Переменные
server_time = 0
Response_time = 0

users = [
    {'id': 0,
     'name': 'Imran Akhmedov',
     'password': '123',
     'Class': '8',
     'birthday': '08.11.2006'}
    
]

#Routes
@app.route('/')
def hello_world():
    return render_template('/index.html', time = server_time)

@app.route('/status')
def status():
    server_time = datetime.datetime.now()
    Response_time = 'Coming soon'
    return 'Server time:' + str(server_time) + ' \nResponse time:' + str(Response_time) + ' '


@app.route('/api/')
def api():
    return "It's work!!!"

@app.route('/api/users/register/',  methods=["GET"])
def api_register_Json():
    value = request.json
    return "JSON value sent: " + str(value)



if __name__ == '__main__':
    app.run()
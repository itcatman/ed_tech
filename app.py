from flask import Flask

app = Flask(__name__)

#Переменные
server_time = datetime.datetime.now()
Response_time = 'Coming soon'

#Routes
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/status')
def status():
    return 'Server time:' + str(server_time) + ' '
    return 'Response time:' + str(Response_time) + ''
@app.route('/api/')

if __name__ == '__main__':
    app.run()
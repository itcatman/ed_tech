from flask import Flask, render_template
import datetime
app = Flask(__name__)
#Переменные
server_time = 0
Response_time = 0

#Routes
@app.route('/')
def hello_world():
    return render_template('/index.html', time = server_time)

@app.route('/status')
def status():
    server_time = datetime.datetime.now()
    Response_time = 'Coming soon'
    return 'Server time:' + str(server_time) + ' '
    return 'Response time:' + str(Response_time) + ''

@app.route('/api/')
def api():
    return "It's work!!!"

if __name__ == '__main__':
    app.run()
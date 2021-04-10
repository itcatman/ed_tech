from flask import Flask, render_template, request, url_for
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
    return render_template('index.html', time = server_time)

@app.route('/status')
def status():
    server_time = datetime.datetime.now()
    Response_time = 'Coming soon'
    #    return 'Server time:' + str(server_time) + ' \nResponse time:' + str(Response_time) + ' '
    return render_template('/status/status.html', time=server_time, request=Response_time )

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
        check = db.check_nickname(name)
        if check == 'OK':
            m_check = db.check_mail(mail)
            if m_check == 'OK':
                pass
            else:
                pass
        else:
            pass

def F():
    return redirect('https://google.com') 

if __name__ == '__main__':
    app.run()
    app.jinja_env.globals.update(F=F)
    #app.jinja_env.globals.update(F=F)
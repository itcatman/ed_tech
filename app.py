from flask import Flask, render_template, request 
import random, os


app = Flask(__name__)

users = [
    'Алия Анесина', 'Абдуллаев Рамазан', 'Викторий Багров', 'Али Шахбазов', 
    'Анюта Николаевна', 'Расул Камзаков', 'Мария Александровна', 'Миша Бабухин', 
    'Никита Баженов', 'Раиса Валерьевна', 'Витя Байков', 'Гаджи Магомедов'
]

head = random.choice(users)
name = head
level = 'Ученик lvl ' + str(random.randint(1, 10))


@app.route('/')
@app.route('/index')
def index():
        return render_template('index.html', head=head, name=name, level=level)


@app.route('/register/', methods=["GET", "POST"])
def login():
    return render_template('register.html')


@app.route('/main-2.html')
def interes():
    return render_template('main-2.html', name=name, level=level)


@app.route('/main-3.html')
def favorites():
    return render_template('main-3.html', name=name, level=level)


@app.route('/main-4.html')
def my_class():
    return render_template('main-4.html', name=name, level=level)


@app.route('/main-5.html')
def achivment():
    return render_template('main-5.html', name=name, level=level)



if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)

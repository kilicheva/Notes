from flask import Flask, render_template, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required, LoginManager, UserMixin
from Notes_DataBase import db


app = Flask(__name__)

app.config.update(
    SECRET_KEY='WOW SUCH SECRET'
)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


class User(UserMixin):
    def __init__(self, id):
        self.id = id


@login_manager.user_loader
def load_user(login=None):
    return User(login)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        row = db.users.get('login', request.form['login'])
        if not row:
            return render_template('login.html', error='Неправильный логин или пароль')

        if request.form['password'] == row.password:
            user = User(login)  # Создаем пользователя
            login_user(user)  # Логинем пользователя
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Неправильный логин или пароль')
    return render_template('login.html')


@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    get_data = db.post.get_all()

    if request.method == 'POST':
        db.post.put(dict(request.form))
        return redirect(url_for('index'))

    return render_template('index.html', data=get_data)


if __name__ ==  '__main__':
    app.run()
from data.db_functions import *

from data.Users import User
from data.Facts import Facts

from flask_login.login_manager import LoginManager
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required

from data.send_email import *

from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask import redirect

from data import config
import os
import hashlib

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)

db_session.global_init("data/db/db.sqlite")


def get_list_of_facts():
    session = db_session.create_session()
    return list(session.query(Facts).all())

def el_of_list_of_facts():
    config.NUM_OF_EL_OF_LIST_OF_FACTS += 2
    return config.NUM_OF_EL_OF_LIST_OF_FACTS - 1


@login_manager.user_loader
def load_user(user_id):
    session = db_session.create_session()
    return session.query(User).get(user_id)


class LoginForm(FlaskForm):
    email = StringField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class RegisterForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    email = StringField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')


class FactForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired()])
    content = StringField('Контент', validators=[DataRequired()])
    submit = SubmitField('Создать')


@app.route('/')
@app.route('/index')
def index():
    list_of_facts = get_list_of_facts()
    return render_template("index.html", list_of_fact=get_list_of_facts())


@app.route('/facts')
def facts():
    return render_template("fact.html", func=el_of_list_of_facts(get_list_of_facts()), list_of_facts=get_list_of_facts())


@app.route('/create_fact', methods=['GET', 'POST'])
def create_fact():
    form = FactForm()
    if form.validate_on_submit():
        add_facts(config.USER_ID, form.title.data, form.content.data)
        return render_template('create_fact.html', message='ФАКТ успешно добавлен', form=form, list_of_facts=get_list_of_facts())
    return render_template('create_fact.html', form=form, list_of_facts=get_list_of_facts())


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        user = session.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            config.USER_ID = user.id
            print(config.USER_ID)
            session.commit()
            return redirect("/")
        return render_template('login.html', message="Неправильный логин или пароль", form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        if session.query(User).filter(User.email == form.email.data).first() is not None:
            return render_template('register.html', message="Такой email уже зарегистрирован", form=form, list_of_facts=get_list_of_facts())
        elif session.query(User).filter(User.name == form.name.data).first() is not None:
            return render_template('register.html', message="Такое имя пользователя уже используется",
                                   form=form, list_of_facts=get_list_of_facts())
        send_email(form.email.data)
        config.NEEDED_CODE = get_code()
        password_hash = hashlib.new('md5', bytes(form.password.data, encoding='utf8'))

        config.USER_LIST = {'name': form.name.data, 'email': form.email.data, 'password_hash': password_hash.hexdigest()}
        session.commit()
        return render_template('submit_email.html', flag="wait", list_of_facts=get_list_of_facts())
    return render_template('register.html', title='Регистрация', form=form, list_of_facts=get_list_of_facts())


@app.route('/submit_email/<code>')
def submit_email(code):
    if code == config.NEEDED_CODE:
        session = db_session.create_session()
        add_user(config.USER_LIST['name'],
                 config.USER_LIST['email'],
                 config.USER_LIST['password_hash'])
        session.commit()
        send_for_admin([config.USER_LIST['name'], config.USER_LIST['email']])
        return render_template('submit_email.html', flag="code", list_of_facts=get_list_of_facts())
    elif code is None:
        return render_template('submit_email.html', flag="wait", list_of_facts=get_list_of_facts())
    else:
        return render_template('submit_email.html', flag="error", list_of_facts=get_list_of_facts())


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

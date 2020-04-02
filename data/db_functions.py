from data import db_session
from data import Users
from data.Users import User
from data import Facts


def add_user(name, email, password):
    user = Users.User()
    user.name = name
    user.email = email
    user.password = password
    session = db_session.create_session()
    session.add(user)
    session.commit()
    session.close()


def add_facts(user_id, title, content, author='Anonym'):
    session = db_session.create_session()

    fact = Facts.Facts()
    fact.user_id = user_id
    fact.title = title
    fact.content = content
    fact.author = author
    fact.user = session.query(User).filter(User.id == user_id).first()
    
    session.add(fact)
    session.commit()
    session.close()

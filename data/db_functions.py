from data import db_session
from data import Users
from data import Facts


def add_user(name, email, password):
    user = Users.User()
    user.name = name
    user.email = email
    user.password = password
    session = db_session.create_session()
    session.add(user)
    session.commit()


def add_facts(user_id, title, content):
    facts = Facts.Facts()
    facts.title = title
    facts.content = content
    facts.user_id = user_id
    session = db_session.create_session()
    session.add(facts)
    session.commit()

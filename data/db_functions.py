from data import db_session
from data import Users
from data import News


def add_user(name, email, password):
    user = Users.User()
    user.name = name
    user.email = email
    user.password = password
    session = db_session.create_session()
    session.add(user)
    session.commit()


def add_news(user, title, content, is_private=False):
    news = News.News()
    news.title = title
    news.content = content
    news.is_private = is_private
    news.user_id = user.id
    news.user = user
    user.news.append(news)

    session = db_session.create_session()
    session.commit()

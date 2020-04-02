import datetime
import sqlalchemy
from sqlalchemy import orm


from data.db_session import SqlAlchemyBase


class Facts(SqlAlchemyBase):
    __tablename__ = 'facts'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    content = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    author = sqlalchemy.Column(sqlalchemy.String, default='Anonym')

    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    user = orm.relation('User')

    def __repr__(self):
        return {'id': self.id, 'title': self.title, 'content': self.content,
         'created_date': created_date, 'author': self.author, 'user_id': user_id, 'user': user}

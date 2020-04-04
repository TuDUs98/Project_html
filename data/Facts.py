import datetime
import sqlalchemy
from sqlalchemy import orm


from data.db_session import SqlAlchemyBase


class Facts(SqlAlchemyBase):
    __tablename__ = 'facts'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    content = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.String, default=datetime.datetime.today().strftime('%H:%m %d/%m/%Y'))
    author = sqlalchemy.Column(sqlalchemy.String, default='Anonym')
    votes_true = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    votes_false = sqlalchemy.Column(sqlalchemy.Integer, default=0)

    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    user = orm.relation('User')

    def __repr__(self):
        return {'id': self.id, 'title': self.title, 'content': self.content,
         'created_date': created_date, 'author': self.author, 'user_id': user_id, 'user': user}

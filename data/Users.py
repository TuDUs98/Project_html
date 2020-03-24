import datetime
import sqlalchemy
from sqlalchemy import orm

from flask_login import UserMixin

from data.db_session import SqlAlchemyBase


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=False)
    password = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)

    facts = orm.relation("Facts", back_populates='user')

    def __repr__(self):
        return f"<User> {self.id} {self.name} {self.email} {self.password} {self.created_date}"

    def check_password(self, password):
        return self.password == password

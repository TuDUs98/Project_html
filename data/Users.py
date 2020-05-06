import datetime
import sqlalchemy
from sqlalchemy import orm

from flask_login import UserMixin

from data.db_session import SqlAlchemyBase

import hashlib


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=False)
    password = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    rating = sqlalchemy.Column(sqlalchemy.Integer, nullable=True, default=100)
    role = sqlalchemy.Column(sqlalchemy.String, default='User')
    # count_of_checked_votes = sqlalchemy.Column(sqlalchemy.Integer, default=0)

    facts = orm.relation("Facts", back_populates='user')
    votes = orm.relation("Votes", back_populates='user')

    def __repr__(self):
        return f"<User> {self.id} {self.name} {self.email} {self.created_date}"

    def check_password(self, password):
        password_hash = hashlib.new('md5', bytes(password, encoding='utf8'))
        return password_hash.hexdigest() == self.password

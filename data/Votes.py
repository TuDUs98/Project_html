import sqlalchemy
from sqlalchemy import orm

from data.db_session import SqlAlchemyBase


class Votes(SqlAlchemyBase):
	__tablename__ = 'votes'

	id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    value = sqlalchemy.Column(sqlalchemy.String)
	user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    user = orm.relation('User')
    fact_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("fact_id"))
    fact = orm.relation('Facts')

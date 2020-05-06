import sqlalchemy
from sqlalchemy import orm

from data.db_session import SqlAlchemyBase


class Votes(SqlAlchemyBase):
    __tablename__ = 'votes'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    value = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    user = orm.relation('User')
    fact_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("facts.id"))
    fact = orm.relation('Facts')

    def __repr__(self):
    	return f"<Vote> {self.id} {self.value} {self.user_id} {self.fact_id}"

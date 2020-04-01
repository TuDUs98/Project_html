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

    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    user = orm.relation('User')

    def __repr__(self):
        return f"<Fact> {self.id} {self.title} {self.content} {self.created_date} {self.user_id}"

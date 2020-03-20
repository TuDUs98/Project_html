from data import db_session
from data.db_functions import *

db_session.global_init("db/db.sqlite")

add_user('admin', 'kaktak.group@gmail.ru', '40221987')
from data import db_session
from data.db_functions import *

db_session.global_init("db/db.sqlite")
add_user('admin', 'qwerty@mail.ru', '1234')
add_user('admin2', 'qwerty2@mail.ru', '12342')
add_user('admin3', 'qwerty3@mail.ru', '12343')
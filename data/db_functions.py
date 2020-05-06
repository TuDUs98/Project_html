from data import db_session
from data.Users import User
from data.Facts import Facts
from data.Votes import Votes


def add_user(name, email, password):
    user = User()
    user.name = name
    user.email = email
    user.password = password
    session = db_session.create_session()
    session.add(user)
    session.commit()
    session.close()


def add_facts(user_id, title, content, author='Anonym'):
    session = db_session.create_session()

    fact = Facts()
    fact.user_id = user_id
    fact.title = title
    fact.content = content
    fact.author = author
    fact.user = session.query(User).filter(User.id == user_id).first()
    
    session.add(fact)
    session.commit()
    session.close()


def add_votes(user_id, fact_id, value):
    session = db_session.create_session()
    user = session.query(User).filter(User.id == user_id).first()
    fact = session.query(Facts).filter(Facts.id == fact_id).first()
    if user.role == 'Admin':
        fact.checked_value = value
        for vote in fact.votes:
            new_user = session.query(User).filter(User.id == vote.user_id).first()
            if vote.value == value:
                new_user.rating += 10
            else:
                new_user.rating -= 10
        fact.is_checked = True
    else:
        if not fact.is_checked:
            if value == 'true':
                fact.votes_true += 1
            else:
                fact.votes_false += 1

            vote = Votes()
            vote.user_id = user_id
            vote.fact_id = fact_id
            vote.value = value
            session.add(vote)
    
    session.commit()
    session.close()


def change_vote(user_id, fact_id, new_value):
    session = db_session.create_session()

    fact = session.query(Facts).filter(Facts.id == fact_id).first()
    vote = session.query(Votes).filter(Votes.user_id == user_id, Votes.fact_id == fact_id).first()
    if vote is not None and not fact.is_checked:
        if vote.value == 'false' and new_value == 'true':
            fact.votes_false -= 1
            fact.votes_true += 1

        elif vote.value == 'true' and new_value == 'false':
            fact.votes_false += 1
            fact.votes_true -= 1

        vote.value = new_value

        session.commit()
        session.close()

    else:
        session.close()
        add_votes(user_id, fact_id, new_value)
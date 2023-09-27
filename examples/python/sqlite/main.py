#!/usr/bin/env python

import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from utils import logging

import db
import datetime
import uuid

logger = logging.create_logger('main')

with db.Session() as session, session.begin():
    alice = session.query(db.User).filter_by(name='Alice').first()
    if alice:
        logger.info('Found user Alice: %s.' % alice)
        alice.is_active = not alice.is_active
    else:
        logger.info('Cannot find user Alice.')
        alice = db.User(name='Alice', birthday=datetime.date(1995, 1, 1))
        session.add(alice)
        logger.info('Add user Alice.')

logger.info('Create a list of users')

users = [db.User(name=str(uuid.uuid4())) for i in range(5)]

with db.Session() as session, session.begin():
    logger.info('Total count of users: %d' % session.query(db.User).count())
    session.add_all(users)

with db.Session() as session:
    count = session.query(db.User).count()
    logger.info(f'After adding {len(users)} users, the total count of users: {count}')

class Foo:
    def __init__(self, user):
        self.user = user

    def update(self, birthday):
        with db.Session() as session, session.begin():
            user = session.query(db.User).filter_by(id=self.user.id).first()
            user.birthday = birthday
            self.user = user

def find_alice():
    with db.Session() as session, session.begin():
        return session.query(db.User).filter_by(name='Alice').first()

alice = find_alice()
Foo(alice).update(datetime.date(1995, 2, 1))
alice = find_alice()
assert alice.birthday == datetime.date(1995, 2, 1)

with db.Session() as session:
    count = session.query(db.User).count()
    logger.info(f'Total count: {count}')

    result = session.query(db.User).limit(2).all()
    logger.info(len(result))

# if user:
#     print('Found user: %s' % user)
# else:
#     user = User(
#         name='baz',
#         passwd='bar'
#     )
#     session.add(user)
#     session.commit()
#
# session.close()
#
# res = session.query(User).all()
# print('Users: %s' % res)
#
# # user1 = session.query(User).filter_by(my_id=1).first()
# # print(user1)
#
# session.close()

from sqlalchemy import Column, UnicodeText, Boolean, Integer, DateTime

from sql import BASE, SESSION

from datetime import datetime


class AFK(BASE):
    __tablename__ = "afk_users"

    user_id = Column(Integer, primary_key=True)
    is_afk = Column(Boolean)
    reason = Column(UnicodeText, nullable=True)
    since = Column(DateTime)

    def __init__(self, user_id, since, reason=None, is_afk=True):
        self.user_id = user_id
        self.reason = reason if len(reason) != 0 else None
        self.is_afk = is_afk
        self.since = since


AFK.__table__.create(checkfirst=True)

AFK_USERS = {}


def is_afk(user_id):
    return user_id in AFK_USERS


def check_afk_status(user_id):
    if user_id in AFK_USERS:
        return True, AFK_USERS[user_id][0], AFK_USERS[user_id][1]
    return False, None, None


def set_afk(user_id, reason=None):
    try:
        curr = SESSION.query(AFK).get(user_id)
        if not curr:
            curr = AFK(user_id, datetime.utcnow(), reason, True)
        else:
            curr.is_afk = True
            curr.reason = reason
            if not curr.since:
                curr.since = datetime.utcnow()
        AFK_USERS[user_id] = [reason, curr.since]
        SESSION.add(curr)
        SESSION.commit()
    except:
        SESSION.rollback()
        raise


def rm_afk(user_id):
    if curr := SESSION.query(AFK).get(user_id):
        if user_id in AFK_USERS:
            del AFK_USERS[user_id]
            SESSION.delete(curr)
            SESSION.commit()
            return True
    SESSION.close()
    return False


def num_afk():
    return len(AFK_USERS)


def __load_afk_users():
    global AFK_USERS
    try:
        all_afk = SESSION.query(AFK).all()
        AFK_USERS = {user.user_id: [user.reason, user.since]
                     for user in all_afk if user.is_afk}
    finally:
        SESSION.close()


__load_afk_users()

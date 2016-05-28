from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String

from ..base import Base
from ..mixins import CRUDMixin

class User(Base, CRUDMixin):
    __tablename__ = "users"

    id = Column('user_id', Integer , primary_key=True)
    username = Column('username', String(20), unique=True, index=True)
    password = Column('password', String(50))
    email = Column('email', String(50), unique=True, index=True)
    created_at = Column('created_at' , DateTime)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.created_at = datetime.utcnow()

        def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.username)

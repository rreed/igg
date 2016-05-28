from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, DateTime
from sqlalchemy.ext.hybrid import hybrid_property

from ..base import Base
from ..mixins import CRUDMixin

class User(Base, CRUDMixin):
    __tablename__ = "users"

    id = Column('user_id', Integer , primary_key=True)
    username = Column('username', String(20), unique=True, index=True)
    _password = Column('password', String(50))
    email = Column('email', String(50), unique=True, index=True)
    created_at = Column('created_at', DateTime)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def _set_password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)

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

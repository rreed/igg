import bcrypt

from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, DateTime, Boolean

from ..base import Base
from ..mixins import CRUDMixin

class User(Base, CRUDMixin):
    __tablename__ = "users"

    id = Column('id', Integer , primary_key=True)
    username = Column('username', String(20), unique=True, index=True)
    password = Column('password', String(100))
    salt = Column('salt', String())
    email = Column('email', String(50), unique=True, index=True)
    created_at = Column('created_at', DateTime)
    admin = Column('admin', Boolean, default = False)

#see flask-login changelog 0.3.0: "is_authenticated" et al are now properties, 
#not methods because fuck your backwards compatibility (paraphrased)
    @property
    def is_authenticated(self):
        return True
    @property
    def is_active(self):
        return True
    @property
    def is_anonymous(self):
        return False

#I guess this should also be a property, but ehhh    
    def is_admin(self):
        return self.admin

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.username)

    def __unicode__(self):
        return self.username

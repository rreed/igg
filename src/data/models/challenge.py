from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String, Float

from ..base import Base
from ..mixins import CRUDMixin

class Challenge(Base, CRUDMixin):
    __tablename__ = 'challenges'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String())
    description = Column('description', String())
    accepted = Column('accepted', Boolean, default=False)
    visible = Column('visible', Boolean, default=True)
    bounty = Column('bounty', Float)
    total = Column('total', Float)
    user_id = Column('user_id', Integer, ForeignKey('users.id'))

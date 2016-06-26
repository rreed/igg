from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String, Float
from sqlalchemy.orm import relationship

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

    def __unicode__(self):
        return self.name

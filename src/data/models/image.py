from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String
from sqlalchemy.orm import relationship

from ..base import Base
from ..mixins import CRUDMixin

class Image(Base):
    __tablename__ = 'images'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    path = Column('path', String, nullable=False)
    prize_id = Column('prize_id', Integer, ForeignKey('prizes.id'), nullable=False)
    prize = relationship('Prize')

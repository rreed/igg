from sqlalchemy.schema import Column
from sqlalchemy.types import Boolean, Integer, String, Float

from ..base import Base
from ..mixins import CRUDMixin

class Game(Base, CRUDMixin):
    __tablename__ = 'games'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String())
    developer = Column('developer', String())

from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, Boolean

from ..base import Base
from ..mixins import CRUDMixin

class Game(Base, CRUDMixin):
    __tablename__ = 'games'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String())
    developer = Column('developer', String())
    site = Column('site', String())
    visible = Column('visible', Boolean, default=True)

    def __unicode__(self):
        return self.name

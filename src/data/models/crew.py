from sqlalchemy.schema import Column
from sqlalchemy.types import Float, Integer, String, Boolean, Text

from ..base import Base
from ..mixins import CRUDMixin

class Crew(Base, CRUDMixin):
    __tablename__ = 'crew'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String())
    image = Column('image', String())
    twitter = Column('twitter', String())
    steam = Column('steam', String())
    favorite = Column('favorite', String())#future TODO: FK to games?
    profile = Column('profile', Text)
    order = Column('order', Integer)
    visible = Column('visible', Boolean, default=True)

    def __unicode__(self):
        return self.name

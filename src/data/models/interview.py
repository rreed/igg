from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String
from sqlalchemy.orm import relationship

from ..base import Base
from ..mixins import CRUDMixin

class Interview(Base, CRUDMixin):
    __tablename__ = 'interviews'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String())
    description = Column('description', String())
    visible = Column('visible', Boolean, default=False)
    game_id = Column('game_id', Integer, ForeignKey('games.id'), nullable=False)
    game = relationship('Game')
    developer = Column('developer', String())

    def __unicode__(self):
        return self.name

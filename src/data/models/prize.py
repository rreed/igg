from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String, Float, DateTime

from ..base import Base
from ..mixins import CRUDMixin

class Prize(Base, CRUDMixin):
    __tablename__ = 'prizes'

    id = Column('id', Integer, primary_key=True)
    title = Column('title', String())
    description = Column('description', String())
    quantity = Column('quantity', Integer, nullable=False)
    visible = Column('visible', Boolean)
    is_auction = Column('is_auction', Boolean, default=False)
    is_giveaway = Column('is_giveaway', Boolean, default=False)
    is_code = Column('is_code', Boolean, default=True)
    entry_cost = Column('entry_cost', Float)
    game_id = Column('game_id', Integer, ForeignKey('games.id'), nullable=False)
    start = Column('start', DateTime)
    end = Column('end', DateTime)

    def __unicode__(self):
        return self.title

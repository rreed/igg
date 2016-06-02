from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String, Float

from ..base import Base
from ..mixins import CRUDMixin

class MarathonInfo(Base):
    __tablename__ = 'marathon_info'

    id = Column('id', Integer, primary_key=True)
    total = Column('total', Float)
    stage = Column('stage', Integer)
    hours = Column('hours', Integer)
    next_hour_cost = ('next_hour_cost', Float)
    current_game_id = Column('current_game_id', Integer, ForeignKey('games.id'))
    next_game_id = Column('next_game_id', Integer, ForeignKey('games.id'))
    current_schedule_entry = Column('current_schedule_entry', Integer, ForeignKey('schedule_entries.id'))

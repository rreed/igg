import datetime

from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, DateTime, Integer, String, Float

from ..base import Base
from ..mixins import CRUDMixin

class MarathonInfo(Base, CRUDMixin): # realistically almost always Update
    __tablename__ = 'marathon_info'

    id = Column('id', Integer, primary_key=True)
    total = Column('total', Float)
    start = Column('start', DateTime, nullable=False)
    hours = Column('hours', Integer)
    next_hour_cost = ('next_hour_cost', Float)
    current_game_id = Column('current_game_id', Integer, ForeignKey('games.id'), nullable=False)
    next_game_id = Column('next_game_id', Integer, ForeignKey('games.id'), nullable=False)
    current_schedule_entry = Column('current_schedule_entry', Integer, ForeignKey('schedule_entries.id'), nullable=False)

    def stage(self):
        now = datetime.datetime.now()
        end = now + datetime.timedelta(hours=self.hours)

        if now < self.start:
            return 'PRE'
        elif self.start < now and now < end:
            return 'LIVE'
        else:
            return 'POST'

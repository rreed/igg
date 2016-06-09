import datetime

from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, DateTime, Integer, String, Float

from ..base import Base
from ..mixins import CRUDMixin

class MarathonInfo(Base, CRUDMixin): # realistically almost always Update
    __tablename__ = 'marathon_info'

    id = Column('id', Integer, primary_key=True)
    total = Column('total', Float, nullable=False)
    start = Column('start', DateTime, nullable=False)
    hours = Column('hours', Integer)
    current_game_id = Column('current_game_id', Integer, ForeignKey('games.id'), nullable=False)
    next_game_id = Column('next_game_id', Integer, ForeignKey('games.id'), nullable=False)
    current_schedule_entry = Column('current_schedule_entry', Integer, ForeignKey('schedule_entries.id'), nullable=False)

    def stage(self):
        now = datetime.datetime.now()
        end = self.start + datetime.timedelta(hours=self.hours)

        if now < self.start:
            return 'PRE'
        elif self.start < now and now < end:
            return 'LIVE'
        else:
            return 'POST'

    def next_hour_cost(self):
        # TODO: replace with our real formula...
        # make up something like 20x per hour per hour to test for now
        next_hour_total = 20 * (20 * self.hours + 1)
        return next_hour_total - self.total

    def elapsed(self):
        now = datetime.datetime.now()
        elapsed = now - self.start
        seconds = elapsed.total_seconds()
        hours = seconds // 60 // 60
        minutes = (seconds  - (hours * 3600)) // 60

        if hours >= self.hours:
            return "{}:00".format(int(self.hours))
        else:
            # pad the return values to make them two digits
            return "{0:02d}:{1:02d}".format(int(hours), int(minutes))

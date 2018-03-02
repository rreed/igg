from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship

from ..base import Base
from ..mixins import CRUDMixin

class ScheduleEntry(Base, CRUDMixin):
    __tablename__ = 'schedule_entries'

    id = Column('id', Integer, primary_key=True)
    start = Column('start', DateTime)
    end = Column('end', DateTime)
    title = Column('title', String())
    description = Column('description', String())
    visible = Column('visible', Boolean)
    game_id = Column('game_id', Integer, ForeignKey('games.id'), nullable=False)
    game = relationship('Game')
    interview_id = Column('interview_id', Integer, ForeignKey('interviews.id'))
    interview = relationship('Interview')
    prize_id = Column('prize_id', Integer, ForeignKey('prizes.id'))
    prize = relationship('Prize')
    opscomment = Column('opscomment', Text)

    def __unicode__(self):
        return self.title

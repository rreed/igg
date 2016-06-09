from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String, Float, DateTime

from ..base import Base
from ..mixins import CRUDMixin

class Donation(Base, CRUDMixin):
    __tablename__ = 'donations'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String())
    url = Column('url', String())
    twitter = Column('twitter', String())
    comment = Column('description', String())
    amount = Column('amount', Float(precision=2))
    prize_interest = Column('prize_interest', Boolean, default=True)
    time = Column('time', DateTime())
    time_approved = Column('time_approved', DateTime())
    approved = Column('approved', Boolean, default=False)
    ipn_hash = Column('ipn_hash', String())
    user_id = Column('user_id', Integer, ForeignKey('users.id'))
    prize_id = Column('prize_id', Integer, ForeignKey('prizes.id'))
    challenge_id = Column('challenge_id', Integer, ForeignKey('challenges.id'))
    game_id = Column('game_id', Integer, ForeignKey('game.id'))

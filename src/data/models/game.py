from sqlalchemy.schema import Column
from sqlalchemy.types import Float, Integer, String, Boolean, Text

from ..base import Base
from ..mixins import CRUDMixin

class Game(Base, CRUDMixin):
    __tablename__ = 'games'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String())
    developer = Column('developer', String())
    site = Column('site', String())
    visible = Column('visible', Boolean, default=True)
    buzz =  Column('buzz', Float(precision=2), default=0.00)
    normalized_buzz =  Column('normalized_buzz', Float(precision=2), default=0.00)
    plays = Column('plays', Integer, default = 0)
    description = Column('description', Text)

    def __unicode__(self):
        return self.name

    ##I'm going to make bee noises now
    
    def add_buzz(self, donation_amount):
        self.buzz += donation_amount
        self.update_buzz()

    def update_buzz(self):
        self.normalized_buzz = self.buzz/(self.plays+1)**2 * 10
        self.save()

    @classmethod
    def update_relative_buzz(cls, db):
        games = db.session.query(cls).filter((cls.normalized_buzz > 0)|(cls.buzz > 0))
        maxbuzz = 0
        for game in games:
            game.update_buzz()
            if game.normalized_buzz > maxbuzz:
                maxbuzz = game.normalized_buzz
        if maxbuzz == 0:
            maxbuzz = 1
        for game in games:
            game.normalized_buzz = game.normalized_buzz * 100 // maxbuzz
            game.save()

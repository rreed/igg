# title = models.CharField(max_length=200)
#     description = models.TextField(max_length=500, null=True, blank=True)
#     opscomment = models.TextField(max_length=500, null=True, blank=True)
#     visible = models.BooleanField(default=False)
#     games = models.ManyToManyField(Game, related_name='interviews', null=True, blank=True)
#     images = models.ManyToManyField(ImageUpload, related_name='interviews', null=True, blank=True)

from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String

from ..base import Base
from ..mixins import CRUDMixin

class Interview(Base, CRUDMixin):
    __tablename__ = 'interviews'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String())
    description = Column('name', String())
    visible = Column('visible', Boolean, default=False)
    game_id = Column('game_id', Integer, ForiegnKey('game.id'), nullable=False)
    developer = Column('developer', String())

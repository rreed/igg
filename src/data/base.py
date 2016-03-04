from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import MetaData

class BaseModel(object):
    """
    The base class for all of our database models.
    """

    @classmethod
    def columns(cls):
        return cls.__table__.columns

def named_declarative_base(**kwargs):
    """
    cf. http://docs.sqlalchemy.org/en/rel_0_9/core/constraints.html#constraint-naming-conventions
    """
    convention = {
        "ix": 'ix_%(column_0_label)s', # index
        "uq": "uq_%(table_name)s_%(column_0_name)s", # unique
        "ck": "ck_%(table_name)s_%(constraint_name)s", # constraint
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s", # foreign key
        "pk": "pk_%(table_name)s" # primary key
    }
    metadata = MetaData(naming_convention=convention)

    return declarative_base(metadata=metadata, **kwargs)

Base = named_declarative_base(cls=BaseModel)

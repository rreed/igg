from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from .base import Base
from ..settings import app_config

class DatabaseConnection(object):
    def __init__(self, url, **factory_args):
        self.engine = create_engine(url)
        self.session_factory = sessionmaker(bind=self.engine, **factory_args)
        self.session = scoped_session(self.session_factory)

    # Alembic configuration uses db.metadata to detect schema changes
    @property
    def metadata(self):
        return Base.metadata

    @contextmanager
    def transient_session(self, **session_args):
        """
        Create a short-lived SQLAlchemy session for cases like database prepopulation.
        """
        session = self.session_factory(**session_args)
        try:
            yield session
        except:
            session.rollback()
            raise
        finally:
            session.close()

db = DatabaseConnection(app_config.SQLALCHEMY_DATABASE_URI)

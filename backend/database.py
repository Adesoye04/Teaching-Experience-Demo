import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker, declarative_base, DeclarativeBase
from sqlalchemy import event
DATABASE_URL = "sqlite:///teaching_experience.db"
engine = sa.create_engine(
    DATABASE_URL,
    echo=True,
    connect_args={"check_same_thread": False},
)
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@event.listens_for(engine, "connect")
def _set_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

class Base(DeclarativeBase):
    pass

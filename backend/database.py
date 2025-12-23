import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker, declarative_base, DeclarativeBase

DATABASE_URL = "sqlite:///teaching_experience.db"
engine = sa.create_engine(
    DATABASE_URL,
    echo=True,
    connect_args={"check_same_thread": False},
)
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

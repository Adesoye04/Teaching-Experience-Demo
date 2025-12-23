import datetime

from pydantic import EmailStr
from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .database import Base

class Teacher(Base):
    __tablename__ = 'teachers'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[EmailStr] = mapped_column(String, nullable=True)
    password_hash: Mapped[str] = mapped_column(String, nullable=True)

class Philosophy_Question(Base):
    __tablename__ = 'philosophy_questions'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    text: Mapped[str] = mapped_column(String, nullable=False)
    order: Mapped[int] = mapped_column(Integer, nullable=False)

class Philosophy_Option(Base):
    __tablename__ = 'philosophy_options'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    question_id: Mapped[int] = mapped_column(Integer, nullable=False)
    label: Mapped[str] = mapped_column(String, nullable=True)
    text: Mapped[str] = mapped_column(String, nullable=True)

class Philosophy_Response(Base):
    __tablename__ = 'philosophy_responses'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    teacher_id: Mapped[int] = mapped_column(Integer, nullable=False)
    option_id: Mapped[int] = mapped_column(Integer, nullable=False)
    question_id: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False)

class Philosophy_Profile(Base):
    __tablename__ = 'philosophy_profiles'
    teacher_id: Mapped[int] = mapped_column(Integer, primary_key= True, nullable=False)
    tags_ranked: Mapped[int] = mapped_column(Integer, nullable=False)
    priority_scores: Mapped[int] = mapped_column(Integer, nullable=False)
    summary: Mapped[str] = mapped_column(String, nullable=True)
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=True)
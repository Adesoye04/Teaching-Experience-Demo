import datetime

from pydantic import EmailStr
from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .database import Base

class Teacher(Base):
    __tablename__ = 'teachers'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str|None] = mapped_column(String, nullable=True)
    password_hash: Mapped[str|None] = mapped_column(String, nullable=True)
    responses: Mapped[list["Philosophy_Response"]] = relationship(
        back_populates="teacher")

class Philosophy_Question(Base):
    __tablename__ = 'philosophy_questions'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False,)
    text: Mapped[str] = mapped_column(String, nullable=False)
    order: Mapped[int] = mapped_column(Integer, nullable=False)
    responses: Mapped[list["Philosophy_Response"]] = relationship(
        back_populates="question")
    options: Mapped[list["Philosophy_Option"]] = relationship(back_populates="question", cascade="all, delete-orphan")

class Philosophy_Option(Base):
    __tablename__ = 'philosophy_options'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    question_id: Mapped[int] = mapped_column(Integer, ForeignKey ("philosophy_questions.id", ondelete = "CASCADE"), nullable=False)
    label: Mapped[str|None] = mapped_column(String, nullable=True)
    text: Mapped[str|None] = mapped_column(String, nullable=True)
    question: Mapped[Philosophy_Question] = relationship(back_populates="options")
    responses: Mapped[list["Philosophy_Response"]] = relationship(back_populates="option")
    primary_tag: Mapped[str|None] = mapped_column(String, nullable=True)
    secondary_tag: Mapped[str|None] = mapped_column(String, nullable=True)

class Philosophy_Response(Base):
    __tablename__ = 'philosophy_responses'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    teacher_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("teachers.id", ondelete="CASCADE"),
        nullable=False
    )
    teacher: Mapped["Teacher"] = relationship(back_populates="responses")
    question: Mapped["Philosophy_Question"] = relationship(back_populates="responses")
    option_id: Mapped[int] = mapped_column(Integer, ForeignKey("philosophy_options.id", ondelete = "CASCADE"),  nullable=False)
    question_id: Mapped[int] = mapped_column(Integer, ForeignKey ("philosophy_questions.id", ondelete = "CASCADE"), nullable=False)
    option: Mapped["Philosophy_Option"] = relationship(back_populates="responses")
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False)

class Philosophy_Profile(Base):
    __tablename__ = 'philosophy_profiles'
    teacher_id: Mapped[int] = mapped_column(Integer, ForeignKey("teachers.id"), primary_key= True, nullable=False)
    tags_ranked: Mapped[int] = mapped_column(Integer, nullable=False)
    priority_scores: Mapped[int] = mapped_column(Integer, nullable=False)
    summary: Mapped[str|None] = mapped_column(String, nullable=True)
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=True)
from datetime import datetime

from pydantic import BaseModel, EmailStr


class TeacherCreate(BaseModel):
    name:str
    email: EmailStr | None = None
    password_hash:str | None = None

class TeacherUpdate(BaseModel):
    name:str
    email:EmailStr | None = None
    password_hash:str | None = None

class TeacherOut(BaseModel):
    id: int
    name: str
    email: EmailStr | None
    class Config:
        orm_mode = True
# Philosophy
class PhilosophyQuestionOut(BaseModel):
    id: int
    text: str
    order: int
    class Config:
        orm_mode = True

class PhilosophyOptionOut(BaseModel):
    id: int
    question_id: int
    label: int
    text: str
    class Config:
        orm_mode = True

class PhilosophyResponseCreate(BaseModel):
    teacher_id: int
    option_id: int
    question_id: int

class PhilosophyResponseOut(BaseModel):
    id: int
    teacher_id: int
    option_id: int
    question_id: int
    created_at: datetime | None

    class Config:
        orm_mode = True

class PhilosophyProfileOut(BaseModel):
    teacher_id: int
    tags_ranked:list[str]
    priority_scores:dict[str, int]
    summary:str
    updated_at: datetime

    class Config:
        orm_mode = True

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session


from .. import models, schemas
from ..deps import get_db
router = APIRouter(prefix = "/teachers", tags=["teachers"])
@router.post("/", response_model=schemas.TeacherOut, status_code=status.HTTP_201_CREATED)
def create_teacher(payload: schemas.TeacherCreate,db: Session = Depends(get_db)):
    teacher = models.Teacher(name = payload.name, email = payload.email, password_hash= payload.password_hash)
    db.add(teacher)
    db.commit()
    db.refresh(teacher)
    return teacher
@router.get("/", response_model=list[schemas.TeacherOut])
def list_teachers(db: Session = Depends(get_db)):
    return db.query(models.Teacher).order_by(models.Teacher.id.asc()).all()

@router.get("/{teacher_id}", response_model=schemas.TeacherOut)
def get_teacher( teacher_id:int, db: Session = Depends(get_db)):
    teacher = db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Teacher not found")
    return teacher

@router.patch("/{teacher_id}", response_model=schemas.TeacherOut)
def update_teacher(teacher_id: int, payload:schemas.TeacherUpdate, db: Session = Depends(get_db)):
    teacher = db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Teacher not found")
    if payload.name is not None:
        teacher.name = payload.name
    if payload.email is not None:
        teacher.email = payload.email
    if payload.password_hash is not None:
        teacher.password_hash = payload.password_hash

    db.commit()
    db.refresh(teacher)
    return teacher
@router.delete("/{teacher_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_teacher(teacher_id: int, db: Session = Depends(get_db)):
    teacher = db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Teacher not found")
    db.delete(teacher)
    db.commit()
    return None

@router.get("/{teacher_id}/philosophy/responses", response_model=list[schemas.PhilosophyResponseOut])
def get_teacher_responses(teacher_id: int, db: Session = Depends(get_db)):
    q = db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()
    if not q:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Teacher not found")
    return q.responses
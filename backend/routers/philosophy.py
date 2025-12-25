from datetime import datetime, timezone

from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session, selectinload

from .. import models, schemas
from ..deps import get_db
router = APIRouter(prefix = "/philosophy", tags = ["philosophy"])

@router.get("/questions", response_model=list[schemas.PhilosophyQuestionOut])
def list_philosophy(db: Session = Depends(get_db)):
    return db.query(models.Philosophy_Question).order_by(models.Philosophy_Question.order.asc()).all()

@router.get("/questions/{question_id}/options", response_model=list[schemas.PhilosophyOptionOut])
def list_philosophy_options(question_id: int, db: Session = Depends(get_db)):
    q = db.query(models.Philosophy_Question).filter(models.Philosophy_Question.id == question_id).first()
    if not q:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question not found")
    return db.query(models.Philosophy_Option).filter(models.Philosophy_Option.question_id == question_id).all()

@router.get("/questions-with-options", response_model=list[schemas.PhilosophyQuestionWithOptionsOut])
def questions_with_options(db: Session = Depends(get_db)):
    return (db.query(models.Philosophy_Question).options(selectinload( models.Philosophy_Question.options ))
            .order_by (models.Philosophy_Question.order.asc()).all())

@router.post("/responses", response_model=schemas.PhilosophyResponseOut)
def submit_philosophy_response(payload: schemas.PhilosophyResponseCreate, db: Session = Depends(get_db)):
    q = db.query(models.Teacher).filter(models.Teacher.id == payload.teacher_id).first()
    if not q:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Teacher not found")
    question = db.query(models.Philosophy_Question).filter(models.Philosophy_Question.id == payload.question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    w = db.query(models.Philosophy_Option).filter(models.Philosophy_Option.question_id == payload.question_id,
                                                  models.Philosophy_Option.id == payload.option_id).first()
    if not w:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Option not found")
    response = models.Philosophy_Response(teacher_id=payload.teacher_id, question_id=payload.question_id, option_id = payload.option_id, created_at=datetime.now(timezone.utc),)
    db.add(response)
    db.commit()
    db.refresh(response)
    return response

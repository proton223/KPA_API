from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST API
@app.post("/kpa", response_model=schemas.KPAFormResponse)
def create_form(data: schemas.KPAFormCreate, db: Session = Depends(get_db)):
    form = models.KPAForm(**data.dict())
    db.add(form)
    db.commit()
    db.refresh(form)
    return form

# GET API
@app.get("/kpa/{id}", response_model=schemas.KPAFormResponse)
def get_form(id: int, db: Session = Depends(get_db)):
    form = db.query(models.KPAForm).filter(models.KPAForm.id == id).first()
    if not form:
        raise HTTPException(status_code=404, detail="Form not found")
    return form

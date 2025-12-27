from sqlalchemy.orm import Session
from . import models, schemas
from .auth import hash_password

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip=0, limit=10):
    return db.query(models.User).offset(skip).limit(limit).all()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

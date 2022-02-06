from sqlalchemy.orm import Session

from . import models, schemas

def get_asteroids(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(models.Asteroid).offset(skip).limit(limit).all()
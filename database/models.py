from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class Asteroid(Base):
    __tablename__ = "transients_app_asteroid"

    id = Column(Integer, primary_key=True, index=True)
    designation = Column(String)
    absolute_magnitude = Column(Float)
    visual_magnitude = Column(Float)
    timestamp = Column(DateTime)
    ra = Column(Float)
    dec = Column(Float)

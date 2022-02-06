from datetime import datetime

from pydantic import BaseModel

class Asteroid(BaseModel):
    designation: str
    absolute_magnitude : float

    timestamp : datetime
    visual_magnitude: float
    ra: float
    dec: float

    class Config:
        orm_mode = True
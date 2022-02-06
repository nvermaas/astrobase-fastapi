from fastapi import APIRouter, Query
from enum import Enum
from datetime import datetime

router = APIRouter(tags=["minor planets"],)

class MinorPlanetType(str, Enum):
    asteroid = "asteroid"
    comet = "comet"

# http://127.0.0.1:8000/minorplanets/comet
@router.get("/minorplanets/{type}", tags=["minor planets"])
async def get_minor_planet(type: MinorPlanetType):
    if type == MinorPlanetType.asteroid:
        return {"type": type, "asteroid": "calculate asteroids"}
    return {"type": type, "comet": "don't look up!"}


# http://127.0.0.1:8000/asteroid/
# http://127.0.0.1:8000/asteroid/?name=vesta
@router.get("/asteroid/", tags=["minor planets"])
async def get_asteroid(name: str = 'Ceres' ):
    return {"asteroid": name}


# example of parameter metadata
# http://127.0.0.1:8000/comet/
# http://127.0.0.1:8000/comet/?comet-name=atlas
@router.get("/comet/", tags=["minor planets"])
async def get_comet(name: str = Query(
    'Neowise',
    alias="comet-name",
    title="comet name",
    description="Enter the name of the comet",
    max_length=30),
    datetime: datetime = datetime.utcnow()):
    return {"comet": name, "datetime" : datetime}

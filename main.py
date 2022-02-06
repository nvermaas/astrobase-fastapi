import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import crud, models, schemas
from database.database import SessionLocal, engine

from routers import minor_planets, cutouts

app = FastAPI(
    title="AstroBase FastAPI",
    description="AstroBase FastAPI",
    version="0.0.1",
    contact={
        "name": "Nico Vermaas",
        "url": "https://uilennest.net",
        "email": "nvermaas@xs4all.nl",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },)

app.include_router(minor_planets.router)
app.include_router(cutouts.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
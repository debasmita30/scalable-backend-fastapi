from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from .database import Base, engine, SessionLocal
from .routers import users, tasks
from . import crud, schemas

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Scalable Backend Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(tasks.router)

app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")


@app.get("/")
def serve_frontend():
    return FileResponse("frontend/index.html")


@app.on_event("startup")
def create_demo_user():
    db = SessionLocal()
    try:
        if not crud.get_user_by_email(db, "deb@example.com"):
            crud.create_user(
                db,
                schemas.UserCreate(
                    name="Debasmita",
                    email="deb@example.com",
                    password="test123"
                )
            )
    finally:
        db.close()

from fastapi import FastAPI
from .database import Base,engine
from . import models
from .routers import books

#create db tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Book CRUD SERVICE")

app.include_router(books.router)

@app.get("/")
def root():
    return {"message":"Welcome to Book crud service"}

import os

from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Field Service Management API",
    description="Backend API for the Field Service Management Core",
    version="0.1.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=False,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
    allow_headers=["*"],
)


engine = create_engine(
    os.environ["DATABASE_URL"],
    pool_pre_ping=True,
)


@app.get("/")
def root():
    return {"message": "Field Service Management API is running"}


@app.get("/health")
def health():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {"status": "ok", "database": "connected"}

    except SQLAlchemyError:
        raise HTTPException(
            status_code=503,
            detail="Database connection unavailable",
        )

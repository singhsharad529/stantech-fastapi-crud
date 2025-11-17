from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Detect if running in Docker or locally
if os.path.exists("/.dockerenv"):
    # Running in Docker
    DATA_DIR = "/app/data"
    DB_PATH = os.path.join(DATA_DIR, "books.db")
else:
    # Running locally
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_PATH = os.path.join(BASE_DIR, "../.books.db")
    DATA_DIR = os.path.dirname(DB_PATH)

# Ensure the data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False}
)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


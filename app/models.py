from sqlalchemy import Column,Integer,String,DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import pytz
from .database import Base


# Define IST timezone
IST = pytz.timezone("Asia/Kolkata")

def get_ist_time():
    """Return current datetime in IST."""
    return datetime.now(IST)

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String,unique=True,nullable=False,index=True)
    description = Column(String,nullable=True)
    created_at = Column(DateTime,default=get_ist_time)
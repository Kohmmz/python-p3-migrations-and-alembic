from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# Create an engine connected to the SQLite database
engine = create_engine('sqlite:///migrations_test.db')

# Base class for SQLAlchemy models
Base = declarative_base()

# Define a sample model (Student)
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=True)
    email = Column(String, unique=True)
    grade = Column(Integer)
    birthday = Column(DateTime)
    enrolled_date = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f"Student {self.id}: {self.name}, Grade {self.grade}"

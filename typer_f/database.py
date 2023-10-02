from contextlib import contextmanager
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, UniqueConstraint, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy.ext.declarative import declarative_base


username = "postgres"
password = "FabioFazio2023"
database = "typer"
port = 5432
host = "localhost"

# Define your SQLAlchemy models
# Base = declarative_base()

# ... Define your User model and other necessary models ...

# Connect to the database
#  # # # # #DATABASE_URL = "postgresql://user:password@localhost:5432/dbname"
SQLALCHEMY_DATABASE_URL = f"postgresql://{username}:{password}@{host}:{port}/{database}"
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# # Initialize the user database
# user_db = SQLAlchemyUserDatabase(User, database, Base)



engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
 
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

class Word(Base):
    __tablename__ = 'words'
    id = Column(Integer, primary_key=True, autoincrement=True)
    word = Column(String(64), nullable=False)
    language = Column(String(32), nullable=False)
    meaning = Column(String(256))
    example = Column(String(256))
    frequency = Column(Integer, nullable=False, default=0)  # Add frequency column
    uq_word_language = UniqueConstraint(word, language) # Add unique constraint

class Lesson(Base):
    __tablename__ = 'lessons'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    description = Column(String(500), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

class Exercise(Base):
    __tablename__ = 'exercises'

    id = Column(Integer, primary_key=True)
    lesson_id = Column(Integer, ForeignKey('lessons.id'), nullable=False)
    text = Column(String(1000), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    lesson = relationship('Lesson', backref='exercises')

class Result(Base):
    __tablename__ = 'results'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    exercise_id = Column(Integer, ForeignKey('exercises.id'), nullable=False)
    duration = Column(Integer, nullable=False)
    accuracy = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False)

    user = relationship('User', backref='results')
    exercise = relationship('Exercise', backref='results')
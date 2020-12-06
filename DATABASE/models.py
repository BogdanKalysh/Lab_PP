from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("postgresql://postgres:29.03.2002@localhost/students_rating", echo = True)

Session = sessionmaker(bind=engine)

Base = declarative_base()

class student(Base):
    __tablename__ = "student"

    student_id = Column('student_id',Integer,primary_key=True)
    name = Column('name',String)
    marks = Column('marks',ARRAY(Integer))

class teacher(Base):
    __tablename__ = 'teacher'

    teacher_id = Column('teacher_id',Integer,primary_key=True)
    name = Column('name',String)
    email = Column('email',String)
    password = Column('password',String)

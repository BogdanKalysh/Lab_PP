from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from werkzeug.security import generate_password_hash

engine = create_engine("postgresql://postgres:147896325@localhost/reiting", echo = True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class student(Base):
    __tablename__ = "student"

    student_id = Column('student_id',Integer,primary_key=True)
    name = Column('name',String)
    s_bal = Column('s_bal',Integer)
    marks = Column('marks',ARRAY(Integer))

class teacher(Base):
    __tablename__ = 'teacher'

    teacher_id = Column('teacher_id',Integer,primary_key=True)
    name = Column('name',String)
    email = Column('email',String)
    password = Column('password',String)


    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table users
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    address = Column(String(250), nullable=False)
    phone_numbers = relationship("Phone_numbers", back_populates="user")

class Phone_numbers(Base):
    __tablename__ = 'phone_numbers'
    # Here we define columns for the table cars.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    phone_number = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(Users, back_populates="phone_numbers")


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///sqlalchemy_phone_book.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
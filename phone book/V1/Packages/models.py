import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Users(Base):
    # класс пользователей (id, name, address)
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    address = Column(String(250), nullable=False)
    phone_numbers = relationship("Phone_numbers", back_populates="user")

    def __str__(self):
        return self.name

class Phone_numbers(Base):
    # класс телефонов (id, phone_number)
    __tablename__ = 'phone_numbers'
    id = Column(Integer, primary_key=True)
    phone_number = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(Users, back_populates="phone_numbers")

    def __str__(self):
        return self.phone_number

engine = create_engine('sqlite:///sqlalchemy_phone_book.db')
Base.metadata.create_all(engine)
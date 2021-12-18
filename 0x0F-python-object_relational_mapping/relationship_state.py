#!/usr/bin/python3
""" Create file that contains the class definition of State
    and a instance of Base = declaratibe_base() with relationship
"""
from enum import unique
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base


class State (Base):
    """ Model State define a State object with relationship
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete', backref='state')

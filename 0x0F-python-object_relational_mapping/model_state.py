#!/usr/bin/python3
""" Create file that contains the class definition of State
    and a instance of Base = declaratibe_base()
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()


class State (Base):
    """ Model State define a State object
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

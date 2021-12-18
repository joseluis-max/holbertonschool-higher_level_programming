#!/usr/bin/python3
""" script that changes the name of a State object from the database hbtn_0e_6_usa
    with sqlalchemy
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    session = Session(engine)
    state = session.query(State).filter(State.id == 2).one()
    state.name = 'New Mexico'
    session.add(state)
    session.commit()
    session.close()

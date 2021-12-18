#!/usr/bin/python3
""" script that deletes all State objects with a name containing the letter
    a from the database hbtn_0e_6_usa
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
    result = session.query(State).filter(State.name.like('%a%')).all()
    for r in result:
        session.delete(r)
    session.commit()
    session.close()

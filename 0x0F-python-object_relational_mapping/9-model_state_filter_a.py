#!/usr/bin/python3
""" script that lists all State objects that contain
    the letter a from the database hbtn_0e_6_usa
    with alchemy
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
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()
    for s in states:
        print('{}: {}'.format(s.id, s.name))
    session.close()

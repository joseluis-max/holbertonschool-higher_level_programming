#!/usr/bin/python3
""" script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
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
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    states = session.query(State).filter(State.name == 'Louisiana').all()
    for s in states:
        print('{}'.format(s.id))
    session.close()

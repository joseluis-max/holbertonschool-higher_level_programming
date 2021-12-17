#!/usr/bin/python3
""" script that lists all State objects, and corresponding
    City objects, contained in the database hbtn_0e_101_usa
"""
import sys
from relationship_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'
                        .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    session = Session(engine)
    states = session.query(State).all()
    for s in states:
        print('{}: {}'.format(s.id, s.name))
        for c in s.cities:
            print('    {}: {}'.format(c.id, c.name))
    session.close()

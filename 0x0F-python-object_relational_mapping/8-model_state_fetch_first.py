#!/usr/bin/python3
""" script that prints the first State object from the database hbtn_0e_6_usa
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
    query = session.query(State).order_by(State.id).first()
    if (query is None):
        print('Nothing')
    else:
        print('{}: {}'.format(query.id, query.name))
    session.close()

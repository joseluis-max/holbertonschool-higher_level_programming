#!/usr/bin/python3
""" script that prints the State object with the name passed as
    argument from the database hbtn_0e_6_usa
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
    states = session.query(State).filter(State.name == sys.argv[4]).order_by(State.id).all()
    if len(states) == 0:
        print("Not found")
    else:
        for s in states:
            print('{}'.format(s.id))
    session.close()

#!/usr/bin/python3
""" script 14-model_city_fetch_by_state.py that prints all City
    objects from the database hbtn_0e_14_usa
    with alchemy
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'
                        .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    session = Session(engine)
    cities = session.query(State.name, City.id, City.name).join(City,
    City.state_id == State.id).order_by(City.id).all()
    for c in cities:
        print('{}: ({}) {}'.format(c[0], c[1], c[2]))
    session.close()

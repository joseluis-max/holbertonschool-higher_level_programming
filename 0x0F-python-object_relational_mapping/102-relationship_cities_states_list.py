#!/usr/bin/python3
""" script that lists all State objects, and corresponding
    City objects, contained in the database hbtn_0e_101_usa
"""
import sys
from relationship_state import Base
from relationship_city import City
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'
                        .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    session = Session(engine)
    cities = session.query(City).join(City.state).order_by(City.id).all()
    for c in cities:
        print('{}: {} -> '.format(c.id, c.name), end="")
        print('{}'.format(c.state.name))
    session.close()

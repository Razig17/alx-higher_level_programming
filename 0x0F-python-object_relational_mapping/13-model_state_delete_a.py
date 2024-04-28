#!/usr/bin/python3

"""
script that deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from model_state import Base, State


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    session = Session()

    states_to_delete = states = session.query(State).order_by(State.id).filter(
        State.name.like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)
    session.commit()

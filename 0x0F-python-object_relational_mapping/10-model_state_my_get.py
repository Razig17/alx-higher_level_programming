#!/usr/bin/python3
"""A script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa"""
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

    state = session.query(State).order_by(State.id).filter(
        State.name.like(sys.argv[4])).first()
    if state:
        print(state.id)
    else:
        print('Not found')

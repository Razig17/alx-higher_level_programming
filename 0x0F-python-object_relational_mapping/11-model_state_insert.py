#!/usr/bin/python3
"""A script that adds the State object “Louisiana” to database hbtn_0e_6_usa"""
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

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit
    state = session.query(State).filter(State.name == 'Louisiana').first()
    print(state.id)

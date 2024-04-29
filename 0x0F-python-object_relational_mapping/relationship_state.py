#!/usr/bin/python3
"""
This module contains the class definition of a State
"""
from sqlalchemy import Column, Integer, String
from relationship_city import City, Base
from sqlalchemy.orm import relationship


class State(Base):
    """Class state that defines states taple """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref="state", cascade="all, delete")

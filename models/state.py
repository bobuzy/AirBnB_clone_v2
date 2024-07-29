#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    storage_type = getenv("HBNB_TYPE_STORAGE")

    if storage_type == 'db':
        cities = relationship("City", backref="state", cascade="delete")
    else:
        @property
        def cities(self):
            """Return list of cities linked to a state"""
            from models import storage
            from models.city import City
            city_list = []
            all_cities = storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list

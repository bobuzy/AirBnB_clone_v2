#!/usr/bin/python3
"""This module defines a class Place"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Place(BaseModel, Base):
    """Place class definition"""

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    user = relationship("User", backref="places")

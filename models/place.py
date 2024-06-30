#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), primary_key=True,
                             ForeignKey('places.id'), nullable=False)
                      Column('amenity_id', String(60), primary_key=True,
                             ForeignKey('amenities.id'), nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenities = relationship("Amenity", secondary=place_amenity,
                             viewonly=False)

    amenities = relationship("Amenity", secondary=place_amenity,
                             back_populates="place_amenities")

    @property
    def amenities(self):
        """Getter for amenities."""
        return self._amenities

    @amenities.setter
    def amenities(self, obj):
        """Setter for amenities."""
        if isinstance(obj, Amenity):
            self._amenities.append(obj)

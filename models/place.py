#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, ForeignKey, Integer, Float, Column
from sqlalchemy.orm import relationship


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
    amenity_ids = []

    reviews = relationship(
                    'Review', backref='place', cascade='all, delete-orphan')

    @property
    def reviews(delf):
        """ getter attribute that retrun the list of review"""
        from models import storage
        from models.review import Review
        list_rev = []
        for rev in storage.all(Review).values():
            if Review.place_id == self.id:
                list_rew.append(rev)
        return list_rev

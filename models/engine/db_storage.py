#!/usr/bin/python3
"""Module definition for DBStorage"""

import models
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {
    "Amenity": Amenity,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}


class DBStorage:
    """DBStrorage class definition"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializze DBStorage object"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Return a dictionary of all/selected class objects"""
        if cls is None:
            objs = []
            for cls_name in classes.values():
                objs.extend(self.__session.query(cls_name).all())
        else:
            if type(cls) == str:
                cls = classes.get(cls, None)
            if cls is None:
                return {}
            objs = self.__session.query(cls).all()
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}

    def new(self, obj):
        """Add new object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a new session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def get(self, cls, id):
        """
        Retrieves one object based on the class name and its ID.
        """
        if cls not in classes:
            return None
        return self.__session.query(classes[cls]).filter_by(id=id).first()

    def close(self):
        """Close the working SQLAlchemy session"""
        self.__session.remove()

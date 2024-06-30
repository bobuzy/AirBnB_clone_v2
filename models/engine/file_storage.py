#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return self.__objects
        list_obj = {}
        for key, obj in self.__objects.items():
            if isinstance(obj, cls):
                list_obj[key] = obj
        return list_obj

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r', encoding='utf-8') as f:
                    temp = json.load(f)
                    for key, val in temp.items():
                        class_name = val['__class__']
                        cls = globals()[class_name]
                        self.__objects[key] = cls(**val)
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error loading JSON file: {e}")
                self.__objects = {}
        else:
            self.__objects = {}

    def delete(self, obj=None):
        """ Deletes obj from __objects if it’s inside.
        If obj is equal to None, the method does nothin"""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]

#!/usr/bin/python3
"""Defines the FileStorage class."""

import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """Represent an abstracted storage engine."""


__file_path = "file.json"
__objects = {}


def all(self, cls=None):
    """Return a dictionary of instantiated objects in __objects."""
    if cls is not None:
        cls_dict = {}
        for k, v in self.__objects.items():
            if isinstance(v, cls):
                cls_dict[k] = v
        return cls_dict
    return self.__objects


def new(self, obj):
    """Set obj in __objects with key <obj_class_name>.id."""
    self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj


def save(self):
    """Serialize __objects to the JSON file __file_path."""
    odict = {o: self.__objects[o].to_dict() for o in self.__objects}
    with open(self.__file_path, "w", encoding="utf-8") as f:
        json.dump(odict, f)


def reload(self):
    """Deserialize the JSON file __file_path to __objects, if it exists."""
    try:
        with open(self.__file_path, "r", encoding="utf-8") as f:
            objects_data = json.load(f)
            for o in objects_data.values():
                class_name = o["__class__"]
                del o["__class__"]
                obj = eval(class_name)(**o)
                self.new(obj)
    except FileNotFoundError:
        pass


def delete(self, obj=None):
    """Delete a given object from __objects, if it exists."""
    if obj:
        keyVal = "{}.{}".format(type(obj).__name__, obj.id)
        del self.__objects[keyVal]

def close(self):
    """Call the reload method."""
    self.reload()

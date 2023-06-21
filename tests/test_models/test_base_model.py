#!/usr/bin/python3
"""
Module for testing the BaseModel class
"""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """
    Class to test the BaseModel class
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the test class
        """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """
        Set up the test environment
        """
        pass

    def tearDown(self):
        """
        Clean up after the test
        """
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_default(self):
        """
        Test the default behavior of BaseModel instantiation
        """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """
        Test BaseModel instantiation with keyword arguments
        """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """
        Test BaseModel instantiation with non-string key in kwargs
        """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """
        Test the save method of BaseModel
        """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """
        Test the __str__ method of BaseModel
        """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(
            self.name, i.id, i.__dict__))

    def test_todict(self):
        """
        Test the to_dict method of BaseModel
        """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """
        Test BaseModel instantiation with None as key in kwargs
        """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """
        Test BaseModel instantiation with a single keyword argument
        """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """
        Test the id attribute of BaseModel
        """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """
        Test the created_at attribute of BaseModel
        """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """
        Test the updated_at attribute of BaseModel
        """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)


if __name__ == "__main__":
    unittest.main()

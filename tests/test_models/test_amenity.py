#!/usr/bin/python3
"""
Module to test the Amenity model
"""

import unittest
import os
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import pep8


class test_Amenity(test_basemodel):
    """
    Class to test the Amenity model
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the test class
        """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """
        Test the name attribute of Amenity class
        """
        new = self.value()
        self.assertEqual(type(new.name), str)

    @classmethod
    def setUpClass(cls):
        """Set up for the test"""
        cls.amenity = Amenity()
        cls.amenity.name = "Breakfast"

    @classmethod
    def teardown(cls):
        """Tear down at the end of the test"""
        del cls.amenity

    def tearDown(self):
        """Tear down method"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Amenity(self):
        """Test for pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "Fix pep8")

    def test_checking_for_docstring_Amenity(self):
        """Check for docstrings"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes_Amenity(self):
        """Check if Amenity has attributes"""
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def test_is_subclass_Amenity(self):
        """Test if Amenity is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_attribute_types_Amenity(self):
        """Test attribute types for Amenity"""
        self.assertEqual(type(self.amenity.name), str)

    def test_save_Amenity(self):
        """Test if the save method works"""
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)

    def test_to_dict_Amenity(self):
        """Test if the to_dict method works"""
        self.assertEqual('to_dict' in dir(self.amenity), True)


if __name__ == "__main__":
    unittest.main()

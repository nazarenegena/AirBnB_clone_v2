#!/usr/bin/python3
"""
Module for testing the State class
"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import unittest
import os
from models.base_model import BaseModel
import pep8


class test_state(test_basemodel):
    """
    Class to test the State class
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the test class
        """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """
        Test the name attribute of State
        """
        new = self.value()
        self.assertEqual(type(new.name), str)


class TestState(unittest.TestCase):
    """This will test the State class"""

    @classmethod
    def setUpClass(cls):
        """Set up for test"""
        cls.state = State()
        cls.state.name = "CA"

    @classmethod
    def tearDownClass(cls):
        """At the end of the test, this will tear it down"""
        del cls.state

    def tearDown(self):
        """Tear down"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_State(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/state.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_State(self):
        """Checking for docstrings"""
        self.assertIsNotNone(State.__doc__)

    def test_attributes_State(self):
        """Checking if State has attributes"""
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)

    def test_is_subclass_State(self):
        """Test if State is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_attribute_types_State(self):
        """Test attribute types for State"""
        self.assertEqual(type(self.state.name), str)

    def test_save_State(self):
        """Test if the save method works"""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict_State(self):
        """Test if the to_dict method works"""
        self.assertEqual('to_dict' in dir(self.state), True)


if __name__ == "__main__":
    unittest.main()

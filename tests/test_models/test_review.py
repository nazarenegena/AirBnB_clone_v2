#!/usr/bin/python3
"""
Module for testing the Review class
"""
import unittest
import pep8
import os
from os import getenv
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Class to test the Review class"""

    @classmethod
    def setUpClass(cls):
        """Set up for test"""
        cls.rev = Review()
        cls.rev.place_id = "4321-dcba"
        cls.rev.user_id = "123-bca"
        cls.rev.text = "The strongest in the Galaxy"

    @classmethod
    def tearDownClass(cls):
        """Tear down after the test"""
        del cls.rev

    def tearDown(self):
        """Tear down"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_Review(self):
        """Test pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/review.py'])
        self.assertEqual(p.total_errors, 0, "Fix pep8")

    def test_checking_for_docstring_Review(self):
        """Test checking for docstrings"""
        self.assertIsNotNone(Review.__doc__)

    def test_attributes_review(self):
        """Test if Review has attributes"""
        self.assertTrue('id' in self.rev.__dict__)
        self.assertTrue('created_at' in self.rev.__dict__)
        self.assertTrue('updated_at' in self.rev.__dict__)
        self.assertTrue('place_id' in self.rev.__dict__)
        self.assertTrue('text' in self.rev.__dict__)
        self.assertTrue('user_id' in self.rev.__dict__)

    def test_is_subclass_Review(self):
        """Test if Review is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.rev.__class__, BaseModel), True)

    def test_attribute_types_Review(self):
        """Test attribute types for Review"""
        self.assertEqual(type(self.rev.text), str)
        self.assertEqual(type(self.rev.place_id), str)
        self.assertEqual(type(self.rev.user_id), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', 'DB')
    def test_save_Review(self):
        """Test if save works"""
        self.rev.save()
        self.assertNotEqual(self.rev.created_at, self.rev.updated_at)

    def test_to_dict_Review(self):
        """Test if to_dict works"""
        self.assertEqual('to_dict' in dir(self.rev), True)

    def test_place_id(self):
        """Test the place_id attribute of Review"""
        new = Review()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """Test the user_id attribute of Review"""
        new = Review()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """Test the text attribute of Review"""
        new = Review()
        self.assertEqual(type(new.text), str)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""
Unit tests for City class
"""

import unittest
from models.city import City
from tests.test_models.test_base_model import TestBaseModel


class TestCity(unittest.TestCase):
    """Test cases for City class"""

    def test_attributes(self):
        """Test default attributes of City class"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""
Unit tests for State class
"""

import unittest
from models.state import State
from tests.test_models.test_base_model import TestBaseModel


class TestState(unittest.TestCase):
    """Test cases for State class"""

    def test_attributes(self):
        """Test default attributes of State class"""
        state = State()
        self.assertEqual(state.name, "")
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))


if __name__ == '__main__':
    unittest.main()

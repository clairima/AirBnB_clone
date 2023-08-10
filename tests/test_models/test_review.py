#!/usr/bin/python3
"""
Unit tests for Review class
"""

import unittest
from models.review import Review
from tests.test_models.test_base_model import TestBaseModel


class TestReview(unittest.TestCase):
    """Test cases for Review class"""

    def test_attributes(self):
        """Test default attributes of Review class"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))


if __name__ == '__main__':
    unittest.main()

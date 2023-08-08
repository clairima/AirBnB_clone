#!/usr/bin/python3

"""
This module is for testing BaseModel class
using unittest
"""
import unittest
from sys import path
path.append('../../../AirBnB_clone')
from models.base_model import BaseModel
import datetime

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89

    def test_str(self):
        expected_output = "[BaseModel] ({}){}".format(self.my_model.id, self.my_model.__dict__)
        self.assertEqual(str(self.my_model), expected_output)

    def test_save(self):
        previous_updated_at = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(previous_updated_at, self.my_model.updated_at)

    def test_to_dict(self):
        my_model_json = self.my_model.to_dict()
        self.assertEqual(my_model_json['name'], "My First Model")
        self.assertEqual(my_model_json['my_number'], 89)
        self.assertEqual(my_model_json['__class__'], 'BaseModel')
        self.assertEqual(my_model_json['updated_at'], self.my_model.updated_at.isoformat())
        self.assertEqual(my_model_json['created_at'], self.my_model.created_at.isoformat())

if __name__ == '__main__':
    unittest.main()


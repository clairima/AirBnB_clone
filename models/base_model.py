#!/usr/bin/python3
"""
This module is for Base class -model- which will act
as the back bone of our project, as  defines all common
attributes/methods for other classes:
"""
import datetime
import uuid


class BaseModel:
    """
    This class defines all common attributes/methods for other classes:

    Public instance attributes:
    * id: string - assign with an uuid when an instance is created:
    * created_at: datetime - assign with the current datetime when an
        instance is created
    * updated_at: datetime - assign with the current datetime when an instance
        is created and it will be updated every time you change your object
    """

    def __init__(self):
        """
        The constructor of our instances:
        * creates a unique id using uuid.uuid4()
        * initialize created_at with the current time
        * initialize updated_at with the current time
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self, name='BaseModel'):
        """
        prints: [<class name>] (<self.id>) <self.__dict__>
        """
        return f'[{name}] ({self.id}){self.__dict__}'

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of
        __dict__ of the instance:

        * by using self.__dict__, only instance attributes set
            will be returned
        * a key __class__ must be added to this dictionary with the
            class name of the object
        * created_at and updated_at must be converted to string object
            in ISO format
        """
        temp_dic = self.__dict__
        temp_dic['created_at'] = temp_dic['created_at'].isoformat()
        temp_dic['updated_at'] = temp_dic['updated_at'].isoformat()
        temp_dic['__class__'] = self.__class__.__name__
        return temp_dic

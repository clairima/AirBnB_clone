# AirBnB Clone

This is the README file for the AirBnB Clone project. This project aims to create a simplified version of the AirBnB platform, implementing various functionalities and features.

## BaseModel

The BaseModel class serves as the foundation for other classes within the project. It defines common attributes and methods that are shared among multiple classes. Here are the details of the BaseModel class:

### Public instance attributes

* id: a unique identifier assigned to each instance. It is generated using uuid.uuid4() and converted to a string.
* created_at: a datetime object representing the timestamp when an instance is created.
* updated_at: a datetime object representing the timestamp when an instance is created or updated.

### Public instance methods

* save(self): updates the updated_at attribute with the current datetime.
* to_dict(self): returns a dictionary representation of the instance. It includes all the instance attributes stored in \__dict__ converted to a dictionary format. The created_at and updated_at attributes are converted to string objects in ISO format.

## Creating an Instance from Dictionary Representation

In addition to the basic functionality, the BaseModel class also supports the recreation of an instance from a dictionary representation. This allows for the serialization and deserialization of objects. Here are the details of the update to the BaseModel class:

## Credits

This project is a part of Alx software engineering track.

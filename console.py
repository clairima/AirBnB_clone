#!/usr/bin/python3

"""
This module contains one class, HBNBCommand(cmd.Cmd),
which inherits from cmd class to provide console
interactive interface
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
import shlex


class HBNBCommand(cmd.Cmd):
    """
    This class provides a cmd interface for the project.
    Through it you can create, show, destroy, update
    objects in the file storage, and interact with data.
    """

    prompt = '(hbnb) '

    def do_EOF(self, line):
        """
        Exiting the program when reaching End of file
        """
        print("")
        return True

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_create(self, class_name=None):
        """
        Creates a new instance of class_name,
        saves it (to the JSON file) and prints the id
        """
        if class_name:
            try:
                cls = globals()[class_name]
                obj = cls()
                storage.save()
                print(obj.id)
            except Exception as e:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def handle_args(self, args, expected_args_num):
        """
        Take the args, and the expected number of
        args, and validate input
        (1st arg is always the class name -if found-)
        (2nd arg is always the id -if found-)
        (3rd arg is always the attribute name -if found-)
        (4th arg is always the attribute value -if found-)
        """
        if len(args) == 0:
            print("** class name missing **")
            return 0
        else:
            class_name = args[0]
            try:
                cls = globals()[class_name]
            except Exception as e:
                print("** class doesn't exist **")
                return 0
        expected_args_num -= 1
        if expected_args_num > 0:
            if len(args) == 1:
                print("** instance id missing **")
                return 0
        if expected_args_num > 0:
            obj_id = args[1]
            key = f'{class_name}.{obj_id}'
            all_objs = storage.all()
            if key not in all_objs.keys():
                print("** no instance found **")
                return 0
        expected_args_num -= 1
        if expected_args_num > 0:
            if len(args) == 2:
                print("** attribute name missing **")
                return 0
        expected_args_num -= 1
        if expected_args_num > 0:
            if len(args) == 3:
                print("** value missing **")
                return 0
        return 1

    def do_show(self, line):
        """
         Prints the string representation
         of an instance based on the class name
         and id -if they exist-
        """
        args = shlex.split(line)
        flag = self.handle_args(args, 2)
        if flag:
            all_objs = storage.all()
            key = f'{args[0]}.{args[1]}'
            print(str(all_objs[key]))

    def do_destroy(self, line):
        """
         Deletes an instance based on the class
         name and id (save the change into the
         JSON file).
        """
        args = shlex.split(line)
        flag = self.handle_args(args, 2)
        if flag:
            all_objs = storage.all()
            key = f'{args[0]}.{args[1]}'
            del all_objs[key]
            storage.save()

    def do_all(self, class_name):
        """
         Prints all string representation of all
         instances based or not on the class name.
        """
        flag = 1
        obj_list = []
        all_obj = storage.all()
        if not class_name:
            for value in all_obj.values():
                obj_list.append(str(value))
            print(obj_list)
            flag = 0
        else:
            try:
                cls = globals()[class_name]
            except Exception as e:
                print("** class doesn't exist **")
                flag = 0
        if flag:
            for key, value in all_obj.items():
                if key.split('.')[0] == class_name:
                    obj_list.append(str(value))
            print(obj_list)

    def do_update(self, line):
        """
         Updates an instance based on the class
         name and id by adding or updating attribute
         (save the change into the JSON file).
         Usage:
         update <cls name> <id> <atr name> "<atr value>"
        """
        args = shlex.split(line)
        flag = self.handle_args(args, 4)
        if flag:
            attr_value = args[3].strip('"')
            all_obj = storage.all()
            key = key = f'{args[0]}.{args[1]}'
            setattr(all_obj[key], args[2], attr_value)
            all_obj[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

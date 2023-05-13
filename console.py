#!/usr/bin/python3
"""Define class 'HBNBCommand' """

import cmd
import models

from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """creates console with the following commands"""

    prompt = "(hbnb) "
    __class_list = ['BaseModel', 'Amenity', 'City',
                    'Place', 'Review', 'State', 'User']

    def emptyline(self):
        """executes no command"""
        pass

    def do_EOF(self, line=''):
        """Exit program"""
        print()
        return True

    def do_quit(self, line=''):
        """Quit program"""
        return self.do_EOF()

    def do_create(self, line=''):
        """Create and save a new class instance """
        arg = line.split()
        if len(arg) == 0:
            print("** class name missing **")
            print(arg)
        else:
            cls_name = arg[0]
            if cls_name not in self.__class_list:
                print("** class doesn't exist **")
                print(cls_name)
                print(self.__class_list)
            else:
                try:
                    obj = eval(cls_name)()
                    obj.save()
                    print(obj.id)
                except NameError:
                    print(f"{cls_name} not implemented")

    def do_show(self, line):
        """
        Prints the string rep. of an instance based on the class name & id.
        Usage: show <class name> <id>
        Ex: $ show BaseModel 1234-1234-1234.
        """
        args = line.split()
        obj_dict = models.storage.all()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__class_list:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj_dict = models.storage.all()
            obj_key = "{}.{}".format(args[0], args[1])
            obj = obj_dict.get(obj_key, None)
            if obj is None:
                print("** no instance found **")
            else:
                print(obj)

    def do_destroy(self, line=''):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file)"""

        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__class_list:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj_dict = models.storage.all()
            obj_key = "{}.{}".format(args[0], args[1])
            obj = obj_dict.get(obj_key, None)
            if obj is None:
                print("** no instance found **")
            else:
                try:
                    del obj_dict[obj_key]
                    models.storage.save()
                except Exception as e:
                    print(e)

    def do_all(self, line=''):
        """Prints all string representation of all instances
        based or not on the class name"""

        args = line.split()
        all_list = []
        obj_dict = models.storage.all()
        if args and args[0] not in self.__class_list:
            print("** class doesn't exist **")
            return
        elif not args:
            for key, value in obj_dict.items():
                all_list.append(value.__str__())
        else:
            for key, value in obj_dict.items():
                if key.split('.')[0] == args[0]:
                    all_list.append(value.__str__())
        print(all_list)

    def do_update(self, line=''):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file)"""
        args = line.split()
        obj_dict = models.storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__class_list:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            key = '.'.join(args[:2])
            setattr(obj_dict[key], args[2], args[3])
            models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

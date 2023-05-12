#!/usr/bin/python3
"""Define class 'HBNBCommand' """

import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """creates console with the following commands"""

    prompt = "(hbnb) "
    __class_list = ['BaseModel', 'User']

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
                obj = eval(cls_name)()
                obj.save()
                print(obj.id)

    #def do_show(self, arg):
    #def de_destroy(self, arg):
    #def do_all(self, arg):
    #def do_update(self, arg):
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()

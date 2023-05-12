#!/usr/bin/python3
"""Define class 'HBNBCommand' """

import cmd

class HBNBCommand(cmd.Cmd):
    """creates console with the following commands"""

    cmd.Cmd.prompt = "(hbnb) "

    def emptyline(self):
        'executes no command'
        pass

    def do_EOF(self, line=''):
        'Exit program'
        print()
        return True

    def do_quit(self, line=''):
        'Quit program'
        return self.do_EOF()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

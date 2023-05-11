#!/usr/bin/python3

import cmd


class Console(cmd.Cmd):
    cmd.Cmd.prompt = "(hbnb) "

    def do_EOF(self, line=''):
        'Exit program'
        print()
        return True

    def do_quit(self, line=''):
        'Quit program'
        return self.do_EOF()


if __name__ == '__main__':
    Console().cmdloop()

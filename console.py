#!/usr/bin/python3
import cmd
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, args):
        arg = args.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg[0])())
            storage.save()

    def do_quit(self, arg):
        """Quit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program using Ctrl+D (EOF)"""
        print()
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

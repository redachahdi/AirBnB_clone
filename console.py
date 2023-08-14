#!/usr/bin/python3
"""
This script defines the HBNBCommand class, a command-line interface
for interacting with objects in the HBNB storage engine.
"""
import sys
import shlex
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


def parse(line):
    """
    Parse a given string using shlex and return a list of parsed tokens.
    """
    return shlex.split(line)


class HBNBCommand(cmd.Cmd):
    """
    A command-line interface class that allows users to interact
    with objects in the HBNB storage engine.
    """
    prompt = '(hbnb) '
    methods = ['all', 'show', 'count', 'update', 'destroy']
    classes = [
        'BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']

    def precmd(self, line):
        """
        Implement custom commands for preprocessing the command line input.
        """
        if line == '' or not line.endswith(')'):
            return line

        flag = 1

        for x in self.classes:
            for y in self.methods:
                if line.startswith("{}.{}(".format(x, y)):
                    flag = 0
        if flag:
            return line

        tmp = ''
        for x in self.methods:
            tmp = line.replace('(', '.').replace(')', '.').split('.')
            if tmp[0] not in self.classes:
                return ' '.join(tmp)
            while tmp[-1] == '':
                tmp.pop()
            if len(tmp) < 2:
                return line
            if len(tmp) == 2:
                tmp = '{} {}'.format(tmp[1], tmp[0])
            else:
                tmp = '{} {} {}'.format(tmp[1], tmp[0], tmp[2])
            if tmp.startswith(x):
                return tmp

        return ''

    def emptyline(self):
        """
        Override the default behavior of executing a command on an empty line.
        """
        pass

    def do_create(self, line):
        """
        Create a new instance, save it to the JSON file, and print its id.
        """
        args = parse(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class does not exist **")
        else:
            obj = eval("{}()".format(args[0]))
            print(obj.id)
            models.storage.save()

    def do_show(self, line):
        """
        Print the string representation of an instance.
        """
        args = parse(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class does not exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objs = models.storage.all()
            key = '{}.{}'.format(args[0], args[1])
            try:
                obj = objs[key]
                print(obj)
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        Delete an instance based on the class name and id.
        """
        args = parse(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class does not exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objs = models.storage.all()
            key = '{}.{}'.format(args[0], args[1])
            try:
                obj = objs[key]
                objs.pop(key)
                del obj
                models.storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, line):
        """
        Print string representation of all instances based on class.
        """
        args = parse(line)
        objs = models.storage.all()
        obj_list = []
        if len(args) >= 1:
            if args[0] not in self.classes:
                print("** class does not exist **")
            else:
                for key, obj in objs.items():
                    if key.startswith(args[0]):
                        obj_list.append(obj.__str__())
                print(obj_list)
        else:
            for obj in objs.values():
                obj_list.append(obj.__str__())
            print(obj_list)

    def do_update(self, line):
        """
        Update an instance based on class name, id, and attribute name.
        """
        args = parse(line)
        objs = models.storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class does not exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = '{}.{}'.format(args[0], args[1])
            try:
                obj = objs[key]
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    try:
                        eval(args[3])
                    except (SyntaxError, NameError):
                        args[3] = "'{}'".format(args[3])
                    setattr(obj, args[2], eval(args[3]))
                    obj.save()
            except KeyError:
                print("** no instance found **")

    def do_quit(self, line):
        """
        Exit the program using the 'quit' command.
        """
        return True

    def do_EOF(self, line):
        """
        Exit the program using the 'EOF' (Ctrl+D) command.
        """
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()


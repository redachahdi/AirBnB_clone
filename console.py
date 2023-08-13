#!/usr/bin/python3
"""Defines a Module for the HBNBCommand"""
import cmd
from models import storage
import sys
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """HBNB commandd"""
    prompt = "(hbnb) "
    methods = ['all', 'show', 'count', 'update', 'destroy']
    classes = ['BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']
    def do_create(self, args):
        arg = args.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg[0])())
            storage.save()

    def do_show(self, args):
        arg = args.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            obj_dict = storage.all()
            obj_key = "{}.{}".format(arg[0], arg[1])
            if obj_key in obj_dict:
                obj = obj_dict[obj_key]
                print(obj)
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        arg = args.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            obj_dict = storage.all()
            obj_key = "{}.{}".format(arg[0], arg[1])
            obj = obj_dict[obj_key]
            if obj is None:
                print("** no instance found **")
            else:
                obj_dict.pop(obj_key)
                storage.save()
                return

    def do_quit(self, arg):
        """Quit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program using Ctrl+D (EOF)"""
        print()
        return True

    def emptyline(self):
        pass
    def precmd(self, line):
        """Implement custom commands"""

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
    def do_all(self, line):
        """Prints all string representation of all instances based on class"""
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
        """Updates an instance based on the class name and id and attribute name"""
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


    def parse(line):
    """Parse a given string, and return a list"""
    return shlex.split(line)
if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
"""is the HBNBCommand module"""
import cmd
import models
import sys
import shlex
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """is  the class HBNBCommand"""

    prompt = '(hbnb) '
    methods = ['all', 'show', 'count', 'update', 'destroy']
    classes = ['BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']

    def precmd(self, line):
        """is the of Implement custom commands"""

        if line == '' or not line.endswith(')'):
            return line

        flag = 1

        for k in self.classes:
            for y in self.methods:
                if line.startswith("{}.{}(".format(k, y)):
                    flag = 0
        if flag:
            return line

        tmp = ''
        for k in self.methods:
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
            if tmp.startswith(k):
                return tmp

        return ''

    def emptyline(self):
        """ is the  empty line behavior so no command is executed"""
        pass

    def do_quit(self, line):
        """is the Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """is the EOF command to exit the program"""
        print()
        return True

    def do_create(self, line):
        """that Creates a new instance of BaseModel, saves it """
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
        """is the Prints the string representation """
        args = parse(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class does not exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            _objs = models.storage.all()
            _key = '{}.{}'.format(args[0], args[1])
            try:
                _obj = _objs[_key]
                print(_obj)
            except KeyError:
                print("** no instance found **")
 def do_update(self, line):
        """the instance based on the class name and id and attribute name"""
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
    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = parse(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class does not exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            _objs = models.storage.all()
            _key = '{}.{}'.format(args[0], args[1])
            try:
                _obj = _objs[_key]
                _objs.pop(_key)
                del _obj
                models.storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, line):
        """that Prints all string representation of all instances"""
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


def parse(line):
    """that Parse a given string, and will return the  list"""
    return shlex.split(line)

if __name__ == '__main__':
    HBNBCommand().cmdloop()

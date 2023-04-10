#!/usr/bin/python3
""" Holberton AirBnB console module """
import cmd
import sys
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import shlex

classes = {'BaseModel': BaseModel, "User": User, "State": State, "City": City,
           "Amenity": Amenity, "Place": Place, "Review": Review}


class HBNBCommand(cmd.Cmd):
    """ HBNB class """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """ exit the program """
        exit()

    def do_EOF(self, arg):
        """ exit the program """
        print('')
        exit()

    def emptyline(self):
        """ shouldn't execute anthing """
        pass

    def do_create(self, arg):
        """
         Creates a new instance of BaseModel,
         saves it (to the JSON file) and prints the id
         """
        cmd_args = shlex.split(arg)
        if len(cmd_args) == 0:
            print("** class name missing **")
            return False
        if cmd_args[0] in classes:
            new_instance = classes[cmd_args[0]]()
        else:
            print("** class doesn't exist **")
            return False
        print(new_instance.id)
        new_instance.save()

    def do_show(self, arg):
        """
        Prints the string representation of an
        instance based on the class name and id
        """
        cmd_args = shlex.split(arg)
        if len(cmd_args) == 0:
            print("** class name missing **")
            return False
        if cmd_args[0] in classes:
            if len(cmd_args) > 1:
                key = cmd_args[0] + "." + cmd_args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
         Deletes an instance based on the class name
         and id (save the change into the JSON file
         """
        cmd_args = shlex.split(arg)
        if len(cmd_args) == 0:
            print("** class name missing **")
        elif cmd_args[0] in classes:
            if len(cmd_args) > 1:
                key = cmd_args[0] + "." + cmd_args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """
         Prints all string representation of all
         instances based or not on the class name
         """
        cmd_args = shlex.split(arg)
        obj_list = []
        if len(cmd_args) == 0:
            obj_dict = models.storage.all()
        elif cmd_args[0] in classes:
            obj_dict = models.storage.all(classes[cmd_args[0]])
        else:
            print("** class doesn't exist **")
            return False
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print("[", end="")
        print(", ".join(obj_list), end="")
        print("]")

    def do_update(self, arg):
        """
         Updates an instance based on the class name and id by adding or
         updating attribute (save the change into the JSON file)"""
        args = shlex.split(arg)
        integers = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        floats = ["latitude", "longitude"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                if args[2] in integers:
                                    try:
                                        args[3] = int(args[3])
                                    except ValueError:
                                        args[3] = 0
                                elif args[2] in floats:
                                    try:
                                        args[3] = float(args[3])
                                    except ValueError:
                                        args[3] = 0.0
                            setattr(models.storage.all()[k], args[2], args[3])
                            models.storage.all()[k].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def default(self, arg):
        """ advanced arguments"""
        cmds = ["all", "count", "destroy", "show", "update"]
        n_list = arg.split('.')
        if len(n_list) > 1:
            try:
                instance = n_list[0]
                command = n_list[1].split('(')[0]
                if command not in cmds:
                    print("*** invalid syntax: {} ***".format(arg))
                if command == cmds[0]:
                    self.do_all(instance)
                    return
                if command == cmds[1]:
                    print(models.storage.count(instance))
                    return
                Id = n_list[1].split('(')[1].split(')')[0]
                if command == cmds[2]:
                    Arg = instance + " " + Id
                    self.do_destroy(Arg)
                    return
                if command == cmds[3]:
                    Arg = instance + " " + Id
                    self.do_show(Arg)
                    return
                if command == cmds[4]:
                    Arg = (n_list[-1].split(","))
                    n_id = Arg[0].split("(")[-1]
                    n_name = Arg[1]
                    n_value = Arg[2].split(')')[0]
                    self.do_update("{} \
{} {} {}".format(instance, n_id, n_name, n_value))

                    return
            except IndexError:
                return

        else:
            print("*** invalid syntax: {} ***")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

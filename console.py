#!/usr/bin/python3
"""This module defines entry point of the command interpreter"""
import cmd
import shlex

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Define a custom command interpreter for Airbnb clone"""
    prompt = "(hbnb) "

    def checkClass(self, arg):
        """Run error check on class argument and eval it if possible"""
        arg = arg.split()
        if len(arg) == 0:  # []
            print("** class name missing **")
            return
            # ["<class_name>"]
        try:
            cls = eval(arg[0])  # check if the class object exists
        except (NameError, SyntaxError):
            print("** class doesn't exist **")
            return
        return cls

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
        if self.checkClass(arg) is None:
            return
        obj = self.checkClass(arg)()  # create new instance
        obj.save()  # save object
        print(obj.id)

    def help_create(self):
        """Help text for create command"""
        print("create <class_name>")
        print("Creates a new instance of BaseModel,",
              "saves it (to the JSON file) and prints the id\n")

    def checkId(self, cls, args):
        """Error check id and pass create key from class name
        and id then return key"""
        args = args.split()
        if len(args) == 1:  # ["<class_name>"]
            print("** instance id missing **")
            return
        # ["<class_name>", "<id>", ...]
        id = args[1]
        key = f"{cls.__name__}.{id}"
        # create key for locating instance in storage
        if key not in storage.all().keys():
            print("** no instance found **")
            return
        return (id, key)

    def do_show(self, args):
        """Prints the string representation of an instance based
        on the class name and id"""
        if self.checkClass(args) is None:
            return
        cls = self.checkClass(args)
        if self.checkId(cls, args) is None:
            return
        key = self.checkId(cls, args)[1]
        obj = storage.all()[key]
        print(obj)

    def help_show(self):
        """Help text for show command"""
        print("show <class_name> <id>")
        print("Prints the string representation of an",
              " instance based on the class name and id\n")

    def do_destroy(self, args):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file)"""
        if self.checkClass(args) is None:
            return
        cls = self.checkClass(args)
        if self.checkId(cls, args) is None:
            return
        key = self.checkId(cls, args)[1]
        odict = storage.all()
        odict.pop(key)
        storage.save()

    def help_destroy(self):
        """Help text for destroy command"""
        print("destroy <class_name> <id>")
        print("Deletes an instance based on the class name",
              " and id (save the change into the JSON file)\n")

    def do_all(self, arg):
        """ Prints all string representation of
        all instances based or not on the class name"""
        odict = storage.all()
        if arg != "":
            # create dict with only objects of specified class
            if self.checkClass(arg) is None:
                return
            cls = self.checkClass(arg)
            odict = {key: obj for key, obj in odict.items()
                     if key.startswith(f'{cls.__name__}')}
        # no specified class so use dict with all stored objects
        str_rep = [str(obj) for obj in odict.values()]
        print(str_rep)

    def help_all(self):
        """Help text for all command"""
        print("all <class_name> or all")
        print(" Prints all string representation of all",
              " instances based or not on the class name\n")

    def checkAttr(self, args):
        """Error check attribute name and value"""
        args = shlex.split(args)
        # update City 1614f1f1-b89c-475a-ac45-1504c95b7ff3 name "Los Angeles"
        # treat "Los Angeles" as a single string instead of separate words
        # args = ['City', '1614f1f1-b89c-475a-ac45-1504c95b7ff3',
        #  'name', 'Los Angeles']
        if len(args) == 2:  # ["<class_name>", "<id>", ...]
            print("** attribute name missing **")
            return
        if len(args) == 3:
            # ["<class_name>", "<id>", "<attribute_name>"...]
            print("** value missing **")
            return
        value = args[3]

        # remove quotes from value but value still a string ooo
        if value.isdigit():
            value = int(value)
        else:
            try:
                value = float(args[3])
            except ValueError:
                pass
        return (args[2], value)

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)"""
        if self.checkClass(args) is None:
            return
        cls = self.checkClass(args)
        if self.checkId(cls, args) is None:
            return
        key = self.checkId(cls, args)[1]
        if self.checkAttr(args) is None:
            return
        name, value = self.checkAttr(args)
        obj = storage.all()[key]
        setattr(obj, name, value)
        obj.save()  # update updated_at and save the object to storage

    def help_update(self):
        """Help text for update command"""
        print('update <class name> <id> <attribute name> "<attribute value>"')
        print("Updates an instance based on the class name and id by adding ",
              "or updating attribute (save the change into the JSON file)\n")

    def do_quit(self, line):
        """quit + ENTER exits the program"""
        return True

    def help_quit(self):
        """Help text for quit command"""
        print("quit + ENTER will exit the program\n")

    def do_EOF(self, line):
        """Ctrl-D exits the program"""
        print("")  # shell prompt will shows on a new line
        return True

    def help_EOF(self):
        """Help text for EOF command"""
        print("Ctrl-D will exit the program\n")

    def emptyline(self):
        """empty line + ENTER runs previous command"""
        pass  # force empty line + ENTER to do nothing


if __name__ == "__main__":
    HBNBCommand().cmdloop()

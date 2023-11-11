#!/usr/bin/python3
"""This module defines entry point of the command interpreter
"""
import cmd

from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
        """Define a custom command interpreter for Airbnb clone"""
        prompt = "(hbnb) "

        def checkClass(self, arg):
                """Run error check on class argument and eval it if possible"""
                arg = arg.split()
                if len(arg) == 0:  # []
                        print("** class name missing **")
                        self.cmdloop()
                # ["<class_name>"]
                try:
                        cls = eval(arg[0]) # check if the class object exists
                except NameError:
                        print("** class doesn't exist **")
                        self.cmdloop()
                return cls

        def do_create(self, arg):
                """Creates a new instance of BaseModel,
                saves it (to the JSON file) and prints the id"""
                self.checkClass(arg)()
                 # create new instance and add it to FileStorage.__objects
                storage.save()
                '''serialize the updated FileStorage.__objects
                dictionary and save to the json file'''

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
                        self.cmdloop()
                # ["<class_name>", "<id>", ...]
                id = args[1]
                key = f"{cls.__name__}.{id}"
                # create key for locating instance in storage
                if key not in storage.all().keys():
                        print("** no instance found **")
                        self.cmdloop()
                return(id, key)

        def do_show(self, args):
                """Prints the string representation of an instance based
                  on the class name and id""" # [<class_name>, <id>]
                cls = self.checkClass(args)
                key = self.checkId(cls, args)[1]
                dict_rep = storage.all()[key]
                obj = cls(**dict_rep)  # recreate the object
                print(obj)

        def help_show(self):
                """Help text for show command"""
                print("show <class_name> <id>")
                print("Prints the string representation of an",
                      " instance based on the class name and id\n")
        
        def do_destroy(self, ):
                """Deletes an instance based on the class name
                and id (save the change into the JSON file)"""


        def help_destroy(self):
                """Help text for destroy command"""
                print("destroy <class_name> <id>")
                print("Deletes an instance based on the class name",
                       " and id (save the change into the JSON file)\n")

        def do_all(self, cls):
                """ Prints all string representation of 
                all instances based or not on the class name"""
                if cls != "":
                        try:
                                cls = eval(cls)  # check if the class object exists
                        except NameError:
                                print("** class doesn't exist **")
                                return  # show prompt again
                        else:
                                pass
                else:
                        pass

        def help_all(self):
                """Help text for all command"""
                print("all <class_name> or all")
                print(" Prints all string representation of all",
                      " instances based or not on the class name\n")

        def do_update(self, ):
                """Updates an instance based on the class name and id by adding
                  or updating attribute (save the change into the JSON file)"""

        def help_update(self):
                """Help text for update command"""
                print('update <class name> <id> <attribute name> "<attribute value>"')
                print("Updates an instance based on the class name and id by",
                      " adding or updating attribute (save the change into the JSON file)\n")

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

        def postloop(self):
                """Runs the specified function just before program is exited"""
                pass  # do nothing


if __name__ == "__main__":
        HBNBCommand().cmdloop()

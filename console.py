#!/usr/bin/python3
"""This module defines entry point of the command interpreter
"""
import cmd

from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
        """Define a custom command interpreter for Airbnb clone"""
        prompt = "(hbnb) "

        def do_create(self, cls):
                """Creates a new instance of BaseModel,
                saves it (to the JSON file) and prints the id"""
                if cls == "":
                        print("** class name missing **")
                try:
                        eval(cls) # check if the class object exists
                except NameError:
                        print("** class doesn't exist **")
                else:
                        obj = eval(cls)()
                        # create new instance and add it to FileStorage.__objects
                        storage.save()
                        '''serialize the updated FileStorage.__objects
                        dictionary and save to the json file'''

        def help_create(self):
                """Help text for create command"""
                print("create <class_name>")
                print("Creates a new instance of BaseModel,",
                      "saves it (to the JSON file) and prints the id\n")

        def do_show(self, args):
                """Prints the string representation of an instance based
                  on the class name and id"""
                args = args.split()  # [<class_name>, <id>]
                if len(args) == 0:
                        print("** class name missing **")
                try:
                        cls = args[0]
                        eval(cls)  # check if the class object exists
                except NameError:
                        print("** class doesn't exist **")
                if len(args) == 1:
                        print("** instance id missing **")
                else:
                        cls, id = args  # unpack list
                        


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

        def do_all(self, ):
                """ Prints all string representation of 
                all instances based or not on the class name"""

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

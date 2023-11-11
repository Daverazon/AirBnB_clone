#!/usr/bin/python3
"""This module defines entry point of the command interpreter
"""
import cmd

from models.base_model import BaseModel
from models.user import User
from models import storage


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
                        cls = eval(arg[0]) # check if the class object exists
                except (NameError, SyntaxError):
                        print("** class doesn't exist **")
                        return
                return cls

        def do_create(self, arg):
                """Creates a new instance of BaseModel,
                saves it (to the JSON file) and prints the id"""
                if self.checkClass(arg) == None:
                        return
                obj = self.checkClass(arg)()
                # create new instance and add it to FileStorage.__objects
                storage.save()
                '''serialize the updated FileStorage.__objects
                dictionary and save to the json file'''
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
                return(id, key)

        def do_show(self, args):
                """Prints the string representation of an instance based
                  on the class name and id"""
                if self.checkClass(args) == None:
                        return
                cls = self.checkClass(args)
                if self.checkId(cls, args) == None:
                        return
                key = self.checkId(cls, args)[1]
                dict_rep = storage.all()[key]
                obj = cls(**dict_rep)  # recreate the object
                print(obj)

        def help_show(self):
                """Help text for show command"""
                print("show <class_name> <id>")
                print("Prints the string representation of an",
                      " instance based on the class name and id\n")
        
        def do_destroy(self, args):
                """Deletes an instance based on the class name
                and id (save the change into the JSON file)"""
                if self.checkClass(args) == None:
                        return
                cls = self.checkClass(args)
                if self.checkId(cls, args) == None:
                        return
                key = self.checkId(cls, args)[1]
                objects = storage.all()
                objects.pop(key)
                storage.save()

        def help_destroy(self):
                """Help text for destroy command"""
                print("destroy <class_name> <id>")
                print("Deletes an instance based on the class name",
                       " and id (save the change into the JSON file)\n")

        def do_all(self, arg):
                """ Prints all string representation of 
                all instances based or not on the class name"""
                objects = storage.all()
                if arg != "":
                        # create dict with only objects of specified class
                        if self.checkClass(arg) == None:
                                return
                        cls = self.checkClass(arg)
                        objects = {key: dict_rep for key, dict_rep in objects.items() if key.startswith(f'{cls.__name__}')}
                # no specified class so use dict with all stored objects
                str_rep = []
                for key, dict_rep in objects.items():
                        cls = key.split(sep='.')[0]  # ['<class_name>', '<id>']
                        obj = eval(cls)(**dict_rep)  # recreate object
                        str_rep.append(str(obj))  # add string rep to list
                print(str_rep)

        def help_all(self):
                """Help text for all command"""
                print("all <class_name> or all")
                print(" Prints all string representation of all",
                      " instances based or not on the class name\n")

        def checkAttr(self, args):
                """Error check attribute name and value"""
                args = args.split()
                if len(args) == 2:  # ["<class_name>", "<id>", ...]
                        print("** attribute name missing **")
                        return
                if len(args) == 3:
                        # ["<class_name>", "<id>", "<attribute_name>"...]
                        print("** value missing **")
                        return
                value = args[3]

                if value.startswith('"') and value.endswith('"'):
                        value = value[1:-1]
                if value.startswith("'") and value.endswith('"'):
                        value = value[1:-1]
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
                if self.checkClass(args) == None:
                        return
                cls = self.checkClass(args)
                if self.checkId(cls, args) == None:
                        return
                key = self.checkId(cls, args)[1]
                if self.checkAttr(args) == None:
                        return
                name, value = self.checkAttr(args)
                dict_rep = storage.all()[key]
                obj = cls(**dict_rep)  # recreate the object
                print(name, value)
                setattr(obj, name, value)
                obj.save()  # update updated_at
                storage.new(obj)  # add update object to FileStorage.__objects
                storage.save()  # save objects to file.json

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

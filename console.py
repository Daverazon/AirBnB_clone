#!/usr/bin/python3
"""This module defines entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Define a custom command interpreter for Airbnb clone"""
    prompt = "(hbnb) "
def do_quit(self, line):                                            """quit + ENTER exits the program"""
                    return True
                                                                                        def help_quit(self):
                                                                                                """Help text for quit command"""                                print("quit + ENTER will exit the program\n")

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

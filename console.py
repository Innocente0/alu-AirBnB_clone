#!/usr/bin/python3
"""Defines AirBnB console."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter."""

    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def help_quit(self):
        """Print help message for quit command."""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Print help message for EOF command."""
        print("EOF signal to exit the program")


if __name__ == "__main__":
    HBNBCommand().cmdloop()

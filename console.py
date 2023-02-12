#!/usr/bin/python3
<<<<<<< HEAD
"""Define AirBnB clone console"""
import cmd
import sys
import shlex
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """
        Starting point of command interpreter
    """

    prompt = ("(hbnb) ")

    def emptyline(self):
        """pass and do nothing with input line"""
        pass

    def do_quit(self, args):
        return True

    def do_EOF(self, args):
        return True

    def default(self, args):
        """ Default catches all function names not spcifically defined"""
        functs = {"all": self.do_all,
                  "update": self.do_update,
                  "show": self.do_show,
                  "count": self.do_count,
                  "destroy": self.do_destroy}
        args = (args.replace("(", ".").replace(")", ".")
                    .replace('"', "").replace(",", "").split("."))

        try:
            commands = args[0] + " " + args[2]
            func = functs[args[1]]
            func(commands)
        except:
            print("*** Unknown syntax:", args[0])

    def do_create(self, args):
        """Creates new instance of class BaseModel
        saves it to json file
        """

        if len(args) == 0:
            print("** class name missing **")
            return

        try:
            args = shlex.split(args)
            newModel = eval(args[0])()
            newModel.save()
            print(newModel.id)

        except:
            print("** class doesn't exist **")

    def do_show(self, args):
        """
           prints string reps of instance based on class name and ID
        """
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        storage = FileStorage()
        storage.reload()
        object_dict = storage.all()

        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        keys = args[0] + "." + args[1]
        keys = args[0] + "." + args[1]
        try:
            Value = object_dict[keys]
            print(Value)
        except KeyError:
            print("** no instance found **")

    def do_count(self, args):
        """
            counts numb of instances
        """
        object_list = []
        storage = FileStorage()
        storage.reload()
        objects = storage.all()
        try:
            if len(args) != 0:
                eval(args)
        except NameError:
            print("** class doesn't exist **")
            return
        for keys, value in objects.items():
            if len(args) != 0:
                if type(value) is eval(args):
                    object_list.append(value)
            else:
                object_list.append(value)
        print(len(object_list))

    def do_destroy(self, args):
        """ deletes instance base on class name and id """
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        classN = args[0]
        classI = args[1]
        storage = FileStorage()
        storage.reload()
        object_dict = storage.all()
        try:
            eval(classN)
        except NameError:
            print("** class doesn't exist **")
            return
        keys = classN + "." + classI
        try:
            del object_dict[keys]
        except KeyError:
            print("** no instance found **")
        storage.save()

    def do_update(self, args):
        """ Updates instance on name and ID passed in """
        storage = FileStorage()
        storage.reload()
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        keys = args[0] + "." + args[1]
        object_dict = storage.all()
        try:
            object_value = object_dict[keys]
        except KeyError:
            print("** no instance found **")
            return
        try:
            attribute_type = type(getattr(object_value, args[2]))
            args[3] = attribute_type(args[3])
        except AttributeError:
            pass
        setattr(object_value, args[2], args[3])
        object_value.save()

    def do_all(self, args):
        """ Prints all string reps of all instances """
        object_list = []
        storage = FileStorage()
        storage.reload()
        objects = storage.all()
        try:
            if len(args) != 0:
                eval(args)
        except NameError:
            print("** class doesn't exist **")
            return
        for keys, value in objects.items():
            if len(args) != 0:
                if type(value) is eval(args):
                    object_list.append(value.__str__())
            else:
                object_list.append(value.__str__())
        print(object_list)


if __name__ == "__main__":
    """ Start point for loop """
=======
"""
This file defines the console class which will
serve as the entry point of the entire project
"""
from cmd import Cmd
from models import storage
from models.engine.error import *
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


# Global variable of registered models
classes = storage.models


class HBNBCommand(Cmd):
    """
    The Console based driver of the AirBnb Clone
    All interactions with the system is done via
    this class"""

    prompt = "(hbnb) "

    """Commands"""
    def do_EOF(self, args):
        """Exit the programme in non-interactive mode"""
        return True

    def do_quit(self, args):
        """Quit command exit the program"""
        return True

    def do_create(self, args):
        """Create an instance of Model given its name eg.
        $ create ModelName
        Throws an Error if ModelName is missing or doesn't exist"""
        args, n = parse(args)

        if not n:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif n == 1:
            # temp = classes[args[0]]()
            temp = eval(args[0])()
            print(temp.id)
            temp.save()
        else:
            print("** Too many argument for create **")
            pass

    def do_show(self, arg):
        """Show an Instance of Model base on its ModelName and id eg.
        $ show MyModel instance_id
        Print error message if either MyModel or instance_id is missing
        Print an Error message for wrong MyModel or instance_id"""
        args, n = parse(arg)

        if not n:
            print("** class name missing **")
        elif n == 1:
            print("** instance id missing **")
        elif n == 2:
            try:
                inst = storage.find_by_id(*args)
                print(inst)
            except ModelNotFoundError:
                print("** class doesn't exist **")
            except InstanceNotFoundError:
                print("** no instance found **")
        else:
            print("** Too many argument for show **")
            pass

    def do_destroy(self, arg):
        """Deletes an Instance of Model base on its ModelName and id eg.
        $ destroy MyModel instance_id
        Print error message if either MyModel or instance_id is missing
        Print an Error message for wrong MyModel or instance_id"""
        args, n = parse(arg)

        if not n:
            print("** class name missing **")
        elif n == 1:
            print("** instance id missing **")
        elif n == 2:
            try:
                storage.delete_by_id(*args)
            except ModelNotFoundError:
                print("** class doesn't exist **")
            except InstanceNotFoundError:
                print("** no instance found **")
        else:
            print("** Too many argument for destroy **")
            pass

    def do_all(self, args):
        """Retrieve all instances: eg.
        $ all
        $ all MyModel
        if MyModel is passed returns only instances of MyModel"""
        args, n = parse(args)

        if n < 2:
            try:
                print(storage.find_all(*args))
            except ModelNotFoundError:
                print("** class doesn't exist **")
        else:
            print("** Too many argument for all **")
            pass

    def do_update(self, arg):
        """Updates an instance base on its id eg
        $ update Model id field value
        Throws errors for missing arguments"""
        args, n = parse(arg)
        if not n:
            print("** class name missing **")
        elif n == 1:
            print("** instance id missing **")
        elif n == 2:
            print("** attribute name missing **")
        elif n == 3:
            print("** value missing **")
        else:
            try:
                storage.update_one(*args[0:4])
            except ModelNotFoundError:
                print("** class doesn't exist **")
            except InstanceNotFoundError:
                print("** no instance found **")

    def do_models(self, arg):
        """Print all registered Models"""
        print(*classes)

    def handle_class_methods(self, arg):
        """Handle Class Methods
        <cls>.all(), <cls>.show() etc
        """

        printable = ("all(", "show(", "count(", "create(")
        try:
            val = eval(arg)
            for x in printable:
                if x in arg:
                    print(val)
                    break
            return
        except AttributeError:
            print("** invalid method **")
        except InstanceNotFoundError:
            print("** no instance found **")
        except TypeError as te:
            field = te.args[0].split()[-1].replace("_", " ")
            field = field.strip("'")
            print(f"** {field} missing **")
        except Exception as e:
            print("** invalid syntax **")
            pass

    def default(self, arg):
        """Override default method to handle class methods"""
        if '.' in arg and arg.split('.')[0] in classes and arg[-1] == ')':
            return self.handle_class_methods(arg)
        return Cmd.default(self, arg)

    def emptyline(self):
        """Override empty line to do nothing"""
        return


def parse(line: str):
    """splits a line by spaces"""
    args = shlex.split(line)
    return args, len(args)


if __name__ == "__main__":
>>>>>>> 87da65c5732b90e2be8e18d9cc9c3855427c9c68
    HBNBCommand().cmdloop()

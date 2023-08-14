#!/usr/bin/python3
"""AirBnB project entry point- the commandline interpreter """

import cmd
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.state import State
from models.city import City

all_classes = {
    "BaseModel": BaseModel,
    "User": User,
    "Amenity": Amenity,
    "Review": Review,
    "Place": Place,
    "State": State,
    "City": City
}


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        print("GoodBye!")
        return True

    def do_EOF(self, arg):
        """Exit the program using Ctrl-D (EOF)"""
        print()
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of any class and save it"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in all_classes:
            print("** class doesn't exist **")
            return
        all_cls = globals().get(arg, None)
        new_instance = all_cls()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in all_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[key])

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in all_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key in storage.all():
            del (storage.all()[key])
            storage.save_to_file()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print all string representations of instances"""
        args = arg.split()
        instances = []
        if not args:
            for instance in storage.all().values():
                instances.append(str(instance))
        else:
            class_name = args[0]
            if class_name not in all_classes:
                print("** class doesn't exist **")
                return
            for key, instance in storage.all().items():
                if class_name == key.split('.')[0]:
                    instances.append(str(instance))
        print(instances)

    def do_update(self, arg):
        """Update an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in all_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        value = args[3]
        instance = storage.all()[key]
        setattr(instance, attribute_name, value)
        instance.save()

    def do_count(self, arg):
        """Print the count all class instances"""
        current_class = globals().get(arg, None)
        if current_class is None:
            print("** class doesn't exist **")
            return
        count = 0
        for obj in storage.all().values():
            if obj.__class__.__name__ == arg:
                count += 1
        print(count)

    def default(self, arg):
        if arg is None:
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()

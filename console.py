#!/usr/bin/python3

import cmd
import json
from models.base_model import BaseModel


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
        """Create a new instance of BaseModel and save it"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key in BaseModel.__objects:
            print(BaseModel.__objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key in BaseModel.__objects:
            del BaseModel.__objects[key]
            BaseModel.save_to_file()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print all string representations of instances"""
        args = arg.split()
        instances = []
        if not args:
            for instance in BaseModel.__objects.values():
                instances.append(str(instance))
        else:
            class_name = args[0]
            if class_name not in ["BaseModel"]:
                print("** class doesn't exist **")
                return
            for key, instance in BaseModel.__objects.items():
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
        if class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in BaseModel.__objects:
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
        instance = BaseModel.__objects[key]
        setattr(instance, attribute_name, value)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

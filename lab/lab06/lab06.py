import sys


def validate_flags(args):
    if args[1] in ["-p", "-i", "-h", "-w", "-r"]:
        return True
    else:
        return False


def flags(args):
    if args[1] == "-p":
        print_args(args[2:])
    if args[1] == "-i":
        print("Hello World")
    if args[1] == "-h":
        help_command = ["Valid flags:", "-p : prints out all the command line arguments after the -p",
                        "-i : prints \"Hello World\"", "-h : prints out a help command"]
        for item in help_command:
            print(item)
    if args[1] == "-w":
        if len(args) > 3:
            with open(args[2], "w") as my_file:
                for arg in args[3:]:
                    my_file.write(arg + "\n")
        else:
            print("No Content Provided")
    if args[1] == "-r":
        with open(args[2], "r") as my_file:
            for line in my_file.read().split():
                print(line)


def print_args(args):
    for arg in args:
        print(arg)


if validate_flags(sys.argv):
    flags(sys.argv)
else:
    print_args(sys.argv)

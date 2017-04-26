"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    the_dojo tcp <host> <port> [--timeout=<seconds>]
    the_dojo serial <port> [--baud=<n>] [--timeout=<seconds>]
    the_dojo add_room <room_type> <room_name>...
    the_dojo add_person <person_name> (FELLOW|STAFF) [wants_accommodation]
    the_dojo (-i | --interactive) 
    the_dojo (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class Thedojo (cmd.Cmd):
    intro = 'The Dojo Awaits You!!' \
        + ''
    prompt = '(the_dojo) '
    file = None

    @docopt_cmd
    def do_tcp(self, arg):
        """Usage: tcp <host> <port> [--timeout=<seconds>]"""

        print(arg)

    @docopt_cmd
    def do_serial(self, arg):
        """Usage: serial <port> [--baud=<n>] [--timeout=<seconds>]
Options:
    --baud=<n>  Baudrate [default: 9600]
        """

        print(arg)

    @docopt_cmd
    def do_add_room(self, arg):
        """Usage: add_room <room_type> <room_name>...
        """

        print(arg)

    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: add_person <person_name> (FELLOW|STAFF) [wants_accommodation]
        """

        print(arg)

    def do_quit(self, arg):
        """Quit from interface."""

        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    Thedojo().cmdloop()

print(opt)
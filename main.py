"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    the_dojo create_room <room_type> <room_name>...
    the_dojo add_person <person_name> (FELLOW|STAFF) [wants_accommodation]
    the_dojo (-i | --interactive)
    the_dojo (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from termcolor import cprint
from pyfiglet import figlet_format
from models.dojo import Dojo
from docopt import docopt, DocoptExit

my_dojo_object = Dojo()


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as exit:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('You have entered an invalid command!')
            print(exit)
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

    cprint(figlet_format('the\n' + 'Dojo\n', font='univers'), 'green', attrs=['bold'])
    intro = ('Welcome To The Dojo \n\nType "help" To View More Commands or "quit" To Exit Applicaton \n\n------------------'
             '\n\nCOMMANDS \n\n------------------ \n\n1 - add_person <person_name> (FELLOW|STAFF) [wants_accommodation] \n2 - create_room <room_type> <room_name>...')
    prompt = '(the_dojo) '



    file = None

    @docopt_cmd
    def do_add_person(self, args):
        """Usage: add_person <person_name> (FELLOW|STAFF) [wants_accommodation]"""
        print(args)

    @docopt_cmd
    def do_create_room(self, args):
        """Usage: create_room <room_type> <room_name>..."""

        for room_name in args["<room_name>"]:
            my_dojo_object.create_room(["<room_type>"], room_name)

    def do_quit(self, arg):
        """Quit from interface."""

        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    Thedojo().cmdloop()

print(opt)
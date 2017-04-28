"""
Usage:
    create_room <room_type> <room_name>
    add_person <person_id> <first_name> <last_name> <F|S> [--wants_accomodation=N]
    reallocate_person <firstname> <lastname> <new_room_name>
    load_people <filename>
    print_allocations [--o=filename]
    print_unallocated [--o=filename]
    print_room <room_name>
    quit
"""

from models.dojo import Dojo
import sys, cmd, os
from termcolor import cprint, colored
from pyfiglet import figlet_format
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

def introduction():
     print (__doc__)

def save_state_on_interrupt():
    print("saving state...")
    Dojo.save_state()


class DojoApplication(cmd.Cmd):
    cprint(figlet_format('the\n' + 'Dojo\n', font='univers'), 'green', attrs=['bold'])
    prompt = '(the_dojo) '



    def do_quit(self, arg):
        '''Usage: quit application '''

        exit()


if __name__ == '__main__':
    introduction()
    try:
        DojoApplication().cmdloop()
    except KeyboardInterrupt:
        save_state_on_interrupt()

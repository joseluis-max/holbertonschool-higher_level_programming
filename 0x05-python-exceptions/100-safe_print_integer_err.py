#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as VE:
        print("Exception: {}".format(VE), file=sys.stderr)
    except TypeError as TE:
        print("Exception: {}".format(TE), file=sys.stderr)
    return False

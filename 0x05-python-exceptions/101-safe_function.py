#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    rel = None
    try:
        rel = fct(*args)
    except ZeroDivisionError as ZDE:
        print("Exception: {}".format(ZDE), file=sys.stderr)
    except IndexError as IE:
        print("Exception: {}".format(IE), file=sys.stderr)
    return rel

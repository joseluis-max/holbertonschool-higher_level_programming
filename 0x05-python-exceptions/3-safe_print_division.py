#!/usr/bin/python3
def safe_print_division(a, b):
    rel = None
    try:
        rel = a / b
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(rel))
    return rel

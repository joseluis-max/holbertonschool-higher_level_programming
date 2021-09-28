#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    n = 0
    try:
        while i < x:
            try:
                print("{:d}".format(my_list[i]), end="")
                i += 1
                n += 1
            except (ValueError, TypeError):
                i += 1
                continue
    except IndexError:
        raise
    print()
    return n

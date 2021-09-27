#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    op = 0
    i = 0
    try:
        while i < list_length:
            try:
                op = my_list_1[i] / my_list_2[i]
            except ZeroDivisionError:
                op = 0
                print("division by 0")
            except TypeError:
                op = 0
                print("wrong type")
            result.append(op)
            i += 1
    except IndexError:
        print("out of range")
        result.append(0)
    finally:
        return result

#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    op = 0
    i = 0
    while i < list_length:
        try:
            op = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            op = 0
            print("division by 0")
        except TypeError:
            op = 0
            print("wrong type")
        except IndexError:
            op = 0
            print("out of range")
        finally:
            result.append(op)
            i += 1
    return result

#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    len = len(argv)
    operator = argv[2]
    a = int(argv[1])
    b = int(argv[3])
    rel = 0
    if len - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if operator == '+':
        rel = add(a, b)
    elif operator == '-':
        rel = sub(a, b)
    elif operator == '*':
        rel = mul(a, b)
    elif operator == '/':
        rel = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{:d} {:s} {:d} = {:d}".format(a, operator, b, rel))

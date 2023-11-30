#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    i = len(sys.argv) - 1

    if i != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>", file=sys.stderr)
        exit(1)
    elif sys.argv[2] not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        from calculator_1 import add, sub, mul, div
        a = int(sys.argv[1])
        b = int(sys.argv[-1])
        op = sys.argv[2]
        if op == "+":
             print("{} + {} = {}".format(a, b, add(a, b)))
        elif op == "-":
             print("{} + {} = {}".format(a, b, sub(a, b)))
        elif op == "*":
             print("{} + {} = {}".format(a, b, sub(a, b)))
        else:
             print("{} + {} = {}".format(a, b, div(a, b)))

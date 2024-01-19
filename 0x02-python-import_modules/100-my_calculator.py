#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    if (len(argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operators = ['+', '-', '*', '/']
    functions = [add, sub, mul, div]
    op = argv[2]
    a = int(argv[1])
    b = int(argv[3])

    for i in range(0, 4):
        if (op == operators[i]):
            print(f"{a} {operators[i]} {b} = {functions[i](a, b)}")

        elif(argv[2] not in list(operators)):
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

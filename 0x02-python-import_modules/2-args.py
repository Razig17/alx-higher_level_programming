#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    argc = len(argv) - 1
    if (argc == 0):
        print("0 arguments.")
    elif (argc == 1):
        print(f"1 argument:\n1: {argv[1]}")
    else:
        print(f"{argc} arguments:")
        for i in range(1, argc + 1):
            print(f"{i}: {argv[i]}")

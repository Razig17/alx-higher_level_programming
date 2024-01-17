#!/usr/bin/python3
for i in range(0, 8):
    j = i + 1
    while (j < 10):
        print(f"{i}{j}", end=", ")
        j += 1
    i += 1
else:
    print(f"{i}{i + 1}")

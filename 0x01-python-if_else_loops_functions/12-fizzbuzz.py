#!/usr/bin/python3

for i in range(1, 101):
    if i % 3 == 0 or i % 5 == 0:
        if i % 3 == 0: 
            print("Fizz", end=" ")
        else:
            print("Buzz", end=" ")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")
    else:
        print("{:d}".format(i), end=" ")

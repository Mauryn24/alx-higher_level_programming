#!/usr/bin/python3
for a in range(1, 101):
    if (a % 3 == 0):
        print("Fizz", end=" ")
    if (a % 5 == 0):
        print("Buzz", end=" ")
    if (a % 3 == 0) or (a % 5 == 0):
        print("FizzBuzz", end=" ")

#!/usr/bin/python3
for a in range(1, 101):
    if (a % 3 == 0):
        print("Fizz")
    if (a % 5 == 0):
        print("Buzz")
    if (a % 3 == 0) or (a % 5 == 0):
        print("FizzBuzz")

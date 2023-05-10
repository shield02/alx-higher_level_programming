#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastd = number % 10
less6 = 'and is less than 6 and not 0'
if number < 0 and lastd != 0:
    print(f'Last digit of {number:d} is {number % -10:d} '+less6)
elif number < 0 and lastd == 0:
    print(f'Last digit of {number:d} is {lastd:d} and is 0')
elif lastd == 0:
    print(f'Last digit of {number:d} is {lastd:d} and is 0')
elif lastd > 5:
    print(f'Last digit of {number:d} is {lastd:d} and is greater than 5')
elif lastd < 6 and lastd != 0:
    print(f'Last digit of {number:d} is {lastd:d} '+less6)

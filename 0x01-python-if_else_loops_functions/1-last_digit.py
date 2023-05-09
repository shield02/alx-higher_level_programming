#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastd = int(str(number)[-1])
if lastd == 0:
    print(f'Last digit of {number:d} is {lastd:d} and is 0')
elif lastd > 5:
    print(f'Last digit of {number:d} is {lastd:d} and is greater than 5')
elif lastd < 6 and lastd != 0:
    print(f'Last digit of {number:d} is {lastd:d} and is less than 6 and not 0')

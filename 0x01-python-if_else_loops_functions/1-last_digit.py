#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastd = int(str(number)[-1])
less6 = 'and is less than {6:d} and not {0:d}'
if number < 0 and lastd != 0:
    print(f'Last digit of {number:d} is {str(number)[0]}{str(lastd)} {less6}')
elif number < 0 and lastd == 0:
    print(f'Last digit of {number} is {lastd:d} and is {0:d}')
elif lastd == 0:
    print(f'Last digit of {number:d} is {lastd:d} and is {0:d}')
elif lastd > 5:
    print(f'Last digit of {number:d} is {lastd:d} and is greater than {5:d}')
elif lastd < 6 and lastd != 0:
    print(f'Last digit of {number:d} is {lastd:d} {less6}')

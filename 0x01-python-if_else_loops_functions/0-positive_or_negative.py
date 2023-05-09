#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if 0 == number:
    print(f'{number} is Zero')
elif number > 0:
    print(f'{number} is positive')
else:
    print(f'{number} is negative')

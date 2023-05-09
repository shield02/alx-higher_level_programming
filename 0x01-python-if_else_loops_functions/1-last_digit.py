#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0 and int(str(number)[-1]) != 0:
    print(f'Last digit of {number:d} is {str(number)[0]}{int(str(number)[-1]):d} and is less than 6 and not 0')
elif number < 0 and int(str(number)[-1]) == 0:
    print(f'Last digit of {number:d} is {int(str(number)[-1]):d} and is less than 6 and not 0')
elif int(str(number)[-1]) == 0:
    print(f'Last digit of {number:d} is {int(str(number)[-1]):d} and is 0')
elif int(str(number)[-1]) > 5:
    print(f'Last digit of {number:d} is {int(str(number)[-1]):d} and is greater than 5')
elif int(str(number)[-1]) < 6 and int(str(number)[-1]) != 0:
    print(f'Last digit of {number:d} is {int(str(number)[-1]):d} and is less than 6 and not 0')

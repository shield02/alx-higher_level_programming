#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    args = sys.argv
    argslen = len(args)
    if argslen != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operators = args[2]
    a = int(args[1])
    b = int(args[3])

    def get_operator(argument):
        opr_sym = {
            "+": add(a, b),
            "-": sub(a, b),
            "*": mul(a, b),
            "/": div(a, b)
        }
        return (opr_sym.get(argument))
    if args[2] in ('+', '-', '*', '/'):
        print("{} {} {} = {}".format(a, operators, b, get_operator(operators)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

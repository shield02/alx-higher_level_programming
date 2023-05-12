#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argslen = len(sys.argv) - 1
    output = 0
    for i in range(1, argslen + 1):
        output += int(sys.argv[i])
    print(output)

#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argslen = len(sys.argv) - 1
    k = 0
    for i in range(1, argslen + 1):
        k += int(sys.argv[i])
    print(k)

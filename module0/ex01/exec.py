import sys

if (len(sys.argv) > 1):

    args = sys.argv[1:]
    print("".join(args)[::-1].swapcase())


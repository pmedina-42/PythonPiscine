import sys

if len(sys.argv) == 2:
    arg = sys.argv[1]
    if arg.isnumeric():
        print(("I'm odd","I'm even", "I'm zero") [(int(arg) == 0) + (int(arg) % 2 == 0)])
    else:
        print("Error")

if len(sys.argv) > 2:
    print("More than one argument provided")

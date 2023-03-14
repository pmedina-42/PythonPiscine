import sys
import string

def print_error(s):
    print(s)
    exit(1)

def create_list(argv, l):
    list = []
    for arg in argv.split():
        if len(arg.strip(string.punctuation)) > int(l):
            print(len(arg.strip(string.punctuation)))
            list.append(arg.strip(string.punctuation))
    return list

def main():
    if len(sys.argv) != 3:
        print_error("Bad arguments")
    if sys.argv[1].isnumeric():
        print_error("Numeric 1st argument")
    if not sys.argv[2].isnumeric():
        print_error("Non numeric 2nd argument")

    l = sys.argv[2]
    argv = sys.argv[1]
    print(create_list(argv, l))




if __name__ == '__main__':
    main()
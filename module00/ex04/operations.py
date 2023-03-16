import sys

if len(sys.argv) != 3:
    print("Bad arguments")
    exit(1)

a = sys.argv[1]
b = sys.argv[2]

try:
    print(f"Sum: {int(a) + int(b)}")
    print(f"Difference: {int(a) - int(b)}")
    print(f"Product: {int(a) * int(b)}")
    if int(b) == 0:
        print("Quotient: ERROR (division by zero)")
        print(f"Remainder: ERROR (modulo by zero)")
    else:
        print(f"Quotient: {int(a) / int(b)}")
        print(f"Remainder: {int(a) % int(b)}")

except:
    print("Bad format")
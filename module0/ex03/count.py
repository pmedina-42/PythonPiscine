import string
import sys

def text_analyzer(*s):
    if (s):
        st = s[0]
    else:
        st = input("Enter string: ")

    if st.isnumeric():
        print("Not a string")
        exit(1)
    total = len(st)
    sp = st.count(' ')
    p = sum(1 for c in st if c in string.punctuation)
    u = 0
    l = 0

    for c in st:
        if c.isupper():
            u += 1
        if c.islower():
            l += 1

    print(f"The text contains {total} character(s):")
    print(f"- {u} upper letter(s)")
    print(f"- {l} lower letter(s)")
    print(f"- {p} punctuation mark(s)")

    print(f"- {sp} space(s)")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("Bad arguments")
        exit(1)

    if len(sys.argv) == 2:
        text_analyzer(sys.argv[1])


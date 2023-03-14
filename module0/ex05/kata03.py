kata = "The right formatu6tyjdrhsgeawty6setg8eurstgbdfg"

def main():
    print("{z}{s}".format(z=len(kata) <= 42
                          and "".join('-'*(42 - len(kata) - 1))
                          or "",
                          s=kata[:41]))


if __name__ == '__main__':
    main()
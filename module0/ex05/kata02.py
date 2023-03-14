kata = (2019, 9, 25, 3, 30)

def reformat(i):
    return "{z}{i}".format(i=i, z=i <= 9 and '0' or '')

def main():
    print(f"{reformat(kata[1])}/{reformat(kata[2])}/{kata[0]} {reformat(kata[3])}:{reformat(kata[4])}")


if __name__ == '__main__':
    main()
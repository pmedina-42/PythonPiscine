from kata02 import reformat

kata = (0, 4, 132.42222, 10000, 12345.67)


def main():

    print(f"module_{reformat(kata[0])}, "
          f"ex_{reformat(kata[1])} : "
          f"{round(kata[2], 2)}, "
          f"{'%.2e' % kata[3]} "
          f"{'%.2e' % kata[4]}")


if __name__ == '__main__':
    main()
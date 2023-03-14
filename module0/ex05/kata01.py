kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

def main():
    for key in kata:
        print(f"{key} was created by {kata[key]}")


if __name__ == '__main__':
    main()
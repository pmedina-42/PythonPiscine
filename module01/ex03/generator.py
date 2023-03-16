import random


def ft_generator(text, sep=" ", option=None):
    try:
        if text.isprintable():
            lst = text.split(sep)
            match str(option):
                case 'shuffle':
                    lst2 = []
                    while len(lst) > 0:
                        random_index = random.randint(0, len(lst) - 1)
                        random_element = lst[random_index]
                        lst2.append(random_element)
                        lst.pop(random_index)
                    lst = lst2
                case 'ordered':
                    lst.sort()
                case 'unique':
                    lst = list(dict.fromkeys(lst))
                case _:
                    raise
            for elem in lst:
                yield elem
        else:
            raise

    except:
        print('Error')


if __name__ == '__main__':

    for elem in ft_generator('Hola que tal estas estas tu tu tu', ' ', 'shuffle'):
        print(elem)
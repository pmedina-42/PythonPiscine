import functools
from ft_map import ft_map
from ft_filter import ft_filter
from ft_reduce import ft_reduce

def sum(a):
    return a + 1

def sum2(a, b):
    return a + b

def check(a):
    return isinstance(a, int)

if __name__ == '__main__':
    lst = [1, 2.0, 4, 7.0]
    print(ft_map(sum, lst))
    print(ft_filter(check, lst))
    print(ft_reduce(sum2, lst))

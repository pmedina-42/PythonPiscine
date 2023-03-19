import functools

def ft_map(function_to_apply, iterable):
    return [function_to_apply(x) for x in iterable]


def ft_filter(function_to_apply, iterable):
    return [x for x in iterable if function_to_apply(x)]

def ft_reduce(function_to_apply, iterable):
    accum_value = 0
    for x in iterable:
        accum_value = function_to_apply(accum_value, x)
    return accum_value

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

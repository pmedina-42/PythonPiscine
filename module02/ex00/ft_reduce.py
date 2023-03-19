
def ft_reduce(function_to_apply, iterable):
    accum_value = 0
    for x in iterable:
        accum_value = function_to_apply(accum_value, x)
    return accum_value

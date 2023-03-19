
def ft_filter(function_to_apply, iterable):
    return [x for x in iterable if function_to_apply(x)]

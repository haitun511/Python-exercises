def min(*args, **kwargs):
    key = kwargs.get("key", None)

    if len(args) == 1:
        args = list(*args)

    result = args[0]

    if key:
        for arg in args:
            if key(arg) < key(result):
                result = arg
    else:
        for arg in args:
            if arg < result:
                result = arg

    return result


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    if len(args) == 1:
        args = list(*args)

    result = args[0]

    if key:
        for arg in args:
            if key(arg) > key(result):
                result = arg
    else:
        for arg in args:
            if arg > result:
                result = arg

    return result
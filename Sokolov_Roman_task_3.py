def type_logger(verbosity=0):
    def _type_logger(func):
        def wrapper(*args):
            result = func(*args)
            msg_content = {arg: type(arg) for arg in args}
            msg = f'{func.__name__} {msg_content}'
            if verbosity > 0:
                msg = f'{msg} ({", ".join(map(str, args))})'
            if verbosity > 1:
                msg = f'{msg} -> {list(result)}'
            return msg

        return wrapper

    return _type_logger


@type_logger(verbosity=2)
def cubes_input(*args):
    for arg in args:
        arg = arg ** 3
        yield arg


cubes = cubes_input(2)
print(cubes)

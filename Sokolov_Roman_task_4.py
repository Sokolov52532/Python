def val_checker(lamb, verbosity=0):
    def _val_checker(func):
        def wrapper(x):
            if not lamb(x):
                raise ValueError(f'wrong val {x}')
            result = func(x)
            msg = f'{func.__name__}'
            if verbosity > 0:
                msg = f'{msg} {x}'
            if verbosity > 1:
                msg = f'{msg} -> {result}'
            return msg

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0, verbosity=2)
def cubes_input(x):
    return x ** 3


cubes = cubes_input(-5)
print(cubes)

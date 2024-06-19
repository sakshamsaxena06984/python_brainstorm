def enforce_positional_arguments(num_arg):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if len(args) != num_arg:
                raise TypeError("provided wrong number of arguments")
            return func(*args, **kwargs)

        return wrapper

    return decorator



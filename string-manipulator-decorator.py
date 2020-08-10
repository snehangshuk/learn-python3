def reverse_decorator(print_func):
    def reverse_wrapper(*args, **kwargs):
        reverse_str = "".join(reversed(print_func(*args, **kwargs)))
        return reverse_str

    return reverse_wrapper


def uppercase_decorator(print_func):
    def uppercase_wrapper(*args, **kwargs):
        uppercase_str = print_func(*args, **kwargs).upper()
        return uppercase_str

    return uppercase_wrapper


@uppercase_decorator
@reverse_decorator
def print_string(string):
    return string


print(print_string("Snehangshu"))

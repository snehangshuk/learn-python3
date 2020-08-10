# Decorator adds more functionality to a given function
def title_decorator(print_name_function):
    def wrapper(*args, **kwargs):
        print("Mr. " + print_name_function(*args, **kwargs))

    return wrapper


# Main functions
@title_decorator
def print_my_name():
    return "Snehangshu Karmakar"


@title_decorator
def print_son_name():
    return "Somangshu Karmakar"


@title_decorator
def print_any_name(name):
    return name


# After use of annotations
print_my_name()
print_son_name()
print_any_name("Himangshu Shekhar Karmakar")

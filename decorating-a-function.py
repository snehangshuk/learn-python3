# How does decorating a function works

# Decorator adds more functionality to a given function
def title_decorator(print_name_function):
    def wrapper():
        print("Mr. " + print_name_function())

    return wrapper


# Main functions
def print_my_name():
    return "Snehangshu Karmakar"


def print_son_name():
    return "Somangshu Karmakar"


# Basic calling of decorated functions, but is more tedious this we use annotations
decorated_function = title_decorator(print_son_name)
decorated_function()

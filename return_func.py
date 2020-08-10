# function also acts like a object, thus can be passed as parameter or can be returned
def get_math_function(operation):  # + or -
    def add(n1, n2):
        return n1 + n2

    def sub(n1, n2):
        return n1 - n2

    if operation == "+":
        return add
    elif operation == "-":
        return sub


add_function = get_math_function("+")
sub_function = get_math_function("-")
print(add_function(5, 7))
print(sub_function(10, 2))
print(add_function)
